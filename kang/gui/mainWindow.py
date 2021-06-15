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

_SHORTMESSAGE_DURATION = 3  # seconds

tr = lambda msg: msg


##############################################################################
#
# The Kang class which defines the main functionality and user interaction
#
##############################################################################
class MainWindow(MainWindowUI):

    _exceptionSignal = Signal(str)

    def __init__(self):
        MainWindowUI.__init__(self)

        # Holds whether the document shown in the window has unsaved changes
        self._modified = False

        # Stores the path of the opened kng file (if any)
        self._filename = ''

        # Holds the status (visible or not) of the Regex Reference Guide Panel
        self._showRegexReferenceGuide = False

        # Holds the status (visible or not) of the Regex Reference Library Panel
        self._showRegexLibrary = False

        # Temporary stores the current regex (when in '_examine'mode)
        self._regexStringSaved = ''

        # Temporary stores last imported File
        self._lastImportedFilename = ''

        # Temporary stores last opened URL
        self._lastImportedURL = ''

        self._updateStatus(MSG_NA, MATCH_NA)
        self._clearResults()

        windowSettings = WindowSettings()
        windowSettings.restore(self)

        self.show()

        self._preferences = Preferences()
        self._preferences.load()
        self._recentFiles = RecentFiles(self, self._preferences.recentFilesNum)

        self._exceptionSignal.connect(self._showReportBugDialog)
        self._regexReferencePanel._pasteSymbol.connect(self._pasteSymbol)
        self._regexLibraryPanel.emitEntry.connect(self._pasteFromRegexLibrary)

        self._checkForKangDir()

    def _checkForKangDir(self):
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
        self._updateStatus(statusMessage, statusValue)

        allmatches = self._regexProcessor.getAllSpans()
        if allmatches:
            self._matchTextBrowser.setEnabled(True)
            self._groupTable.setEnabled(True)
            self._matchNumberSpinBox.setMaximum(len(allmatches))
            self._matchNumberSpinBox.setEnabled(True)
        else:
            # No match found
            self._matchTextBrowser.setDisabled(True)
            self._groupTable.setDisabled(True)
            self._matchNumberSpinBox.setValue(0)
            self._matchNumberSpinBox.setDisabled(True)

        replaceString = self._replaceTextEdit.toPlainText()
        if allmatches and replaceString:
            self._replaceTextBrowser.setEnabled(True)
            self._replaceNumberSpinBox.setMaximum(len(allmatches))
            self._replaceNumberSpinBox.setEnabled(True)
        else:
            # No match found
            self._replaceTextBrowser.setDisabled(True)
            self._replaceNumberSpinBox.setValue(0)
            self._replaceNumberSpinBox.setDisabled(True)

        self._populateGroupTable()
        self._populateMatchTextbrowser()
        self._populateReplaceTextbrowser()
        self._populateCodeTextBrowser()
        self._populateEmbeddedFlags()

    def _updateStatus(self, statusString, statusValue, duration=0):
        if duration > 0:
            self.statusBar().showMessage(statusString, duration * 1000)
        else:
            self.statusBar().clearMessage()
            self.statusBar().showPermanentMessage(statusString)

    def _setModified(self):
        # invoked whenever the user has _modified something
        self._modified = True

    def _pause(self, paused):
        if paused:
            self._regexProcessor.pause()
            self._updateStatus(MSG_PAUSED, MATCH_PAUSED)
            self._matchTextBrowser.setDisabled(True)
            self._matchTextBrowser.setPlainText('')
            self._groupTable.setDisabled(True)
            self._groupTable.clear()
            self._replaceTextBrowser.setDisabled(True)
            self._replaceTextBrowser.setPlainText('')
            self._codeTextBrowser.setDisabled(True)
            self._codeTextBrowser.setPlainText('')
            self._matchNumberSpinBox.setEnabled(False)
            self._replaceNumberSpinBox.setEnabled(False)
        else:
            self._matchTextBrowser.setEnabled(True)
            self._groupTable.setEnabled(True)
            self._replaceTextBrowser.setEnabled(True)
            self._codeTextBrowser.setEnabled(True)
            self._matchNumberSpinBox.setEnabled(True)
            self._replaceNumberSpinBox.setEnabled(True)
            self._regexProcessor.unpause()

    def _examine(self, examine):
        if examine:
            self._regexStringSaved = self._regexMultiLineEdit.toPlainText()

            self._stringMultiLineEdit.setReadOnly(True)
            self._regexMultiLineEdit.setReadOnly(True)
            self._replaceTextEdit.setReadOnly(True)
            self._stringMultiLineEdit.setEnabled(False)
            self._regexMultiLineEdit.setEnabled(False)
            self._replaceTextEdit.setEnabled(False)
            self._stringMultiLineEdit.setTextColor(self._normalTextColor)
            self._stringMultiLineEdit.setText(self._stringMultiLineEdit.toPlainText())
            self._replaceTextEdit.setTextColor(self._normalTextColor)
            self._replaceTextEdit.setText(self._replaceTextEdit.toPlainText())

            matching, dontmatching = self._regexProcessor.examine()
            self._refreshRegexWidget(matching, dontmatching)
        else:
            self._regexMultiLineEdit.setReadOnly(False)
            self._stringMultiLineEdit.setReadOnly(False)
            self._replaceTextEdit.setReadOnly(False)
            self._stringMultiLineEdit.setEnabled(True)
            self._regexMultiLineEdit.setEnabled(True)
            self._replaceTextEdit.setEnabled(True)
            self._regexMultiLineEdit.setTextColor(self._normalTextColor)

            self._regexMultiLineEdit.setPlainText(self._regexStringSaved)

    def _refreshRegexWidget(self, matching, dontmatching):
        self._regexMultiLineEdit.clear()

        self._regexMultiLineEdit.blockSignals(True)
        self._regexMultiLineEdit.insertPlainText(matching)
        self._regexMultiLineEdit.setTextColor(self._disabledTextColor)
        self._regexMultiLineEdit.insertPlainText(dontmatching)
        self._regexMultiLineEdit.blockSignals(False)

        self._regexProcessor.setRegexString(matching)

    def _matchNumberChanged(self):
        self._populateGroupTable()
        self._populateMatchTextbrowser()

    def _replaceNumberChanged(self):
        self._populateReplaceTextbrowser()

    def _clear(self):
        self._clearResults()

        self._matchNumberSpinBox.setValue(0)
        self._regexMultiLineEdit.setPlainText('')
        self._stringMultiLineEdit.setPlainText('')
        self._replaceTextEdit.setPlainText('')

        self._ignorecaseCheckBox.setChecked(False)
        self._multilineCheckBox.setChecked(False)
        self._dotallCheckBox.setChecked(False)
        self._verboseCheckBox.setChecked(False)
        self._asciiCheckBox.setChecked(False)

    def _clearResults(self):
        self._groupTable.clear()
        self._codeTextBrowser.setPlainText('')
        self._matchTextBrowser.setPlainText('')
        self._matchNumberSpinBox.setEnabled(False)
        self._replaceNumberSpinBox.setEnabled(False)
        self._replaceTextBrowser.setPlainText('')

    def _populateGroupTable(self):
        groups = self._regexProcessor.getAllGroups()

        self._groupTable.clear()

        for matchNumber, group in enumerate(groups, start=1):
            # print(matchNumber, group)

            child = None
            for subGroup in group:
                if not child:
                    child = QTreeWidgetItem(self._groupTable)
                    child.setText(0, str(matchNumber))
                    item = child
                else:
                    subchild = QTreeWidgetItem()
                    child.addChild(subchild)
                    item = subchild

                item.setText(1, str(subGroup[0]))
                item.setText(2, subGroup[1])
                item.setText(3, subGroup[2])

        self._groupTable.expandAll()
        for column in range(0, self._groupTable.columnCount()):
            self._groupTable.resizeColumnToContents(column)

        model = self._groupTable.model()
        selectionModel = self._groupTable.selectionModel()

        evidenceMatchNumber = self._matchNumberSpinBox.value()

        if evidenceMatchNumber > 0:
            row = evidenceMatchNumber - 1
            index = model.index(row, 0)
            selectionModel.select(index, QItemSelectionModel.Select | QItemSelectionModel.Rows)
            for i in range(0, model.rowCount(index)):
                childIndex = model.index(i, 0, index)
                selectionModel.select(childIndex, QItemSelectionModel.Select | QItemSelectionModel.Rows)

    def _populateMatchTextbrowser(self):
        matchNumber = self._matchNumberSpinBox.value()
        if matchNumber > 0:
            spans = [self._regexProcessor.getSpan(matchNumber - 1)]
        else:
            spans = self._regexProcessor.getAllSpans()
        self._populateText(spans, self._matchTextBrowser)

    def _populateReplaceTextbrowser(self):
        replaceString = self._replaceTextEdit.toPlainText()
        allmatches = self._regexProcessor.getAllSpans()

        if replaceString and allmatches:
            statusValue, strings = self._regexProcessor.replace(self._replaceNumberSpinBox.value())

            if statusValue == MATCH_OK:
                self._colorizeStrings(strings, self._replaceTextBrowser)
            else:
                self._replaceTextBrowser.clear()
                self._updateStatus("Error in replace string: %s" % strings, statusValue, _SHORTMESSAGE_DURATION)
        else:
            self._replaceTextBrowser.clear()

    def _populateCodeTextBrowser(self):
        self._codeTextBrowser.setPlainText(self._regexProcessor.getRegexCode())

    def _populateEmbeddedFlags(self):

        self._ignorecaseCheckBox.setEnabled(True)
        self._multilineCheckBox.setEnabled(True)
        self._dotallCheckBox.setEnabled(True)
        self._asciiCheckBox.setEnabled(True)
        self._verboseCheckBox.setEnabled(True)

        flags = self._regexProcessor.getEmbeddedFlags()
        for flag in flags:
            if flag == 'i':
                self._ignorecaseCheckBox.setEnabled(False)
                # self._ignorecaseCheckBox.setChecked(True)
            elif flag == 'm':
                self._multilineCheckBox.setEnabled(False)
                # self._multilineCheckBox.setChecked(True)
            elif flag == 's':
                self._dotallCheckBox.setEnabled(False)
                # self._dotallCheckBox.setChecked(True)
            elif flag == 'a':
                self._asciiCheckBox.setEnabled(False)
                # self._asciiCheckBox.setChecked(True)
            elif flag == 'x':
                self._verboseCheckBox.setEnabled(False)
                # self._verboseCheckBox.setChecked(True)
            elif flag == 'L':
                self._updateStatus(self.tr("Locale Flag not supported"), MATCH_NONE, _SHORTMESSAGE_DURATION)
            elif flag == 'u':
                self._updateStatus(self.tr("Unicode Flag not supported"), MATCH_NONE, _SHORTMESSAGE_DURATION)

    def _populateText(self, spans, widget):
        widget.clear()

        if not spans:
            return

        idx = 0
        text = self._stringMultiLineEdit.toPlainText()
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

        textColors = [self._normalTextColor, self._highlightTextColor]
        foregroundColors = [self._normalForegroundColor, self._highlightForegroundColor]

        widget.setTextColor(self._normalTextColor)

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

    def _fileExit(self):
        self.close()

    def closeEvent(self, event):
        """This event handler is called with the given event when Qt receives a window close request."""
        self._checkModified()

        settings = WindowSettings()
        settings.save(self)

        event.accept()

    def _importURL(self):
        dialog = ImportURLDialog(self, self._lastImportedURL)
        (ok, text, url, mode) = dialog.getURL()
        if ok:
            self._lastImportedURL = url
            if mode == ImportURLDialogMode.HTML:
                self._stringMultiLineEdit.setHtml(text)
                text = self._stringMultiLineEdit.toPlainText()
                self._stringMultiLineEdit.setPlainText(text)
            else:
                self._stringMultiLineEdit.setPlainText(text)

    def _importFile(self):
        (filename, _filter) = QFileDialog.getOpenFileName(self,
                                                          self.tr("Import File"),
                                                          self._lastImportedFilename, "All (*)")

        if not filename:
            self._updateStatus(self.tr("A file was not selected for import"), MATCH_NONE, _SHORTMESSAGE_DURATION)
            return

        try:
            fp = open(filename, 'r')
        except:
            msg = self.tr("Could not open file for reading: ") + filename
            self._updateStatus(msg, MATCH_NONE, _SHORTMESSAGE_DURATION)
            return

        self._lastImportedFilename = filename
        data = fp.read()
        fp.close()
        self._stringMultiLineEdit.setPlainText(data)

    def _fileNew(self):
        self._checkModified()
        self._filename = ''

        self._regexMultiLineEdit.setPlainText('')
        self._stringMultiLineEdit.setPlainText('')
        self._replaceTextEdit.setPlainText('')

        self._ignorecaseCheckBox.setChecked(False)
        self._multilineCheckBox.setChecked(False)
        self._dotallCheckBox.setChecked(False)
        self._verboseCheckBox.setChecked(False)
        self._asciiCheckBox.setChecked(False)

        self._modified = False

    def _fileOpen(self):
        (filename, _filter) = QFileDialog.getOpenFileName(self,
                                                          self.tr("Open Kang File"),
                                                          self._filename,
                                                          "*.kng\nAll (*)",
                                                          )
        if filename:
            self.loadFile(filename)

    def _fileSave(self):
        if not self._filename:
            self._fileSaveAs()
            return

        regexString = self._regexMultiLineEdit.toPlainText()
        matchString = self._stringMultiLineEdit.toPlainText()
        replaceString = self._replaceTextEdit.toPlainText()

        try:
            kngfile = KngFile(self._filename,
                              matchString,
                              regexString,
                              replaceString,
                              self._ignorecaseCheckBox.isChecked(),
                              self._multilineCheckBox.isChecked(),
                              self._dotallCheckBox.isChecked(),
                              self._verboseCheckBox.isChecked(),
                              self._asciiCheckBox.isChecked()
                              )
            kngfile.save()

            self._modified = False

            basename = os.path.basename(self._filename)
            msg = '%s %s' % (basename, self.tr("successfully saved"))
            self._updateStatus(msg, MATCH_NONE, _SHORTMESSAGE_DURATION)
            self._recentFiles.add(self._filename)
        except IOError as ex:
            msg = str(ex)
            self._updateStatus(msg, MATCH_NONE, _SHORTMESSAGE_DURATION)

    def _fileSaveAs(self):
        (filename, _filter) = QFileDialog.getSaveFileName(self,
                                                          self.tr("Save Kang File"),
                                                          self._filename,
                                                          "*.kng\nAll (*)"
                                                          )
        if not filename:
            self._updateStatus(self.tr("No file selected to save"), MATCH_NONE, _SHORTMESSAGE_DURATION)
            return
        filename = os.path.normcase(filename)

        basename = os.path.basename(filename)
        if basename.find('.') == -1:
            filename += '.kng'

        self._filename = filename
        self._fileSave()

    def _fileRevert(self):
        if not self._filename:
            self._updateStatus(self.tr("There is no _filename to revert"), MATCH_NONE, _SHORTMESSAGE_DURATION)
            return

        self.loadFile(self._filename)

    def loadFile(self, filename):
        """Loads a kng file"""

        self._checkModified()

        try:
            self._filename = ''

            kngfile = KngFile(filename)
            kngfile.load()

            self._clear()

            self._regexProcessor.pause()

            self._regexMultiLineEdit.setPlainText(kngfile.regexString)
            self._stringMultiLineEdit.setPlainText(kngfile.matchString)
            self._replaceTextEdit.setPlainText(kngfile.replaceString)

            self._ignorecaseCheckBox.setChecked(kngfile.flagIgnorecase)
            self._multilineCheckBox.setChecked(kngfile.flagMultiline)
            self._dotallCheckBox.setChecked(kngfile.flagDotall)
            self._verboseCheckBox.setChecked(kngfile.flagVerbose)
            self._asciiCheckBox.setChecked(kngfile.flagAscii)

            self._filename = filename
            self._recentFiles.add(self._filename)

            # Reset Pause and Examine status
            self._editPauseAction.setChecked(False)
            self._pause(False)
            self._editExamineAction.setChecked(False)
            self._regexStringSaved = kngfile.regexString
            self._examine(False)
            self._regexProcessor.unpause()

            basename = os.path.basename(filename)
            msg = '%s %s' % (basename, self.tr("loaded successfully"))
            self._updateStatus(msg, MATCH_NONE, _SHORTMESSAGE_DURATION)
            self._modified = False

            return True

        except IOError as ex:
            msg = str(ex)
            self._updateStatus(msg, MATCH_NONE, _SHORTMESSAGE_DURATION)
            self._recentFiles.remove(filename)
            return False

    def _pasteSymbol(self, symbol):
        self._regexMultiLineEdit.insertPlainText(symbol)

    def _checkModified(self):

        if not self._preferences.askSave:
            return

        if self._preferences.askSaveOnlyForNamedProjects and not self._filename:
            return

        if self._modified:
            message = self.tr("You have made changes. Would you like to save them before continuing?")

            prompt = QMessageBox().warning(self,
                                           self.tr("Save changes?"),
                                           message,
                                           QMessageBox.No,
                                           QMessageBox.Yes)

            if prompt == QMessageBox.Yes:
                self._fileSave()
                if not self._filename:
                    self._checkModified()  # pragma: no cover - Unusual, quite impossible to test

    def _pasteFromRegexLibrary(self, libraryEntry):
        self._checkModified()

        self._filename = ''

        self._regexMultiLineEdit.setPlainText(libraryEntry.get('regex', ''))
        self._stringMultiLineEdit.setPlainText(libraryEntry.get('match', ''))
        self._replaceTextEdit.setPlainText(libraryEntry.get('replace', ''))

        try:
            # set the current page if applicable
            self._resultTabWidget.setCurrentIndex(int(libraryEntry.get('tab', 0)))
        except ValueError:
            pass  # Ignore the error

        self._modified = False

    def _widgetMethod(self, methodstr, anywidget=False):
        # execute the methodstr of widget only if widget
        # is one of the editable widgets OR if the method
        # may be applied to any widget.
        widget = qApp.focusWidget()
        if anywidget or widget in (self._regexMultiLineEdit,
                                   self._stringMultiLineEdit,
                                   self._replaceTextEdit,
                                   self._codeTextBrowser):
            try:
                eval('widget.%s' % methodstr)
            except:
                pass

    def _editUndo(self):
        self._widgetMethod('undo()')

    def _editRedo(self):
        self._widgetMethod('redo()')

    def _editCopy(self):
        self._widgetMethod('copy()', 1)

    def _editCut(self):
        self._widgetMethod('cut()')

    def _editPaste(self):
        self._widgetMethod('paste()')

    def _editPreferences(self):
        dialog = PreferencesDialog(self, self._preferences)
        (ok, preferences) = dialog.getPreferences()
        if ok:
            self._preferences = preferences
            self._recentFiles.setNumShown(self._preferences.recentFilesNum)
            self._preferences.save()

    def _helpPythonRegex(self):
        webbrowser.open(PYTHON_RE_LIBRARY_URL)

    def _helpRegexReferenceGuide(self, showRegexReferenceGuide):
        self._showRegexReferenceGuide = showRegexReferenceGuide

        if showRegexReferenceGuide:
            index = self._splitterTabWidget.insertTab(0, self._regexReferencePanel, tr("Regex Reference Guide"))
            self._splitterTabWidget.setCurrentIndex(index)
        else:
            index = self._splitterTabWidget.indexOf(self._regexReferencePanel)
            self._splitterTabWidget.removeTab(index)

        self._splitterTabWidget.setVisible(self._showRegexReferenceGuide or self._showRegexLibrary)

    def _helpRegexLibrary(self, showRegexLibrary):
        self._showRegexLibrary = showRegexLibrary

        if showRegexLibrary:
            index = self._splitterTabWidget.insertTab(1, self._regexLibraryPanel, tr("Regex Library"))
            self._splitterTabWidget.setCurrentIndex(index)
        else:
            index = self._splitterTabWidget.indexOf(self._regexLibraryPanel)
            self._splitterTabWidget.removeTab(index)

        self._splitterTabWidget.setVisible(self._showRegexReferenceGuide or self._showRegexLibrary)

    def _helpAbout(self):
        aboutWindow = AboutDialog(self)
        aboutWindow.show()

    def _signalException(self, msg):
        self._exceptionSignal.emit(msg)

    def _showReportBugDialog(self, msg):
        rbd = ReportBugDialog(self, msg)
        rbd.exec_()
