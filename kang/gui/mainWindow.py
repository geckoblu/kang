from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import os
import re
import webbrowser

from kang import KANG_WEBSITE, PYTHON_RE_LIBRARY_URL, MATCH_NA, MATCH_OK, MATCH_FAIL, MATCH_PAUSED, MSG_NA, MSG_PAUSED, MATCH_NONE
from kang.gui.aboutDialog import AboutDialog
from kang.gui.importURLDialog import ImportURLDialog
from kang.gui.mainWindowBA import MainWindowBA
from kang.gui.newUserDialog import NewUserDialog
from kang.gui.preferencesDialog import PreferencesDialog
from kang.gui.regexLibraryWindow import RegexLibraryWindow
from kang.gui.regexReferenceWindow import RegexReferenceWindow
from kang.gui.reportBugDialog import ReportBugDialog
from kang.gui.statusbar import StatusBar
from kang.images import getIcon, getPixmap
from kang.modules.kngfile import KngFile
from kang.modules.myPyQtSignal import MyPyQtSignaL
from kang.modules.preferences import Preferences
from kang.modules.recentfiles import RecentFiles
from kang.modules.regexprocessor import RegexProcessor
from kang.modules.util import findFile, restoreWindowSettings, saveWindowSettings, \
    getConfigDirectory


STATE_UNEDITED = 0
STATE_EDITED = 1

GEO = 'kang_geometry'

# colors for normal & examination mode
QCOLOR_WHITE = QColor(Qt.white)  # normal
QCOLOR_LIGHTCYAN = QColor('#DDFFFF')  # examine

# Initialized in the __init__ method because QPixmap should be loaded in the main thread
STATUS_PIXMAPS_DICT = {}


##############################################################################
#
# The Kang class which defines the main functionality and user interaction
#
##############################################################################
class MainWindow(MainWindowBA):

    # TODO __signalException = pyqtSignal(str)
    __signalException = MyPyQtSignaL()

    def __init__(self, filename=''):
        MainWindowBA.__init__(self)

        # Initialized here because QPixmap should be loaded in the main thread
        STATUS_PIXMAPS_DICT[MATCH_NA] = getPixmap('yellowStatusIcon.xpm')
        STATUS_PIXMAPS_DICT[MATCH_OK] = getPixmap('greenStatusIcon.xpm')
        STATUS_PIXMAPS_DICT[MATCH_FAIL] = getPixmap('redStatusIcon.xpm')
        STATUS_PIXMAPS_DICT[MATCH_PAUSED] = getPixmap('pauseStatusIcon.xpm')

        self._rp = RegexProcessor()
        self._rp.connect(self._regexStatusChanged)

        self._regexSaved = ''
        self._isExamined = False
        self._isPaused = False

        self.importFilename = ''
        self.filename = ''

        self.url = KANG_WEBSITE
        self.editstate = STATE_UNEDITED

        header = self.groupTable.horizontalHeader()
        # FIXME header.setResizeMode(QHeaderView.Stretch)
        # header.setStretchLastSection(True)

        self.refWin = None
        self.regexlibwin = None

        self.setWindowIcon(getIcon('kang-icon'))

        self.statusbar = StatusBar(self)

        self.loadToolbarIcons()

        self.updateStatus(MSG_NA, MATCH_NA)
        self._clearResults()

        restoreWindowSettings(self, GEO)

        self._showReplaceWidgets(False)

        self.show()

        self.preferences = Preferences()
        self.recentFiles = RecentFiles(self, self.preferences.recentFilesNum)
        self.preferencesChanged()

        if filename and self.openFile(filename):
            qApp.processEvents()

        # FIXME self._signalException.connect(self.showReportBugDialog)

        self.connect(self, SIGNAL('preferencesChanged()'), self.preferencesChanged)
        self.connect(self, SIGNAL('pasteSymbol(PyQt_PyObject)'), self.pasteSymbol)
        self.connect(self, SIGNAL('urlImported(PyQt_PyObject, PyQt_PyObject)'), self.urlImported)
        self.connect(self, SIGNAL('pasteRegexLib(PyQt_PyObject)'), self.pasteFromRegexLib)

        self.checkForKangDir()

    def loadToolbarIcons(self):
        self.fileOpenAction.setIcon(getIcon('document-open'))
        self.fileSaveAction.setIcon(getIcon('document-save'))
        self.editCutAction.setIcon(getIcon('edit-cut'))
        self.editCopyAction.setIcon(getIcon('edit-copy'))
        self.editPasteAction.setIcon(getIcon('edit-paste'))
        self.editPauseAction.setIcon(getIcon('media-playback-pause'))
        self.examineAction.setIcon(getIcon('edit-find'))
        self.helpRegexReferenceAction.setIcon(getIcon('book'))
        self.helpRegexLibAction.setIcon(getIcon('library'))

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
        statusValue, statusMessage = self._rp.getStatus()
        self.updateStatus(statusMessage, statusValue)

        allmatches = self._rp.getAllSpans()
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
        pixmap = STATUS_PIXMAPS_DICT.get(statusValue)

        self.statusbar.setMessage(statusString, duration, pixmap)

    def edited(self):
        # invoked whenever the user has edited something
        self.editstate = STATE_EDITED

    def pause(self):
        self._isPaused = not self._isPaused

        if self._isPaused:
            self._rp.pause()
            self.updateStatus(MSG_PAUSED, MATCH_PAUSED)
            self.matchNumberSpinBox.setDisabled(True)
            self.replaceNumberSpinBox.setDisabled(True)
        else:
            self.matchNumberSpinBox.setEnabled(True)
            self.replaceNumberSpinBox.setEnabled(True)
            self._rp.unpause()

    def examine(self):
        self._isExamined = not self._isExamined

        if self._isExamined:
            color = QCOLOR_LIGHTCYAN
            self.regexMultiLineEdit.setReadOnly(True)
            self.stringMultiLineEdit.setReadOnly(True)
            self.replaceTextEdit.setReadOnly(True)
            self._regexSaved, new = self._rp.examine()
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

    def matchNumSlot(self, num):
        self._populateGroupTable()
        self._populateMatchTextbrowser()

    def replaceNumSlot(self, num):
        self._populateReplaceTextbrowser()

    def regexChangedSlot(self):
        regexString = self.regexMultiLineEdit.toPlainText()
        self._rp.setRegexString(regexString)

    def stringChangedSlot(self):
        matchString = self.stringMultiLineEdit.toPlainText()
        self._rp.setMatchString(matchString)

    def replaceChangedSlot(self):
        replaceString = self.replaceTextEdit.toPlainText()
        self._rp.setReplaceString(replaceString)
        self._showReplaceWidgets(replaceString != '')

    def checkboxSlot(self):
        self._rp.setIgnorecaseFlag(self.ignorecaseCheckBox.isChecked())
        self._rp.setMultilineFlag(self.multilineCheckBox.isChecked())
        self._rp.setDotallFlag(self.dotallCheckBox.isChecked())
        self._rp.setVerboseFlag(self.verboseCheckBox.isChecked())
        self._rp.setLocaleFlag(self.localeCheckBox.isChecked())
        self._rp.setUnicodeFlag(self.unicodeCheckBox.isChecked())

    def setFlags(self, flags):
        """From the given integer value of flags, set the checkboxes.
           This is used when loading a saved file
        """
        self.ignorecaseCheckBox.setChecked(flags & re.IGNORECASE)
        self.multilineCheckBox.setChecked(flags & re.MULTILINE)
        self.dotallCheckBox.setChecked(flags & re.DOTALL)
        self.verboseCheckBox.setChecked(flags & re.VERBOSE)
        self.localeCheckBox.setChecked(flags & re.LOCALE)
        self.unicodeCheckBox.setChecked(flags & re.UNICODE)

    def getFlags(self):
        flags = 0

        if self.ignorecaseCheckBox.isChecked():
            flags += re.IGNORECASE
        if self.multilineCheckBox.isChecked():
            flags += re.MULTILINE
        if self.dotallCheckBox.isChecked():
            flags += re.DOTALL
        if self.verboseCheckBox.isChecked():
            flags += re.VERBOSE
        if self.localeCheckBox.isChecked():
            flags += re.LOCALE
        if self.unicodeCheckBox.isChecked():
            flags += re.UNICODE

        return flags

    def _clear(self):
        self._clearResults()

        self.matchNumberSpinBox.setValue(1)
        self.regexMultiLineEdit.setPlainText('')
        self.stringMultiLineEdit.setPlainText('')
        self.setFlags(0)
        self.replaceTextEdit.setPlainText('')

    def _clearResults(self):
        self.groupTable.clearContents()
        self.groupTable.setRowCount(0)
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
            self.spacerLabel.hide()
            self.replaceLabel.hide()
            self.replaceNumberSpinBox.hide()
            self.replaceTextBrowser.clear()
            self.replaceTextBrowser.setDisabled(True)

    def _populateGroupTable(self):
        groups = self._rp.getGroups(self.matchNumberSpinBox.value() - 1)

        self.groupTable.setRowCount(len(groups))

        row = 0
        for t in groups:
            self.groupTable.setItem(row, 0, QTableWidgetItem(t[1]))
            self.groupTable.setItem(row, 1, QTableWidgetItem(t[2]))
            row += 1

    def _populateMatchTextbrowser(self):
        spans = []
        span = self._rp.getSpan(self.matchNumberSpinBox.value() - 1)
        if span:
            spans.append(span)
        self._populateText(spans, self.matchTextBrowser)

    def _populateMatchAllTextbrowser(self):
        spans = self._rp.getAllSpans()
        self._populateText(spans, self.matchAllTextBrowser)

    def _populateReplaceTextbrowser(self):

        statusValue, strings = self._rp.replace(self.replaceNumberSpinBox.value())

        if statusValue == MATCH_OK:
            self._colorizeStrings(strings, self.replaceTextBrowser)
        else:
            self.replaceTextBrowser.clear()
            self.updateStatus("Error in replace string: %s" % strings, statusValue, 5)

    def _populateCodeTextBrowser(self):
        self.codeTextBrowser.setPlainText(self._rp.getRegexCode())

    def _populateEmbeddedFlags(self):

        self.ignorecaseCheckBox.setEnabled(True)
        self.localeCheckBox.setEnabled(True)
        self.multilineCheckBox.setEnabled(True)
        self.dotallCheckBox.setEnabled(True)
        self.unicodeCheckBox.setEnabled(True)
        self.verboseCheckBox.setEnabled(True)

        flags = self._rp.getEmbeddedFlags()
        for flag in flags:
            if flag == 'i':
                self.ignorecaseCheckBox.setEnabled(False)
                self.ignorecaseCheckBox.setChecked(True)
            elif flag == 'L':
                self.localeCheckBox.setEnabled(False)
                self.localeCheckBox.setChecked(True)
            elif flag == 'm':
                self.multilineCheckBox.setEnabled(False)
                self.multilineCheckBox.setChecked(True)
            elif flag == 's':
                self.dotallCheckBox.setEnabled(False)
                self.dotallCheckBox.setChecked(True)
            elif flag == 'u':
                self.unicodeCheckBox.setEnabled(False)
                self.unicodeCheckBox.setChecked(True)
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

        colors = (QColor(Qt.black), QColor(Qt.blue))
        i = 0
        pos = widget.textCursor()
        for s in strings:
            widget.setTextColor(colors[i % 2])
            widget.insertPlainText(s)
            if i == cursorOffset:
                pos = widget.textCursor()
            i += 1

        widget.setTextCursor(pos)

    def closeEvent(self, ev):
        self.checkEditState(self.tr("&No, Just Exit Kang"))
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
        fn = QFileDialog.getOpenFileName(self, self.tr("Import File"), self.importFilename, "All (*)")

        if fn.isEmpty():
            self.updateStatus(self.tr("A file was not selected for import"), MATCH_NONE, 5)
            return

        filename = str(fn)

        try:
            fp = open(filename, 'r')
        except:
            msg = self.tr("Could not open file for reading: ") + filename
            self.updateStatus(msg, MATCH_NONE, 5)
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
        self.setFlags(0)
        self.editstate = STATE_UNEDITED

    def fileOpen(self):
        fn = QFileDialog.getOpenFileName(self,
                                         self.tr("Open Kang File"),
                                         self.filename,
                                         "*.kng\nAll (*)",
                                         )
        if not fn.isEmpty():
            filename = str(fn)
            self.openFile(filename)

    def fileSave(self):
        if not self.filename:
            self.fileSaveAs()
            return

        regexString = self.regexMultiLineEdit.toPlainText()
        matchString = self.stringMultiLineEdit.toPlainText()
        replaceString = self.replaceTextEdit.toPlainText()
        flags = self.getFlags()

        try:
            kngfile = KngFile(self.filename, regexString, matchString, replaceString, flags)
            kngfile.save()

            self.editstate = STATE_UNEDITED

            msg = '%s %s' % (self.filename,
                             self.tr("successfully saved"))
            self.updateStatus(msg, MATCH_NONE, 5)
            self.recentFiles.add(self.filename)
        except IOError as ex:
            msg = str(ex)
            self.updateStatus(msg, MATCH_NONE, 5)

    def fileSaveAs(self):
        fn = QFileDialog.getSaveFileName(self,
                                         self.tr("Save Kang File"),
                                         self.filename,
                                         "*.kng\nAll (*)"
                                         )
        filename = fn
        if not filename:
            self.updateStatus(self.tr("No file selected to save"), MATCH_NONE, 5)
            return
        filename = os.path.normcase(filename)

        basename = os.path.basename(filename)
        if basename.find('.') == -1:
            filename += '.kng'

        self.filename = filename
        self.fileSave()

    def fileRevert(self):
        if not self.filename:
            self.updateStatus(self.tr("There is no filename to revert"), MATCH_NONE, 5)
            return

        self.openFile(self.filename)

    def openFile(self, filename):
        self.checkEditState()

        try:
            self.filename = ''

            kngfile = KngFile(filename)
            kngfile.load()

            self._clear()

            self._rp.pause()
            self.regexMultiLineEdit.setPlainText(kngfile.regex)
            self.stringMultiLineEdit.setPlainText(kngfile.matchstring)
            self.setFlags(kngfile.flags)
            self.replaceTextEdit.setPlainText(kngfile.replace)

            self.filename = filename
            self.recentFiles.add(self.filename)

            self._rp.unpause()

            msg = '%s %s' % (filename, self.tr("loaded successfully"))
            self.updateStatus(msg, MATCH_NONE, 5)
            self.editstate = STATE_UNEDITED
            return True

        except IOError as ex:
            msg = str(ex)
            self.updateStatus(msg, MATCH_NONE, 5)
            self.recentFiles.remove(filename)
            return False

    def pasteSymbol(self, symbol):
        self.regexMultiLineEdit.insertPlainText(symbol)

    def checkEditState(self, noButtonStr=None):

        if not self.preferences.askSave:
            return

        if self.preferences.askSaveOnlyForNamedProjects and not self.filename:
            return

        if not noButtonStr:
            noButtonStr = self.tr("&No")

        if self.editstate == STATE_EDITED:
            message = self.tr("You have made changes. Would you like to save them before continuing")

            prompt = QMessageBox().warning(None,
                                         self.tr("Save changes?"),
                                         message,
                                         self.tr("&Yes, Save Changes"),
                                         noButtonStr)

            if prompt == 0:
                self.fileSave()
                if not self.filename:
                    self.checkEditState(noButtonStr)

    def pasteFromRegexLib(self, regexLibDict):
        self.filename = ''
        self.checkEditState()

        self.regexMultiLineEdit.setPlainText(regexLibDict.get('regex', ''))
        self.stringMultiLineEdit.setPlainText(regexLibDict.get('text', ''))
        self.replaceTextEdit.setPlainText(regexLibDict.get('replace', ''))

        try:
            # set the current page if applicable
            self.resultTabWidget.setCurrentPage(int(regexLibDict.get('tab', '')))
        except ValueError:
            pass
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
