# pylint: disable=protected-access
import os
import shutil
import sys
import tempfile
import unittest

from PySide2.QtCore import QCoreApplication
from PySide2.QtWidgets import QApplication
from PySide2.QtTest import QTest

from kang.gui import mainWindow
from kang.gui.tests.fakeQFileDialog import FakeQFileDialog
from kang.gui.tests.fakeWebbrowser import FakeWebbrowser
from kang.gui.tests.fakedialog import FakeDialog
from kang.gui.tests.fakemessagebox import FakeMessageBox
from kang.modules import util


class TestMainWindow(unittest.TestCase):

    def setUp(self):
        self.qApp = QCoreApplication.instance()
        if not self.qApp:
            self.qApp = QApplication(sys.argv)
        # Set config directory
        self.dtmp = tempfile.mkdtemp()
        os.environ['XDG_CONFIG_HOME'] = self.dtmp
        cdir = util.getConfigDirectory()
        os.mkdir(cdir)

        self.filename1 = os.path.abspath(os.path.join(os.path.dirname(__file__), 'mwTest1.kng'))

        self.window = mainWindow.MainWindow()
        QTest.qWaitForWindowExposed(self.window)
        self.window.preferences.askSave = False

    def tearDown(self):
        self.window.close()

    # Test if the window shows when loading a file
    def test_window_with_filename(self):
        self.window.close()  # Do not use the standard window
        window = mainWindow.MainWindow()
        window.loadFile(self.filename1)
        # QTest.qWaitForWindowExposed(window)
        window.close()

    def test_checkForKangDir(self):
        self.window.close()  # Do not use the standard window

        mainWindow.NewUserDialog = FakeDialog
        mainWindow.QMessageBox = FakeMessageBox

        self.dtmp = tempfile.mkdtemp()
        os.environ['XDG_CONFIG_HOME'] = self.dtmp

        # here user configuration directory doesn't exist
        # checkForKangDir is called in the __init__ so it creates the directory
        window = mainWindow.MainWindow()
        QTest.qWaitForWindowExposed(window)

        # here the user configuration directory exists
        window.checkForKangDir()

        # here the creation of user configuration directory will fail
        os.environ['XDG_CONFIG_HOME'] = '/'
        window.checkForKangDir()

        os.environ['XDG_CONFIG_HOME'] = self.dtmp
        window.close()

    def test_pause(self):
        self.window.pause(True)  # pause
        self.window.pause(False)  # unpause

    def test_examine(self):
        self.window.regex = 'abc'
        self.window.examine(True)
        self.window.examine(False)

    def test_matchNumSlot(self):
        self.window.loadFile(self.filename1)
        self.window._matchNumberChanged()

    def test_replaceNumSlot(self):
        self.window.loadFile(self.filename1)
        self.window._replaceNumberChanged()

    def test_populateReplaceTextbrowser(self):
        self.window.replaceNumberSpinBox.setValue(0)

        self.window._regexProcessor.setMatchString('abcdabc')
        self.window._regexProcessor.setRegexString('b')
        self.window.replaceTextEdit.setText('x')
        # self.window._regexProcessor.setReplaceString('x')

        self.window._populateReplaceTextbrowser()
        self.assertEqual(self.window.replaceTextBrowser.toPlainText(), 'axcdaxc')

        self.window._regexProcessor.setReplaceString('\\')
        self.window._populateReplaceTextbrowser()
        self.assertEqual(self.window.replaceTextBrowser.toPlainText(), '')

    def test_populateEmbeddedFlags(self):
        self.window.ignorecaseCheckBox.setChecked(True)
        self.window.multilineCheckBox.setChecked(True)
        self.window.dotallCheckBox.setChecked(True)
        self.window.asciiCheckBox.setChecked(True)
        self.window.verboseCheckBox.setChecked(True)

        self.window._regexProcessor.setRegexString('(?iLmsux)')

        self.window._populateEmbeddedFlags()
        self.assertTrue(self.window.ignorecaseCheckBox.isChecked())
        self.assertFalse(self.window.ignorecaseCheckBox.isEnabled())
        self.assertTrue(self.window.multilineCheckBox.isChecked())
        self.assertFalse(self.window.multilineCheckBox.isEnabled())
        self.assertTrue(self.window.dotallCheckBox.isChecked())
        self.assertFalse(self.window.dotallCheckBox.isEnabled())
        self.assertTrue(self.window.asciiCheckBox.isChecked())
        self.assertFalse(self.window.asciiCheckBox.isEnabled())
        self.assertTrue(self.window.verboseCheckBox.isChecked())
        self.assertFalse(self.window.verboseCheckBox.isEnabled())

        self.window._regexProcessor.setRegexString('')

        self.window._populateEmbeddedFlags()
        self.assertTrue(self.window.ignorecaseCheckBox.isChecked())
        self.assertTrue(self.window.ignorecaseCheckBox.isEnabled())
        self.assertTrue(self.window.multilineCheckBox.isChecked())
        self.assertTrue(self.window.multilineCheckBox.isEnabled())
        self.assertTrue(self.window.dotallCheckBox.isChecked())
        self.assertTrue(self.window.dotallCheckBox.isEnabled())
        self.assertTrue(self.window.asciiCheckBox.isChecked())
        self.assertTrue(self.window.asciiCheckBox.isEnabled())
        self.assertTrue(self.window.verboseCheckBox.isChecked())
        self.assertTrue(self.window.verboseCheckBox.isEnabled())

    def test_fileNew(self):
        self.window.fileNew()

    def test_fileSave(self):
        self.window.filename = os.path.join(self.dtmp, 'filesave1.kngs')
        self.window.fileSave()

        # This is a not validi filename
        self.window.filename = os.path.join(self.dtmp, 'not/a_valid_filename')
        self.window.fileSave()

    def test_fileSaveAs(self):

        qfd = mainWindow.QFileDialog

        mainWindow.QFileDialog = FakeQFileDialog(None)
        self.window.fileSave()  # As filemname is empty this will call fileSaveAs

        dtmp = tempfile.mkdtemp()

        mainWindow.QFileDialog = FakeQFileDialog(filename=os.path.join(dtmp, 'test1'))
        self.window.fileSaveAs()

        shutil.rmtree(dtmp)

        mainWindow.QFileDialog = qfd

    def test_fileRevert(self):
        self.window.fileRevert()
        self.window.filename = self.filename1
        self.window.fileRevert()

    def test_importFile(self):

        qfd = mainWindow.QFileDialog

        mainWindow.QFileDialog = FakeQFileDialog(None)
        self.window.importFile()

        mainWindow.QFileDialog = FakeQFileDialog(filename='not_existent_file')
        self.window.importFile()

        ntf = tempfile.NamedTemporaryFile(mode='w')
        ntf.write('abcdef')
        ntf.flush()
        mainWindow.QFileDialog = FakeQFileDialog(filename=ntf.name)
        self.window.importFile()
        self.assertEqual(self.window.stringMultiLineEdit.toPlainText(), 'abcdef')

        mainWindow.QFileDialog = qfd

    def test_openFile(self):
        self.window.loadFile(self.filename1)

        self.window.loadFile('not_a_valid_filename')

    def test_fileOpen(self):

        # TODO check better the opening of the file (also for other methods)
        qfd = mainWindow.QFileDialog

        mainWindow.QFileDialog = FakeQFileDialog(filename=self.filename1)
        self.window.fileOpen()

        mainWindow.QFileDialog = qfd

    def test_processRegex(self):
        self.window.pause(True)
        self.window.stringMultiLineEdit.setPlainText('abcdabc')
        self.window.pause(False)  # unpause
        self.window.regexMultiLineEdit.setPlainText('e')
        self.window.regexMultiLineEdit.setPlainText('d')
        self.window.regexMultiLineEdit.setPlainText('b')
        self.window.regexMultiLineEdit.setPlainText('(b)')
        self.window.regexMultiLineEdit.setPlainText('(?P<g1>b)')
        self.window.replaceTextEdit.setPlainText('\\1')

        code1 = str(self.window.codeTextBrowser.toPlainText()).split('\n')
        code2 = self.window._regexProcessor.getRegexCode().split('\n')
        for i in range(0, min(len(code1), len(code2))):
            c1 = code1[i]
            c2 = code2[i]
            self.assertEqual(c1, c2)

    def test_actionsSlot(self):
        self.window.editCopy()
        self.window.editPaste()
        self.window.editCut()
        self.window.editUndo()
        self.window.editRedo()

        self.window.widgetMethod('xxx', True)

    def test_editPreferences(self):
        old = mainWindow.PreferencesDialog
        mainWindow.PreferencesDialog = FakeDialog

        self.window.editPreferences()

        mainWindow.PreferencesDialog = old

    def test_helpPythonRegex(self):
        wold = mainWindow.webbrowser
        fwb = FakeWebbrowser()
        mainWindow.webbrowser = fwb

        self.window.helpPythonRegex()
        fwb.assertIsWebUrl(self)

        mainWindow.webbrowser = wold

    def test_helpRegexLib(self):
        old = mainWindow.RegexLibraryWindow
        mainWindow.RegexLibraryWindow = FakeDialog

        self.window.helpRegexLib()

        mainWindow.RegexLibraryWindow = old

    def test_helpAbout(self):
        old = mainWindow.AboutDialog
        mainWindow.AboutDialog = FakeDialog

        self.window.helpAbout()

        mainWindow.AboutDialog = old

    def test_referenceGuide(self):
        old = mainWindow.RegexReferenceWindow
        mainWindow.RegexReferenceWindow = FakeDialog

        self.window.referenceGuide()

        mainWindow.RegexReferenceWindow = old

    def test_showReportBugDialog(self):
        old = mainWindow.ReportBugDialog
        mainWindow.ReportBugDialog = FakeDialog

        self.window.showReportBugDialog('msg')

        mainWindow.ReportBugDialog = old

    def test_signalException(self):
        old = mainWindow.ReportBugDialog
        mainWindow.ReportBugDialog = FakeDialog

        self.window.signalException('msg')

        mainWindow.ReportBugDialog = old

    def test_importURL(self):
        old = mainWindow.ImportURLDialog
        mainWindow.ImportURLDialog = FakeDialog

        self.window._importURL()

        mainWindow.ImportURLDialog = old

    def test_pasteFromRegexLib(self):

        d = {'regex': 'regex',
             'text': 'text',
             'replace': 'replace',
             'tab': '1'
            }

        self.window.pasteFromRegexLib(d)

        d['tab'] = 'tab'  # Not a numeric tab
        self.window.pasteFromRegexLib(d)

        del d['tab']  # tab not defined
        self.window.pasteFromRegexLib(d)

    def test_checkEditState(self):

        self.window.preferences.askSave = False
        self.window._checkModified()

        self.window.preferences.askSave = True
        self.window.preferences.askSaveOnlyForNamedProjects = True
        self.window._checkModified()

        self.window.preferences.askSave = True
        self.window.preferences.askSaveOnlyForNamedProjects = False
        self.window._checkModified()

        self.window.preferences.askSave = True
        self.window.preferences.askSaveOnlyForNamedProjects = False
        self.window._modified = True

        old = mainWindow.QMessageBox
        mainWindow.QMessageBox = FakeMessageBox
        self.window.filename = os.path.join(util.getConfigDirectory(), 't.kng')
        self.window._checkModified()
        mainWindow.QMessageBox = old

        # an unavoidable trick to reach the 100% code coverage
        self.window.filename = ''
        self.window._modified = True
        old = mainWindow.QMessageBox
        mainWindow.QMessageBox = FakeMessageBox
        fileSave = self.window.fileSave
        self.window.fileSave = lambda: None
        checkModified = self.window._checkModified
        self.window._checkModified = lambda: None
        checkModified()
        self.window._checkModified = checkModified
        self.window.fileSave = fileSave
        mainWindow.QMessageBox = old

        self.window.preferences.askSave = False

    def test_pasteSymbol(self):
        self.window.pasteSymbol('symbol')

    def test_populateText(self):
        self.window.stringMultiLineEdit.setPlainText('abcdabc')
        widget = FakeColorizeWidget()

        # No match
        self.window._regexProcessor.setRegexString('X')
        spans = self.window._regexProcessor.getAllSpans()
        self.window._populateText(spans, widget)
        self.assertEqual(widget.colorized, [])

        qColorNormal = self.window.normalTextColor
        qColorEvidence = self.window.highlightTextColor

        # One match in the middle
        self.window._regexProcessor.setRegexString('d')
        spans = self.window._regexProcessor.getAllSpans()
        self.window._populateText(spans, widget)
        # self.assertEqual(widget.colorized, "[]")
        self.assertEqual(widget.colorized, [(qColorNormal, 'abc'),
                                            (qColorEvidence, 'd'),
                                            (qColorNormal, 'abc')])

        # Two match in the middle
        self.window._regexProcessor.setRegexString('b')
        spans = self.window._regexProcessor.getAllSpans()
        self.window._populateText(spans, widget)
        self.assertEqual(widget.colorized, [(qColorNormal, 'a'),
                                            (qColorEvidence, 'b'),
                                            (qColorNormal, 'cda'),
                                            (qColorEvidence, 'b'),
                                            (qColorNormal, 'c')])

        # Match in the end
        self.window._regexProcessor.setRegexString('c')
        spans = self.window._regexProcessor.getAllSpans()
        self.window._populateText(spans, widget)
        self.assertEqual(widget.colorized, [(qColorNormal, 'ab'),
                                            (qColorEvidence, 'c'),
                                            (qColorNormal, 'dab'),
                                            (qColorEvidence, 'c'),
                                            (qColorNormal, '')])

        # Match in the start
        self.window._regexProcessor.setRegexString('a')
        spans = self.window._regexProcessor.getAllSpans()
        self.window._populateText(spans, widget)
        self.assertEqual(widget.colorized, [(qColorNormal, ''),
                                            (qColorEvidence, 'a'),
                                            (qColorNormal, 'bcd'),
                                            (qColorEvidence, 'a'),
                                            (qColorNormal, 'bc')])


class FakeColorizeWidget():

    def __init__(self):
        self._currentTextColor = None
        self._currentBackgroundColor = None
        self.colorized = []

    def clear(self):
        self._currentTextColor = None
        self._currentBackgroundColor = None
        self.colorized = []

    def textCursor(self):
        return 0

    def setTextColor(self, color):
        self._currentTextColor = color

    def setTextBackgroundColor(self, color):
        self._currentBackgroundColor = color

    def insertPlainText(self, text):
        self.colorized.append((self._currentTextColor, str(text)))

    def setTextCursor(self, pos):
        pass


if __name__ == "__main__":
    # unittest.main()

    suite = unittest.TestSuite()
    suite.addTest(TestMainWindow("test_populateReplaceTextbrowser"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
