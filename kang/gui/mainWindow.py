import os
import webbrowser

from PySide2.QtCore import Qt, Signal, qApp
from PySide2.QtGui import QColor, QPalette, QBrush
from PySide2.QtWidgets import QMessageBox, QFileDialog, QTreeWidgetItem

from kang import KANG_WEBSITE, PYTHON_RE_LIBRARY_URL, MATCH_NA, MATCH_OK, MATCH_FAIL, MATCH_PAUSED, MSG_NA, MSG_PAUSED, MATCH_NONE
from kang.gui.aboutDialog import AboutDialog
from kang.gui.importURLDialog import ImportURLDialog
from kang.gui.mainWindowUI import MainWindowUI
from kang.gui.newUserDialog import NewUserDialog
from kang.gui.preferencesDialog import PreferencesDialog
from kang.gui.regexLibraryWindow import RegexLibraryWindow
from kang.gui.regexReferenceWindow import RegexReferenceWindow
from kang.gui.reportBugDialog import ReportBugDialog
from kang.modules.kngfile import KngFile
from kang.modules.preferences import Preferences
from kang.modules.recentfiles import RecentFiles
from kang.modules.util import findFile, restoreWindowSettings, saveWindowSettings, getConfigDirectory

STATE_UNEDITED = 0
STATE_EDITED = 1

GEO = 'kang_geometry'

# colors for normal & examination mode
QCOLOR_WHITE = QColor(Qt.white)  # normal
QCOLOR_EVIDENCE = QColor('#DDFFFF')  # Evidenced Match
QCOLOR_EXAMINE = QColor('#DDFFFF')  # Examine status

SHORTMESSAGE_DURATION = 5  # seconds


##############################################################################
#
# The Kang class which defines the main functionality and user interaction
#
##############################################################################
class MainWindow(MainWindowUI):

    _signalException = Signal(str)

    def __init__(self):
        MainWindowUI.__init__(self)

        self._regexSaved = ''
        self._isExamined = False
        self._isPaused = False

        self.importFilename = ''
        self.filename = ''

        self.url = KANG_WEBSITE
        self.editstate = STATE_UNEDITED

        self.refWin = None
        self.regexlibwin = None

        self.updateStatus(MSG_NA, MATCH_NA)
        self._clearResults()

        restoreWindowSettings(self, GEO)

        # TODO self._showReplaceWidgets(False)

        self.show()

        self.preferences = Preferences()
        self.recentFiles = RecentFiles(self, self.preferences.recentFilesNum)
        self.preferencesChanged()

        self._signalException.connect(self.showReportBugDialog)

        # FIXME self.connect(self, SIGNAL('preferencesChanged()'), self.preferencesChanged)
        # FIXME self.connect(self, SIGNAL('pasteSymbol(PyQt_PyObject)'), self.pasteSymbol)
        # FIXME self.connect(self, SIGNAL('urlImported(PyQt_PyObject, PyQt_PyObject)'), self.urlImported)
        # FIXME self.connect(self, SIGNAL('pasteRegexLib(PyQt_PyObject)'), self.pasteFromRegexLib)

        self.checkForKangDir()

    def checkForKangDir(self):
        kdir = getConfigDirectory()
        if os.access(kdir, os.X_OK):
            return

        newuserdialog = NewUserDialog(self)
        newuserdialog.setModal(True)
        newuserdialog.exec_()

        try:
            os.mkdir(kdir, 0o755)
        except:
            message = '%s: %s' % (self.tr('Failed to create'), kdir)
            QMessageBox().critical(self, self.tr('ERROR'), message, buttons=QMessageBox.Ok)

    def _regexStatusChanged(self):
        statusValue, statusMessage = self._regexProcessor.getStatus()
        self.updateStatus(statusMessage, statusValue)

        allmatches = self._regexProcessor.getAllSpans()
        if allmatches and len(allmatches):
            self.matchNumberSpinBox.setMaximum(len(allmatches))
            self.matchNumberSpinBox.setEnabled(True)
            self.replaceNumberSpinBox.setMaximum(len(allmatches))
            self.replaceNumberSpinBox.setEnabled(True)
        else:
            self.matchNumberSpinBox.setEnabled(False)
            self.replaceNumberSpinBox.setEnabled(False)

        self._populateGroupTable()
        self._populateMatchTextbrowser()
        self._populateMatchAllTextbrowser()
        self._populateReplaceTextbrowser()
        self._populateCodeTextBrowser()
        self._populateEmbeddedFlags()

    def updateStatus(self, statusString, statusValue, duration=0):
        if duration > 0:
            self.statusBar().showMessage(statusString, duration * 1000)
        else:
            self.statusBar().clearMessage()
            self.statusBar().showPermanentMessage(statusString)

    def _edited(self):
        # invoked whenever the user has _edited something
        self.editstate = STATE_EDITED

    def pause(self):
        self._isPaused = not self._isPaused

        if self._isPaused:
            self._regexProcessor.pause()
            self.updateStatus(MSG_PAUSED, MATCH_PAUSED)
            self.matchNumberSpinBox.setDisabled(True)
            self.replaceNumberSpinBox.setDisabled(True)
        else:
            self.matchNumberSpinBox.setEnabled(True)
            self.replaceNumberSpinBox.setEnabled(True)
            self._regexProcessor.unpause()

    def examine(self):
        self._isExamined = not self._isExamined

        if self._isExamined:
            color = QCOLOR_EXAMINE
            self.regexMultiLineEdit.setReadOnly(True)
            self.stringMultiLineEdit.setReadOnly(True)
            self.replaceTextEdit.setReadOnly(True)
            self._regexSaved, new = self._regexProcessor.examine()
            self._refreshRegexWidget(color, new)
        else:
            color = QCOLOR_WHITE
            self.regexMultiLineEdit.setReadOnly(False)
            self.stringMultiLineEdit.setReadOnly(False)
            self.replaceTextEdit.setReadOnly(False)
            self._refreshRegexWidget(color, self._regexSaved)

    def _refreshRegexWidget(self, color, regex):
        p = self.regexMultiLineEdit.palette()
        p.setColor(QPalette.Base, color)
        self.regexMultiLineEdit.setPalette(p)

        self.regexMultiLineEdit.blockSignals(1)
        self.regexMultiLineEdit.clear()
        self.regexMultiLineEdit.blockSignals(0)
        self.regexMultiLineEdit.setPlainText(regex)

    def _matchNumberChanged(self):
        self._populateGroupTable()
        self._populateMatchTextbrowser()

    def _replaceNumberChanged(self):
        self._populateReplaceTextbrowser()

    def _clear(self):
        self._clearResults()

        self.matchNumberSpinBox.setValue(0)
        self.regexMultiLineEdit.setPlainText('')
        self.stringMultiLineEdit.setPlainText('')
        self.replaceTextEdit.setPlainText('')

        self.ignorecaseCheckBox.setChecked(False)
        self.multilineCheckBox.setChecked(False)
        self.dotallCheckBox.setChecked(False)
        self.verboseCheckBox.setChecked(False)
        self.asciiCheckBox.setChecked(False)

    def _clearResults(self):
        self.groupTable.clear()
        self.codeTextBrowser.setPlainText('')
        self.matchTextBrowser.setPlainText('')
        self.matchNumberSpinBox.setEnabled(False)
        self.replaceNumberSpinBox.setEnabled(False)
        self.replaceTextBrowser.setPlainText('')
        self.matchAllTextBrowser.setPlainText('')

    def _showReplaceWidgets(self, show):
        if show:
            self.spacerLabel.show()
            self.replaceLabel.show()
            self.replaceNumberSpinBox.show()
            self.replaceNumberSpinBox.setEnabled(True)
            self.replaceTextBrowser.setEnabled(True)
        else:
            # self.spacerLabel.hide()
            self.replaceLabel.hide()
            self.replaceNumberSpinBox.hide()
            self.replaceTextBrowser.clear()
            self.replaceTextBrowser.setDisabled(True)

    def _populateGroupTable(self):
        groups = self._regexProcessor.getAllGroups()

        brush = QBrush(QCOLOR_EVIDENCE)
        evidenceMatchNumber = self.matchNumberSpinBox.value()

        self.groupTable.clear()

        for matchNumber, group in enumerate(groups, start=1):
            # print(matchNumber, group)

            child = None
            for subGroup in group:
                if not child:
                    child = QTreeWidgetItem(self.groupTable)
                    child.setText(0, str(matchNumber))
                    item = child
                else:
                    subchild = QTreeWidgetItem()
                    child.addChild(subchild)
                    item = subchild

                item.setText(1, str(subGroup[0]))
                item.setText(2, subGroup[1])
                item.setText(3, subGroup[2])
                if matchNumber == evidenceMatchNumber:
                    item.setBackground(0, brush)
                    item.setBackground(1, brush)
                    item.setBackground(2, brush)
                    item.setBackground(3, brush)

        self.groupTable.expandAll()
        for column in range(0, self.groupTable.columnCount()):
            self.groupTable.resizeColumnToContents(column)

    def _populateMatchTextbrowser(self):
        matchNumber = self.matchNumberSpinBox.value()
        if matchNumber > 0:
            spans = [self._regexProcessor.getSpan(matchNumber - 1)]
        else:
            spans = self._regexProcessor.getAllSpans()
        self._populateText(spans, self.matchTextBrowser)

    def _populateMatchAllTextbrowser(self):
        spans = self._regexProcessor.getAllSpans()
        self._populateText(spans, self.matchAllTextBrowser)

    def _populateReplaceTextbrowser(self):

        statusValue, strings = self._regexProcessor.replace(self.replaceNumberSpinBox.value())

        if statusValue == MATCH_OK:
            self._colorizeStrings(strings, self.replaceTextBrowser)
        else:
            self.replaceTextBrowser.clear()
            self.updateStatus("Error in replace string: %s" % strings, statusValue, SHORTMESSAGE_DURATION)

    def _populateCodeTextBrowser(self):
        self.codeTextBrowser.setPlainText(self._regexProcessor.getRegexCode())

    def _populateEmbeddedFlags(self):

        self.ignorecaseCheckBox.setEnabled(True)
        self.multilineCheckBox.setEnabled(True)
        self.dotallCheckBox.setEnabled(True)
        self.asciiCheckBox.setEnabled(True)
        self.verboseCheckBox.setEnabled(True)

        flags = self._regexProcessor.getEmbeddedFlags()
        for flag in flags:
            if flag == 'i':
                self.ignorecaseCheckBox.setEnabled(False)
                self.ignorecaseCheckBox.setChecked(True)
            elif flag == 'L':
                self.updateStatus(self.tr("Locale Flag not supported"), MATCH_NONE, SHORTMESSAGE_DURATION)
            elif flag == 'm':
                self.multilineCheckBox.setEnabled(False)
                self.multilineCheckBox.setChecked(True)
            elif flag == 's':
                self.dotallCheckBox.setEnabled(False)
                self.dotallCheckBox.setChecked(True)
            elif flag == 'u':
                self.asciiCheckBox.setEnabled(False)
                self.asciiCheckBox.setChecked(True)
            elif flag == 'x':
                self.verboseCheckBox.setEnabled(False)
                self.verboseCheckBox.setChecked(True)

    def _populateText(self, spans, widget):
        widget.clear()

        if not spans:
            return

        idx = 0
        text = self.stringMultiLineEdit.toPlainText()
        strings = []
        for span in spans:
            s = text[idx:span[0]]

            idx = span[1]
            strings.append(s)
            strings.append(text[span[0]:span[1]])

        if 0 <= idx <= len(text):
            strings.append(text[idx:])

        self._colorizeStrings(strings, widget)

    def _colorizeStrings(self, strings, widget, cursorOffset=0):
        widget.clear()

        colors = (QCOLOR_WHITE, QCOLOR_EVIDENCE)
        i = 0
        pos = widget.textCursor()
        for s in strings:
            widget.setTextBackgroundColor(colors[i % 2])
            widget.insertPlainText(s)
            if i == cursorOffset:
                pos = widget.textCursor()
            i += 1

        widget.setTextCursor(pos)

    def fileExit(self, ev):
        self.closeEvent(ev)

    def closeEvent(self, ev):
        self.checkEditState()
        saveWindowSettings(self, GEO)

        try:
            self.regexlibwin.close()
        except:
            pass

        try:
            self.refWin.close()
        except:
            pass
        ev.accept()

    def importURL(self):
        urldialog = ImportURLDialog(self, self.url)
        urldialog.show()

    def urlImported(self, html, url):
        self.url = url
        self.stringMultiLineEdit.setPlainText(html)

    def importFile(self):
        (filename, _filter) = QFileDialog.getOpenFileName(self, self.tr("Import File"), self.importFilename, "All (*)")

        if not filename:
            self.updateStatus(self.tr("A file was not selected for import"), MATCH_NONE, SHORTMESSAGE_DURATION)
            return

        try:
            fp = open(filename, 'r')
        except:
            msg = self.tr("Could not open file for reading: ") + filename
            self.updateStatus(msg, MATCH_NONE, SHORTMESSAGE_DURATION)
            return

        self.importFilename = filename
        data = fp.read()
        fp.close()
        self.stringMultiLineEdit.setPlainText(data)

    def fileNew(self):
        self.checkEditState()
        self.filename = ''

        self.regexMultiLineEdit.setPlainText('')
        self.stringMultiLineEdit.setPlainText('')
        self.replaceTextEdit.setPlainText('')

        self.ignorecaseCheckBox.setChecked(False)
        self.multilineCheckBox.setChecked(False)
        self.dotallCheckBox.setChecked(False)
        self.verboseCheckBox.setChecked(False)
        self.asciiCheckBox.setChecked(False)

        self.editstate = STATE_UNEDITED

    def fileOpen(self):
        (filename, _filter) = QFileDialog.getOpenFileName(self,
                                                          self.tr("Open Kang File"),
                                                          self.filename,
                                                          "*.kng\nAll (*)",
                                                          )
        if filename:
            self.loadFile(filename)

    def fileSave(self):
        if not self.filename:
            self.fileSaveAs()
            return

        regexString = self.regexMultiLineEdit.toPlainText()
        matchString = self.stringMultiLineEdit.toPlainText()
        replaceString = self.replaceTextEdit.toPlainText()

        try:
            kngfile = KngFile(self.filename,
                              matchString,
                              regexString,
                              replaceString,
                              self.ignorecaseCheckBox.isChecked(),
                              self.multilineCheckBox.isChecked(),
                              self.dotallCheckBox.isChecked(),
                              self.verboseCheckBox.isChecked(),
                              self.asciiCheckBox.isChecked()
                              )
            kngfile.save()

            self.editstate = STATE_UNEDITED

            msg = '%s %s' % (self.filename,
                             self.tr("successfully saved"))
            self.updateStatus(msg, MATCH_NONE, SHORTMESSAGE_DURATION)
            self.recentFiles.add(self.filename)
        except IOError as ex:
            msg = str(ex)
            self.updateStatus(msg, MATCH_NONE, SHORTMESSAGE_DURATION)

    def fileSaveAs(self):
        (filename, _filter) = QFileDialog.getSaveFileName(self,
                                                          self.tr("Save Kang File"),
                                                          self.filename,
                                                          "*.kng\nAll (*)"
                                                          )
        if not filename:
            self.updateStatus(self.tr("No file selected to save"), MATCH_NONE, SHORTMESSAGE_DURATION)
            return
        filename = os.path.normcase(filename)

        basename = os.path.basename(filename)
        if basename.find('.') == -1:
            filename += '.kng'

        self.filename = filename
        self.fileSave()

    def fileRevert(self):
        if not self.filename:
            self.updateStatus(self.tr("There is no filename to revert"), MATCH_NONE, SHORTMESSAGE_DURATION)
            return

        self.loadFile(self.filename)

    def loadFile(self, filename):
        self.checkEditState()

        try:
            self.filename = ''

            kngfile = KngFile(filename)
            kngfile.load()

            self._clear()

            self._regexProcessor.pause()

            self.regexMultiLineEdit.setPlainText(kngfile.regexString)
            self.stringMultiLineEdit.setPlainText(kngfile.matchString)
            self.replaceTextEdit.setPlainText(kngfile.replaceString)

            self.ignorecaseCheckBox.setChecked(kngfile.flagIgnorecase)
            self.multilineCheckBox.setChecked(kngfile.flagMultiline)
            self.dotallCheckBox.setChecked(kngfile.flagDotall)
            self.verboseCheckBox.setChecked(kngfile.flagVerbose)
            self.asciiCheckBox.setChecked(kngfile.flagAscii)

            self.filename = filename
            self.recentFiles.add(self.filename)

            self._regexProcessor.unpause()

            msg = '%s %s' % (filename, self.tr("loaded successfully"))
            self.updateStatus(msg, MATCH_NONE, SHORTMESSAGE_DURATION)
            self.editstate = STATE_UNEDITED
            return True

        except IOError as ex:
            msg = str(ex)
            self.updateStatus(msg, MATCH_NONE, SHORTMESSAGE_DURATION)
            self.recentFiles.remove(filename)
            return False

    def pasteSymbol(self, symbol):
        self.regexMultiLineEdit.insertPlainText(symbol)

    def checkEditState(self):

        if not self.preferences.askSave:
            return

        if self.preferences.askSaveOnlyForNamedProjects and not self.filename:
            return

        if self.editstate == STATE_EDITED:
            message = self.tr("You have made changes. Would you like to save them before continuing?")

            prompt = QMessageBox().warning(self,
                                           self.tr("Save changes?"),
                                           message,
                                           QMessageBox.No,
                                           QMessageBox.Yes)

            if prompt == 0:
                self.fileSave()
                if not self.filename:
                    self.checkEditState()

    def pasteFromRegexLib(self, regexLibDict):
        self.filename = ''
        self.checkEditState()

        self.regexMultiLineEdit.setPlainText(regexLibDict.get('regex', ''))
        self.stringMultiLineEdit.setPlainText(regexLibDict.get('text', ''))
        self.replaceTextEdit.setPlainText(regexLibDict.get('replace', ''))

        # TODO set the current page if applicable ?
        # try:
        #    # set the current page if applicable
        #    self.resultTabWidget.setCurrentPage(int(regexLibDict.get('tab', '')))
        # except ValueError:
        #    pass
        self.editstate = STATE_UNEDITED

    def widgetMethod(self, methodstr, anywidget=False):
        # execute the methodstr of widget only if widget
        # is one of the editable widgets OR if the method
        # may be applied to any widget.
        widget = qApp.focusWidget()
        if anywidget or (
                widget == self.regexMultiLineEdit or
                widget == self.stringMultiLineEdit or
                widget == self.replaceTextEdit or
                widget == self.codeTextBrowser):
            try:
                eval('widget.%s' % methodstr)
            except:
                pass

    def editUndo(self):
        self.widgetMethod('undo()')

    def editRedo(self):
        self.widgetMethod('redo()')

    def editCopy(self):
        self.widgetMethod('copy()', 1)

    def editCut(self):
        self.widgetMethod('cut()')

    def editPaste(self):
        self.widgetMethod('paste()')

    def editPreferences(self):
        sd = PreferencesDialog(self, self.preferences)
        sd.showPrefsDialog()

    def preferencesChanged(self):
        self.recentFiles.setNumShown(self.preferences.recentFilesNum)

    def helpHelp(self):
        f = findFile('doc', 'index.html')
        if f:
            webbrowser.open('file://%s' % f)
        else:
            webbrowser.open('%s/doc/index.html' % KANG_WEBSITE)

    def helpPythonRegex(self):
        webbrowser.open(PYTHON_RE_LIBRARY_URL)

    def helpRegexLib(self):
        self.regexlibwin = RegexLibraryWindow(self)
        self.regexlibwin.show()

    def helpAbout(self):
        aboutWindow = AboutDialog(self)
        aboutWindow.show()

    def helpVisitKangWebsite(self):
        webbrowser.open(KANG_WEBSITE)

    def referenceGuide(self):
        self.refWin = RegexReferenceWindow(self)
        self.refWin.show()

    def signalException(self, msg):
        self._signalException.emit(msg)

    def showReportBugDialog(self, msg):
        rbd = ReportBugDialog(self, msg)
        rbd.exec_()
