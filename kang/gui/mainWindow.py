from PyQt4.QtCore import Qt, SIGNAL
from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import QFileDialog, QColor, QMessageBox, \
                        QPixmap, QPalette, QTableWidgetItem, QHeaderView, qApp
import os
import re
import signal
import types
import webbrowser

from kang import KANG_WEBSITE, PYTHON_RE_LIBRARY_URL
from kang.gui.aboutDialog import AboutDialog
from kang.gui.importURLDialog import ImportURLDialog
from kang.gui.mainWindowBA import MainWindowBA
from kang.gui.newUserDialog import NewUserDialog
from kang.gui.preferencesDialog import PreferencesDialog
from kang.gui.regexLibraryWindow import RegexLibraryWindow
from kang.gui.regexReferenceWindow import RegexReferenceWindow
from kang.gui.reportBugDialog import ReportBugDialog
from kang.gui.statusbar import StatusBar
from kang.images import getIcon
from kang.modules.kngfile import KngFile
from kang.modules.preferences import Preferences
from kang.modules.recentfiles import RecentFiles
from kang.modules.regexprocessor import RegexProcessor
from kang.modules.util import findFile, restoreWindowSettings, saveWindowSettings, \
    getConfigDirectory
import kang.modules.xpm as xpm


TIMEOUT = 3

# regex to find special flags which must begin at beginning of line
# or after some spaces
EMBEDDED_FLAGS = r'^ *\(\?(?P<flags>[iLmsux]*)\)'

RX_BACKREF = re.compile(r"""\\\d""")

STATE_UNEDITED = 0
STATE_EDITED = 1

GEO = 'kang_geometry'

# colors for normal & examination mode
QCOLOR_WHITE = QColor(Qt.white)  # normal
QCOLOR_LIGHTCYAN = QColor('#DDFFFF')  # examine

_ = lambda st: st  # No translation at the moment

# match status
MATCH_NONE = -1
MATCH_NA = 0
MATCH_OK = 1
MATCH_FAIL = 2
MATCH_PAUSED = 3
MATCH_EXAMINED = 4

MSG_NA = _("Enter a regular expression and a string to match against")
MSG_PAUSED = _("Kang regular expression processing is paused.  Click the pause icon to unpause")
MSG_FAIL = _("Pattern does not match")

MSG_MATCH_FOUND = _("Pattern matches (found 1 match)")
MSG_MATCHES_FOUND = _("Pattern matches (found %d matches)")

# Initialized in the __init__ method because QPixmap should be loaded in the main thread
STATUS_PIXMAPS_DICT = {}


##############################################################################
#
# The Kang class which defines the main functionality and user interaction
#
##############################################################################
class MainWindow(MainWindowBA):

    _signalException = pyqtSignal(str)

    def __init__(self, filename=''):
        MainWindowBA.__init__(self)

        # Initialized here because QPixmap should be loaded in the main thread
        STATUS_PIXMAPS_DICT[MATCH_NA] = QPixmap(xpm.yellowStatusIcon)
        STATUS_PIXMAPS_DICT[MATCH_OK] = QPixmap(xpm.greenStatusIcon)
        STATUS_PIXMAPS_DICT[MATCH_FAIL] = QPixmap(xpm.redStatusIcon)
        STATUS_PIXMAPS_DICT[MATCH_PAUSED] = QPixmap(xpm.pauseStatusIcon)

        self._rp = RegexProcessor()

        self.regex = ''
        self.regexSaved = ''
        self.matchstring = ''
        self.replace = ''
        self.flags = 0
        self.isPaused = False
        self.isExamined = False
        self.importFilename = ''
        self.filename = ''
        self.matchNum = 1  # matches are labeled 1..n
        self.replaceNum = 0  # replace all
        self.url = KANG_WEBSITE
        self.groupTuples = None
        self.editstate = STATE_UNEDITED

        self.embeddedFlagsObj = re.compile(EMBEDDED_FLAGS)
        self.embeddedFlags = ''
        self.regexEmbeddedFlagsRemoved = ''

        header = self.groupTable.horizontalHeader()
        header.setResizeMode(QHeaderView.Stretch)
        # header.setStretchLastSection(True)

        self.refWin = None
        self.regexlibwin = None

        self.setWindowIcon(getIcon('kang-icon'))

        self.statusbar = StatusBar(self)

        self.loadToolbarIcons()

        self.updateStatus(MSG_NA, MATCH_NA)
        self._clearResults()

        restoreWindowSettings(self, GEO)

        self.show()

        self.preferences = Preferences()
        self.recentFiles = RecentFiles(self, self.preferences.recentFilesNum)
        self.preferencesChanged()

        if filename and self.openFile(filename):
            qApp.processEvents()

        self._signalException.connect(self.showReportBugDialog)

        self.connect(self, SIGNAL('preferencesChanged()'), self.preferencesChanged)
        self.connect(self, SIGNAL('pasteSymbol(PyQt_PyObject)'), self.paste_symbol)
        self.connect(self, SIGNAL('urlImported(PyQt_PyObject, PyQt_PyObject)'), self.urlImported)
        self.connect(self, SIGNAL('pasteRegexLib(PyQt_PyObject)'), self.pasteFromRegexLib)

        if self.replace:
            self.show_replace_widgets()
        else:
            self.hide_replace_widgets()

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

        try:
            os.mkdir(kdir, 0o755)
        except:
            message = '%s: %s' % (self.tr('Failed to create'), kdir)
            QMessageBox().critical(self, self.tr('ERROR'), message, buttons=QMessageBox.Ok)

        newuserdialog = NewUserDialog(self)
        newuserdialog.show()

    def updateStatus(self, status_string, status_value, duration=0):
        pixmap = STATUS_PIXMAPS_DICT.get(status_value)

        self.statusbar.setMessage(status_string, duration, pixmap)

    def edited(self):
        # invoked whenever the user has edited something
        self.editstate = STATE_EDITED

    def setFlags(self, flags):
        # from the given integer value of flags, set the checkboxes
        # this is used when loading a saved file
        self.ignorecaseCheckBox.setChecked(flags & re.IGNORECASE)
        self.multilineCheckBox.setChecked(flags & re.MULTILINE)
        self.dotallCheckBox.setChecked(flags & re.DOTALL)
        self.verboseCheckBox.setChecked(flags & re.VERBOSE)
        self.localeCheckBox.setChecked(flags & re.LOCALE)
        self.unicodeCheckBox.setChecked(flags & re.UNICODE)

    def _getFlagsStr(self):
        flagsStr = ''

        if self.ignorecaseCheckBox.isChecked():
            flagsStr += '| re.IGNORECASE '

        if self.multilineCheckBox.isChecked():
            flagsStr += '| re.MULTILINE '

        if self.dotallCheckBox.isChecked():
            flagsStr += '| re.DOTALL '

        if self.verboseCheckBox.isChecked():
            flagsStr += '| re.VERBOSE '

        if self.localeCheckBox.isChecked():
            flagsStr += '| re.LOCALE '

        if self.unicodeCheckBox.isChecked():
            flagsStr += '| re.UNICODE'

        if flagsStr:
            flagsStr = ', ' + flagsStr[1:]
        return flagsStr

    def getEmbeddedFlagsStr(self):
        flagsStr = flags = ''

        if self.ignorecaseCheckBox.isChecked():
            flags += 'i'

        if self.multilineCheckBox.isChecked():
            flags += 'm'

        if self.dotallCheckBox.isChecked():
            flags += 's'

        if self.verboseCheckBox.isChecked():
            flags += 'x'

        if self.localeCheckBox.isChecked():
            flags += 'L'

        if self.unicodeCheckBox.isChecked():
            flags += 'u'

        if flags:
            flagsStr = '(?' + flags + ')'

        return flagsStr

    def pause(self):
        self.isPaused = not self.isPaused

        if self.isPaused:
            self.updateStatus(MSG_PAUSED, MATCH_PAUSED)
            self.matchNumberSpinBox.setDisabled(1)

        else:
            self._processRegex()
            self.matchNumberSpinBox.setEnabled(1)

    def examine(self):
        self.isExamined = not self.isExamined

        if self.isExamined:
            color = QCOLOR_LIGHTCYAN
            regex = self.regex
            self.regexSaved = self.regex
            length = len(regex)
            self.regexMultiLineEdit.setReadOnly(True)
            self.stringMultiLineEdit.setReadOnly(True)
            self.replaceTextEdit.setReadOnly(True)
            for i in range(length, 0, -1):
                regex = regex[:i]
                self._processEmbeddedFlags()
                try:
                    m = re.search(regex, self.matchstring, self.flags)
                    if m:
                        self.__refresh_regex_widget(color, regex)
                        return
                except:
                    pass

            self.__refresh_regex_widget(color, '')
        else:
            regex = self.regexSaved
            color = QCOLOR_WHITE
            self.regexMultiLineEdit.setReadOnly(False)
            self.stringMultiLineEdit.setReadOnly(False)
            self.replaceTextEdit.setReadOnly(False)
            self.__refresh_regex_widget(color, regex)

    def __refresh_regex_widget(self, base_qcolor, regex):
        p = self.regexMultiLineEdit.palette()
        p.setColor(QPalette.Base, base_qcolor)
        self.regexMultiLineEdit.setPalette(p)

        self.regexMultiLineEdit.blockSignals(1)
        self.regexMultiLineEdit.clear()
        self.regexMultiLineEdit.blockSignals(0)
        self.regexMultiLineEdit.setPlainText(regex)

    def matchNumSlot(self, num):
        self.matchNum = num
        self._processRegex()

    def replaceNumSlot(self, num):
        self.replaceNum = num
        self._processRegex()

    def regexChangedSlot(self):
        try:
            regexString = str(self.regexMultiLineEdit.toPlainText())
        except UnicodeError:
            regexString = unicode(self.regexMultiLineEdit.toPlainText())
        self.regex = regexString
        self._rp.setRegexString(regexString)
        self._processRegex()

    def stringChangedSlot(self):
        try:
            matchString = str(self.stringMultiLineEdit.toPlainText())
        except UnicodeError:
            matchString = unicode(self.stringMultiLineEdit.toPlainText())
        self.matchstring = matchString
        self._rp.setMatchString(matchString)
        self._processRegex()

    def replaceChangedSlot(self):
        try:
            replaceString = str(self.replaceTextEdit.toPlainText())
        except UnicodeError:
            replaceString = unicode(self.replaceTextEdit.toPlainText())

        self.replace = replaceString
        self._rp.setReplaceString(replaceString)
        self._processRegex()
        if not self.replace:
            self.hide_replace_widgets()
        else:
            self.show_replace_widgets()

    def checkboxSlot(self):
        self.flags = 0

        if self.ignorecaseCheckBox.isChecked():
            self.flags = self.flags + re.IGNORECASE

        if self.multilineCheckBox.isChecked():
            self.flags = self.flags + re.MULTILINE

        if self.dotallCheckBox.isChecked():
            self.flags = self.flags + re.DOTALL

        if self.verboseCheckBox.isChecked():
            self.flags = self.flags + re.VERBOSE

        if self.localeCheckBox.isChecked():
            self.flags = self.flags + re.LOCALE

        if self.unicodeCheckBox.isChecked():
            self.flags = self.flags + re.UNICODE

        self._processRegex()

    def hide_replace_widgets(self):
        self.spacerLabel.hide()
        self.replaceLabel.hide()
        self.replaceNumberSpinBox.hide()
        self.replaceTextBrowser.clear()
        self.replaceTextBrowser.setDisabled(True)

    def show_replace_widgets(self):
        self.spacerLabel.show()
        self.replaceLabel.show()
        self.replaceNumberSpinBox.show()
        self.replaceNumberSpinBox.setEnabled(True)
        self.replaceTextBrowser.setEnabled(True)

    def _populateGroupTable(self, tuples):
        self.groupTable.setRowCount(len(tuples))

        row = 0
        for t in tuples:
            self.groupTable.setItem(row, 0, QTableWidgetItem(unicode(t[1])))
            self.groupTable.setItem(row, 1, QTableWidgetItem(unicode(t[2])))
            row += 1

    def _populateCodeTextbrowser(self):
        self.codeTextBrowser.setPlainText('')

        code = 'import re\n\n'
        code += '# common variables\n\n'
        code += 'rawstr = r"""' + self.regexEmbeddedFlagsRemoved + '"""\n'
        code += 'embedded_rawstr = r"""' + self.getEmbeddedFlagsStr() + \
                self.regexEmbeddedFlagsRemoved + '"""\n'
        code += 'matchstr = \"\"\"' + self.matchstring + '\"\"\"'
        code += '\n\n'
        code += '# method 1: using a compile object\n'
        code += 'compile_obj = re.compile(rawstr'
        code += self._getFlagsStr()
        code += ')\n'
        code += 'match_obj = compile_obj.search(matchstr)\n\n'

        code += '# method 2: using search function (w/ external flags)\n'
        code += 'match_obj = re.search(rawstr, matchstr'
        code += self._getFlagsStr()
        code += ')\n\n'

        code += '# method 3: using search function (w/ embedded flags)\n'
        code += 'match_obj = re.search(embedded_rawstr, matchstr)\n\n'

        if self.groupTuples:
            code += '# Retrieve group(s) from match_obj\n'
            code += 'all_groups = match_obj.groups()\n\n'
            code += '# Retrieve group(s) by index\n'
            i = 0
            named_grps = 0
            for grp in self.groupTuples:
                i += 1
                code += 'group_%d = match_obj.group(%d)\n' % (i, i)
                if grp[1]:
                    named_grps = 1

            if named_grps:
                code += '\n# Retrieve group(s) by name\n'
                for grp in self.groupTuples:
                    if grp[1]:
                        code += '%s = match_obj.group("%s")\n' % (grp[1], grp[1])

            code += '\n'

        if self.replace:
            code += '# Replace string\n'
            code += 'newstr = compile_obj.subn("%s", matchstr)\n' % self.replace

        self.codeTextBrowser.setPlainText(code)

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

    def _populateMatchTextbrowser(self, startpos, endpos):
        pre = post = ''

        match = self.matchstring[startpos:endpos]

        # prepend the beginning that didn't match
        if startpos > 0:
            pre = self.matchstring[0:startpos]

        # append the end that didn't match
        if endpos < len(self.matchstring):
            post = self.matchstring[endpos:]

        strings = [pre, match, post]
        self._colorizeStrings(strings, self.matchTextBrowser, 1)

    def _populateReplaceTextbrowser(self, spans, nummatches, compile_obj):
        self.replaceTextBrowser.clear()
        if not spans:
            return

        num = self.replaceNumberSpinBox.value()
        if num == 0:
            num = nummatches
        text = self.matchstring

        replace_text = unicode(self.replaceTextEdit.toPlainText())
        if RX_BACKREF.search(replace_text):
            # if the replace string contains a backref we just use the
            # python regex methods for the substitution
            replaced = compile_obj.subn(replace_text, text, num)[0]
            self.replaceTextBrowser.setPlainText(replaced)
            return

        numreplaced = idx = 0

        strings = []

        for span in spans:
            if span[0] != 0:
                s = text[idx:span[0]]
            else:
                s = ''

            idx = span[1]
            numreplaced += 1

            strings.append(s)
            strings.append(self.replace)

            if numreplaced >= num:
                strings.append(text[span[1]:])
                break

        self._colorizeStrings(strings, self.replaceTextBrowser)

    def _populateMatchAllTextbrowser(self, spans):
        self.matchAllTextBrowser.clear()
        if not spans:
            return

        idx = 0
        text = self.matchstring
        strings = []
        for span in spans:
            if span[0] != 0:
                s = text[idx:span[0]]
            else:
                s = ''

            idx = span[1]
            strings.append(s)
            strings.append(text[span[0]:span[1]])

        if 0 <= idx <= len(text):
            strings.append(text[span[1]:])

        self._colorizeStrings(strings, self.matchAllTextBrowser)

    def _clearResults(self):
        self.groupTable.clearContents()
        self.groupTable.setRowCount(0)
        self.codeTextBrowser.setPlainText('')
        self.matchTextBrowser.setPlainText('')
        self.matchNumberSpinBox.setEnabled(False)
        self.replaceNumberSpinBox.setEnabled(False)
        self.replaceTextBrowser.setPlainText('')
        self.matchAllTextBrowser.setPlainText('')

    def _processRegex(self):
        def timeout(signum, frame):
            return

        if self.isPaused:
            return

        self._processEmbeddedFlags()

        if not self.regex or not self.matchstring:
            self.updateStatus(MSG_NA, MATCH_NA)
            self._clearResults()
            return

        signal.signal(signal.SIGALRM, timeout)
        signal.alarm(TIMEOUT)

        try:
            compile_obj = re.compile(self.regex, self.flags)
            allmatches = compile_obj.findall(self.matchstring)

            if allmatches and len(allmatches):
                self.matchNumberSpinBox.setMaximum(len(allmatches))
                self.matchNumberSpinBox.setEnabled(True)
                self.replaceNumberSpinBox.setMaximum(len(allmatches))
                self.replaceNumberSpinBox.setEnabled(True)
            else:
                self.matchNumberSpinBox.setEnabled(False)
                self.replaceNumberSpinBox.setEnabled(False)

            match_obj = compile_obj.search(self.matchstring)

        except Exception as ex:
            self.updateStatus(str(ex), MATCH_FAIL)
            return

        signal.alarm(0)

        if not match_obj:
            self.updateStatus(MSG_FAIL, MATCH_FAIL)

            self._clearResults()
            return

        # matchIndex is the list element for matchNum.
        # Therefor matchNum is for ui display
        # and matchIndex is for application logic.
        matchIndex = self.matchNum - 1

        if matchIndex > 0:
            for i in range(matchIndex):
                match_obj = compile_obj.search(self.matchstring,
                                               match_obj.end())

        self._populateMatchTextbrowser(match_obj.start(), match_obj.end())

        self.groupTuples = []

        if match_obj.groups():
            # print match_obj.groups()
            s = '<font color=blue>'
            num_groups = len(match_obj.groups())

            group_nums = {}
            if compile_obj.groupindex:
                keys = compile_obj.groupindex.keys()
                for key in keys:
                    group_nums[compile_obj.groupindex[key]] = key

            # create group_tuple in the form: (group #, group name, group matches)
            g = allmatches[matchIndex]
            if type(g) == types.TupleType:
                for i in range(len(g)):
                    group_tuple = (i + 1, group_nums.get(i + 1, ''), g[i])
                    self.groupTuples.append(group_tuple)
            else:
                self.groupTuples.append((1, group_nums.get(1, ''), g))

        self._populateGroupTable(self.groupTuples)

        if len(allmatches) == 1:
            status = MSG_MATCH_FOUND
        else:
            status = MSG_MATCHES_FOUND % len(allmatches)
        self.updateStatus(status, MATCH_OK)

        self._populateCodeTextbrowser()

        spans = self._findAllSpans(compile_obj)
        if self.replace:
            self._populateReplaceTextbrowser(spans, len(allmatches), compile_obj)

        self._populateMatchAllTextbrowser(spans)

    def _findAllSpans(self, compile_obj):
        spans = []

        match_obj = compile_obj.search(self.matchstring)

        last_span = None

        while match_obj:
            start = match_obj.start()
            end = match_obj.end()
            span = (start, end)
            if last_span == span:
                break

            spans.append(span)

            last_span = span
            match_obj = compile_obj.search(self.matchstring, end)

        return spans

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
            return None

        filename = str(fn)

        try:
            fp = open(filename, 'r')
        except:
            msg = self.tr("Could not open file for reading: ") + filename
            self.updateStatus(msg, MATCH_NONE, 5)
            return None

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

        try:
            kngfile = KngFile(self.filename, self.regex, self.matchstring, self.replace, self.flags)
            kngfile.save()

            self.editstate = STATE_UNEDITED

            msg = '%s %s' % (unicode(self.filename),
                             unicode(self.tr("successfully saved")))
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
        filename = unicode(fn)
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

            self.isPaused = True

            self.matchNumberSpinBox.setValue(1)
            self.regexMultiLineEdit.setPlainText(kngfile.regex)
            self.stringMultiLineEdit.setPlainText(kngfile.matchstring)
            self.setFlags(kngfile.flags)
            self.replaceTextEdit.setPlainText(kngfile.replace)

            self.filename = filename
            self.recentFiles.add(self.filename)

            self.isPaused = False
            self._processRegex()

            msg = '%s %s' % (filename, unicode(self.tr("loaded successfully")))
            self.updateStatus(msg, MATCH_NONE, 5)
            self.editstate = STATE_UNEDITED
            return True

        except IOError as ex:
            msg = str(ex)
            self.updateStatus(msg, MATCH_NONE, 5)
            self.recentFiles.remove(filename)
            return False

    def paste_symbol(self, symbol):
        self.regexMultiLineEdit.insertPlainText(symbol)

    def _processEmbeddedFlags(self):
        # determine if the regex contains embedded regex flags.
        # if not, return 0 -- inidicating that the regex has no embedded flags
        # if it does, set the appropriate checkboxes on the UI to reflect the flags that are embedded
        #   and return 1 to indicate that the string has embedded flags

        self.ignorecaseCheckBox.setEnabled(True)
        self.ignorecaseCheckBox.setEnabled(True)
        self.localeCheckBox.setEnabled(True)
        self.multilineCheckBox.setEnabled(True)
        self.dotallCheckBox.setEnabled(True)
        self.unicodeCheckBox.setEnabled(True)
        self.verboseCheckBox.setEnabled(True)

        match = self.embeddedFlagsObj.match(self.regex)
        if not match:
            self.embeddedFlags = ''
            self.regexEmbeddedFlagsRemoved = self.regex
            return 0

        self.embeddedFlags = match.group('flags')
        self.regexEmbeddedFlagsRemoved = self.embeddedFlagsObj.sub('', self.regex, 1)

        for flag in self.embeddedFlags:
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

        return 1

    def checkEditState(self, noButtonStr=None):

        if not self.preferences.askSave:
            return

        if self.preferences.askSaveOnlyForNamedProjects and not self.filename:
            return

        if not noButtonStr:
            noButtonStr = self.tr("&No")

        if self.editstate == STATE_EDITED:
            message = self.tr("You have made changes. Would you like to save them before continuing")

            prompt = QMessageBox.warning(None,
                                         self.tr("Save changes?"),
                                         message,
                                         self.tr("&Yes, Save Changes"),
                                         noButtonStr)

            if prompt == 0:
                self.fileSave()
                if not self.filename:
                    self.checkEditState(noButtonStr)

    def pasteFromRegexLib(self, d):
        self.filename = ''
        self.checkEditState()

        self.regexMultiLineEdit.setPlainText(d.get('regex'))
        self.stringMultiLineEdit.setPlainText(d.get('text'))
        self.replaceTextEdit.setPlainText(d.get('replace'))

        try:
            # set the current page if applicable
            self.resultTabWidget.setCurrentPage(int(d['tab']))
        except:
            pass
        self.editstate = STATE_UNEDITED

    def widgetMethod(self, methodstr, anywidget=0):
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
