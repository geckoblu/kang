import os
import webbrowser

from PySide2.QtCore import Signal, qApp, QItemSelectionModel
from PySide2.QtWidgets import QMessageBox, QFileDialog, QTreeWidgetItem

from kang import PYTHON_RE_LIBRARY_URL, MATCH_NA, MATCH_OK, MATCH_FAIL, MATCH_PAUSED, MSG_NA, MSG_PAUSED, MATCH_NONE
from kang.gui.aboutDialog import AboutDialog
from kang.gui.importURLDialog import ImportURLDialog, ImportURLDialogMode
from kang.gui.mainWindowUI import MainWindowUI
from kang.gui.newUserDialog import NewUserDialog
from kang.gui.preferencesDialog import PreferencesDialog
from kang.gui.reportBugDialog import ReportBugDialog
from kang.modules.kngfile import KngFile
from kang.modules.preferences import Preferences
from kang.modules.recentfiles import RecentFiles
from kang.modules.util import getConfigDirectory
from kang.modules.windowsettings import WindowSettings


GEO = 'kang_geometry'

SHORTMESSAGE_DURATION = 3  # seconds

tr = lambda msg: msg


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

        self.importFilename = ''
        self._filename = ''

        # Temporary stores last opened URL
        self._lastImportedURL = ''

        # This property holds whether the document shown in the window has unsaved changes
        self._modified = False

        self.showRegexLibrary = False
        self.showRegexReferenceGuide = False

        self.updateStatus(MSG_NA, MATCH_NA)
        self._clearResults()

        windowSettings = WindowSettings()
        windowSettings.restore(self)

        self.show()

        self.preferences = Preferences()
        self.preferences.load()
        self.recentFiles = RecentFiles(self, self.preferences.recentFilesNum)

        self._signalException.connect(self.showReportBugDialog)
        self.regexReferencePanel.pasteSymbol.connect(self.pasteSymbol)

        # FIXME self.connect(self, SIGNAL('pasteRegexLib(PyQt_PyObject)'), self.pasteFromRegexLib)

        self.checkForKangDir()

    def checkForKangDir(self):
        kdir = getConfigDirectory()
        if os.access(kdir, os.X_OK):
            return

        newuserdialog = NewUserDialog(self)
        newuserdialog.exec_()

        try:
            os.mkdir(kdir, 0o755)
        except:
            message = '%s: %s' % (self.tr('Failed to create'), kdir)
            QMessageBox().critical(self, self.tr('ERROR'), message, buttons=QMessageBox.Ok)

    def _regexprocessorStatusChanged(self):
        statusValue, statusMessage = self._regexProcessor.getStatus()
        self.updateStatus(statusMessage, statusValue)

        allmatches = self._regexProcessor.getAllSpans()
        if allmatches:
            self.matchTextBrowser.setEnabled(True)
            self.groupTable.setEnabled(True)
            self.matchNumberSpinBox.setMaximum(len(allmatches))
            self.matchNumberSpinBox.setEnabled(True)
        else:
            # No match found
            self.matchTextBrowser.setDisabled(True)
            self.groupTable.setDisabled(True)
            self.matchNumberSpinBox.setValue(0)
            self.matchNumberSpinBox.setDisabled(True)

        replaceString = self.replaceTextEdit.toPlainText()
        if allmatches and replaceString:
            self.replaceTextBrowser.setEnabled(True)
            self.replaceNumberSpinBox.setMaximum(len(allmatches))
            self.replaceNumberSpinBox.setEnabled(True)
        else:
            # No match found
            self.replaceTextBrowser.setDisabled(True)
            self.replaceNumberSpinBox.setValue(0)
            self.replaceNumberSpinBox.setDisabled(True)

        self._populateGroupTable()
        self._populateMatchTextbrowser()
        self._populateReplaceTextbrowser()
        self._populateCodeTextBrowser()
        self._populateEmbeddedFlags()

    def updateStatus(self, statusString, statusValue, duration=0):
        if duration > 0:
            self.statusBar().showMessage(statusString, duration * 1000)
        else:
            self.statusBar().clearMessage()
            self.statusBar().showPermanentMessage(statusString)

    def _setModified(self):
        # invoked whenever the user has _modified something
        self._modified = True

    def pause(self, paused):
        if paused:
            self._regexProcessor.pause()
            self.updateStatus(MSG_PAUSED, MATCH_PAUSED)
            self.matchTextBrowser.setDisabled(True)
            self.matchTextBrowser.setPlainText('')
            self.groupTable.setDisabled(True)
            self.groupTable.clear()
            self.replaceTextBrowser.setDisabled(True)
            self.replaceTextBrowser.setPlainText('')
            self.codeTextBrowser.setDisabled(True)
            self.codeTextBrowser.setPlainText('')
            self.matchNumberSpinBox.setEnabled(False)
            self.replaceNumberSpinBox.setEnabled(False)
        else:
            self.matchTextBrowser.setEnabled(True)
            self.groupTable.setEnabled(True)
            self.replaceTextBrowser.setEnabled(True)
            self.codeTextBrowser.setEnabled(True)
            self.matchNumberSpinBox.setEnabled(True)
            self.replaceNumberSpinBox.setEnabled(True)
            self._regexProcessor.unpause()

    def examine(self, examine):
        if examine:
            self._regexSaved = self.regexMultiLineEdit.toPlainText()

            self.stringMultiLineEdit.setReadOnly(True)
            self.regexMultiLineEdit.setReadOnly(True)
            self.replaceTextEdit.setReadOnly(True)
            self.stringMultiLineEdit.setEnabled(False)
            self.regexMultiLineEdit.setEnabled(False)
            self.replaceTextEdit.setEnabled(False)
            self.stringMultiLineEdit.setTextColor(self.normalTextColor)
            self.stringMultiLineEdit.setText(self.stringMultiLineEdit.toPlainText())
            self.replaceTextEdit.setTextColor(self.normalTextColor)
            self.replaceTextEdit.setText(self.replaceTextEdit.toPlainText())

            matching, dontmatching = self._regexProcessor.examine()
            self._refreshRegexWidget(matching, dontmatching)
        else:
            self.regexMultiLineEdit.setReadOnly(False)
            self.stringMultiLineEdit.setReadOnly(False)
            self.replaceTextEdit.setReadOnly(False)
            self.stringMultiLineEdit.setEnabled(True)
            self.regexMultiLineEdit.setEnabled(True)
            self.replaceTextEdit.setEnabled(True)
            self.regexMultiLineEdit.setTextColor(self.normalTextColor)

            self.regexMultiLineEdit.setPlainText(self._regexSaved)

    def _refreshRegexWidget(self, matching, dontmatching):
        self.regexMultiLineEdit.clear()

        self.regexMultiLineEdit.blockSignals(True)
        self.regexMultiLineEdit.insertPlainText(matching)
        self.regexMultiLineEdit.setTextColor(self.disabledTextColor)
        self.regexMultiLineEdit.insertPlainText(dontmatching)
        self.regexMultiLineEdit.blockSignals(False)

        self._regexProcessor.setRegexString(matching)

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

    def _populateGroupTable(self):
        groups = self._regexProcessor.getAllGroups()

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

        self.groupTable.expandAll()
        for column in range(0, self.groupTable.columnCount()):
            self.groupTable.resizeColumnToContents(column)

        model = self.groupTable.model()
        selectionModel = self.groupTable.selectionModel()

        evidenceMatchNumber = self.matchNumberSpinBox.value()

        if evidenceMatchNumber > 0:
            row = evidenceMatchNumber - 1
            index = model.index(row, 0)
            selectionModel.select(index, QItemSelectionModel.Select | QItemSelectionModel.Rows)
            for i in range(0, model.rowCount(index)):
                childIndex = model.index(i, 0, index)
                selectionModel.select(childIndex, QItemSelectionModel.Select | QItemSelectionModel.Rows)

    def _populateMatchTextbrowser(self):
        matchNumber = self.matchNumberSpinBox.value()
        if matchNumber > 0:
            spans = [self._regexProcessor.getSpan(matchNumber - 1)]
        else:
            spans = self._regexProcessor.getAllSpans()
        self._populateText(spans, self.matchTextBrowser)

    def _populateReplaceTextbrowser(self):
        replaceString = self.replaceTextEdit.toPlainText()
        allmatches = self._regexProcessor.getAllSpans()

        if replaceString and allmatches:
            statusValue, strings = self._regexProcessor.replace(self.replaceNumberSpinBox.value())

            if statusValue == MATCH_OK:
                self._colorizeStrings(strings, self.replaceTextBrowser)
            else:
                self.replaceTextBrowser.clear()
                self.updateStatus("Error in replace string: %s" % strings, statusValue, SHORTMESSAGE_DURATION)
        else:
            self.replaceTextBrowser.clear()

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

        textColors = [self.normalTextColor, self.highlightTextColor]
        foregroundColors = [self.normalForegroundColor, self.highlightForegroundColor]

        widget.setTextColor(self.normalTextColor)

        i = 0
        pos = widget.textCursor()
        for s in strings:
            widget.setTextColor(textColors[i % 2])
            widget.setTextBackgroundColor(foregroundColors[i % 2])
            widget.insertPlainText(s)
            if i == cursorOffset:
                pos = widget.textCursor()
            i += 1

        widget.setTextCursor(pos)

    def fileExit(self, ev):
        self.closeEvent(ev)

    def closeEvent(self, ev):
        self._checkModified()

        # saveWindowSettings(self, GEO)
        settings = WindowSettings()
        settings.save(self)

        ev.accept()

    def _importURL(self):
        dialog = ImportURLDialog(self, self._lastImportedURL)
        (ok, text, url, mode) = dialog.getURL()
        if ok:
            self._lastImportedURL = url
            if mode == ImportURLDialogMode.HTML:
                self.stringMultiLineEdit.setHtml(text)
                text = self.stringMultiLineEdit.toPlainText()
                self.stringMultiLineEdit.setPlainText(text)
            else:
                self.stringMultiLineEdit.setPlainText(text)

    def importFile(self):
        (filename, _filter) = QFileDialog.getOpenFileName(self,
                                                          self.tr("Import File"),
                                                          self.importFilename, "All (*)")

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
        self._checkModified()
        self._filename = ''

        self.regexMultiLineEdit.setPlainText('')
        self.stringMultiLineEdit.setPlainText('')
        self.replaceTextEdit.setPlainText('')

        self.ignorecaseCheckBox.setChecked(False)
        self.multilineCheckBox.setChecked(False)
        self.dotallCheckBox.setChecked(False)
        self.verboseCheckBox.setChecked(False)
        self.asciiCheckBox.setChecked(False)

        self._modified = False

    def fileOpen(self):
        (filename, _filter) = QFileDialog.getOpenFileName(self,
                                                          self.tr("Open Kang File"),
                                                          self._filename,
                                                          "*.kng\nAll (*)",
                                                          )
        if filename:
            self.loadFile(filename)

    def fileSave(self):
        if not self._filename:
            self.fileSaveAs()
            return

        regexString = self.regexMultiLineEdit.toPlainText()
        matchString = self.stringMultiLineEdit.toPlainText()
        replaceString = self.replaceTextEdit.toPlainText()

        try:
            kngfile = KngFile(self._filename,
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

            self._modified = False

            basename = os.path.basename(self._filename)
            msg = '%s %s' % (basename, self.tr("successfully saved"))
            self.updateStatus(msg, MATCH_NONE, SHORTMESSAGE_DURATION)
            self.recentFiles.add(self._filename)
        except IOError as ex:
            msg = str(ex)
            self.updateStatus(msg, MATCH_NONE, SHORTMESSAGE_DURATION)

    def fileSaveAs(self):
        (filename, _filter) = QFileDialog.getSaveFileName(self,
                                                          self.tr("Save Kang File"),
                                                          self._filename,
                                                          "*.kng\nAll (*)"
                                                          )
        if not filename:
            self.updateStatus(self.tr("No file selected to save"), MATCH_NONE, SHORTMESSAGE_DURATION)
            return
        filename = os.path.normcase(filename)

        basename = os.path.basename(filename)
        if basename.find('.') == -1:
            filename += '.kng'

        self._filename = filename
        self.fileSave()

    def fileRevert(self):
        if not self._filename:
            self.updateStatus(self.tr("There is no _filename to revert"), MATCH_NONE, SHORTMESSAGE_DURATION)
            return

        self.loadFile(self._filename)

    def loadFile(self, filename):
        self._checkModified()

        try:
            self._filename = ''

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

            self._filename = filename
            self.recentFiles.add(self._filename)

            # Reset Pause and Examine status
            self.editPauseAction.setChecked(False)
            self.pause(False)
            self.editExamineAction.setChecked(False)
            self._regexSaved = kngfile.regexString
            self.examine(False)
            self._regexProcessor.unpause()

            basename = os.path.basename(filename)
            msg = '%s %s' % (basename, self.tr("loaded successfully"))
            self.updateStatus(msg, MATCH_NONE, SHORTMESSAGE_DURATION)
            self._modified = False

            return True

        except IOError as ex:
            msg = str(ex)
            self.updateStatus(msg, MATCH_NONE, SHORTMESSAGE_DURATION)
            self.recentFiles.remove(filename)
            return False

    def pasteSymbol(self, symbol):
        self.regexMultiLineEdit.insertPlainText(symbol)

    def _checkModified(self):

        if not self.preferences.askSave:
            return

        if self.preferences.askSaveOnlyForNamedProjects and not self._filename:
            return

        if self._modified:
            message = self.tr("You have made changes. Would you like to save them before continuing?")

            prompt = QMessageBox().warning(self,
                                           self.tr("Save changes?"),
                                           message,
                                           QMessageBox.No,
                                           QMessageBox.Yes)

            if prompt == 0:
                self.fileSave()
                if not self._filename:
                    self._checkModified()

    def pasteFromRegexLib(self, regexLibDict):
        self._filename = ''
        self._checkModified()

        self.regexMultiLineEdit.setPlainText(regexLibDict.get('regex', ''))
        self.stringMultiLineEdit.setPlainText(regexLibDict.get('text', ''))
        self.replaceTextEdit.setPlainText(regexLibDict.get('replace', ''))

        # TODO set the current page if applicable ?
        # try:
        #    # set the current page if applicable
        #    self.resultTabWidget.setCurrentPage(int(regexLibDict.get('tab', '')))
        # except ValueError:
        #    pass
        self._modified = False

    def widgetMethod(self, methodstr, anywidget=False):
        # execute the methodstr of widget only if widget
        # is one of the editable widgets OR if the method
        # may be applied to any widget.
        widget = qApp.focusWidget()
        if anywidget or widget in (self.regexMultiLineEdit,
                                   self.stringMultiLineEdit,
                                   self.replaceTextEdit,
                                   self.codeTextBrowser):
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

    def _editPreferences(self):
        dialog = PreferencesDialog(self, self.preferences)
        (ok, preferences) = dialog.getPreferences()
        if ok:
            self.preferences = preferences
            self.recentFiles.setNumShown(self.preferences.recentFilesNum)
            self.preferences.save()

    def helpPythonRegex(self):
        webbrowser.open(PYTHON_RE_LIBRARY_URL)

    def helpRegexReferenceGuide(self, showRegexReferenceGuide):
        self.showRegexReferenceGuide = showRegexReferenceGuide

        if showRegexReferenceGuide:
            index = self.splitterTabWidget.insertTab(0, self.regexReferencePanel, tr("Regex Reference Guide"))
            self.splitterTabWidget.setCurrentIndex(index)
        else:
            index = self.splitterTabWidget.indexOf(self.regexReferencePanel)
            self.splitterTabWidget.removeTab(index)

        self.splitterTabWidget.setVisible(self.showRegexReferenceGuide or self.showRegexLibrary)

    def helpRegexLibrary(self, showRegexLibrary):
        self.showRegexLibrary = showRegexLibrary

        if showRegexLibrary:
            index = self.splitterTabWidget.insertTab(1, self.regexLibraryPanel, tr("Regex Library"))
            self.splitterTabWidget.setCurrentIndex(index)
        else:
            index = self.splitterTabWidget.indexOf(self.regexLibraryPanel)
            self.splitterTabWidget.removeTab(index)

        self.splitterTabWidget.setVisible(self.showRegexReferenceGuide or self.showRegexLibrary)

    def _updateSplitterStatus(self):
        pass

    def helpAbout(self):
        aboutWindow = AboutDialog(self)
        aboutWindow.show()

    def signalException(self, msg):
        self._signalException.emit(msg)

    def showReportBugDialog(self, msg):
        rbd = ReportBugDialog(self, msg)
        rbd.exec_()
