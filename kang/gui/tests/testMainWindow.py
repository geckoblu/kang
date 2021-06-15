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
from kang.modules import util
from kang.gui.importURLDialog import ImportURLDialogMode
from kang.gui.tests.fakeQFileDialog import FakeQFileDialog
from kang.gui.tests.fakeWebbrowser import FakeWebbrowser
from kang.gui.tests import fakedialog
from kang.gui.tests import fakemessagebox
from kang.gui.tests.fakedialog import FakeDialog
from kang.gui.tests.fakemessagebox import FakeMessageBox


class TestMainWindow(unittest.TestCase):

    def setUp(self):
        self.qApp = QCoreApplication.instance()
        if not self.qApp:
            self.qApp = QApplication(sys.argv)  # pragma: no cover - This line is executed only in single mode execution
        # Set config directory
        self.dtmp = tempfile.mkdtemp()
        os.environ['XDG_CONFIG_HOME'] = self.dtmp
        cdir = util.getConfigDirectory()
        os.mkdir(cdir)

        self.filename1 = os.path.abspath(os.path.join(os.path.dirname(__file__), 'mwTest1.kng'))

        self.window = mainWindow.MainWindow()
        QTest.qWaitForWindowExposed(self.window)
        self.window._preferences.askSave = False

    def tearDown(self):
        self.window.close()

    # Test if the window shows when loading a file
    def testWindowWithFilename(self):
        self.window.close()  # Do not use the standard window
        window = mainWindow.MainWindow()
        window.loadFile(self.filename1)
        # QTest.qWaitForWindowExposed(window)
        window.close()

    def testCheckForKangDir(self):
        self.window.close()  # Do not use the standard window

        mainWindow.NewUserDialog = FakeDialog
        mainWindow.QMessageBox = FakeMessageBox

        self.dtmp = tempfile.mkdtemp()
        os.environ['XDG_CONFIG_HOME'] = self.dtmp

        # here user configuration directory doesn't exist
        # _checkForKangDir is called in the __init__ so it creates the directory
        window = mainWindow.MainWindow()
        QTest.qWaitForWindowExposed(window)

        # here the user configuration directory exists
        window._checkForKangDir()

        # here the creation of user configuration directory will fail
        os.environ['XDG_CONFIG_HOME'] = '/'
        window._checkForKangDir()

        os.environ['XDG_CONFIG_HOME'] = self.dtmp
        window.close()

    def testPause(self):
        self.window._pause(True)  # _pause
        self.window._pause(False)  # unpause

    def testExamine(self):
        self.window.regex = 'abc'
        self.window._examine(True)
        self.window._examine(False)

    def testMatchNumSlot(self):
        self.window.loadFile(self.filename1)
        self.window._matchNumberChanged()

    def testReplaceNumSlot(self):
        self.window.loadFile(self.filename1)
        self.window._replaceNumberChanged()
        self.window._matchNumberSpinBox.setValue(1)

    def testPopulateReplaceTextbrowser(self):
        self.window._replaceNumberSpinBox.setValue(0)

        self.window._regexProcessor.setMatchString('abcdabc')
        self.window._regexProcessor.setRegexString('b')
        self.window._replaceTextEdit.setText('x')
        # self.window._regexProcessor.setReplaceString('x')

        self.window._populateReplaceTextbrowser()
        self.assertEqual(self.window._replaceTextBrowser.toPlainText(), 'axcdaxc')

        self.window._regexProcessor.setReplaceString('\\')
        self.window._populateReplaceTextbrowser()
        self.assertEqual(self.window._replaceTextBrowser.toPlainText(), '')

    def testPopulateEmbeddedFlags(self):
        self.window._regexProcessor.setRegexString('(?imsax)')

        self.window._populateEmbeddedFlags()
        self.assertFalse(self.window._ignorecaseCheckBox.isEnabled())
        self.assertFalse(self.window._multilineCheckBox.isEnabled())
        self.assertFalse(self.window._dotallCheckBox.isEnabled())
        self.assertFalse(self.window._verboseCheckBox.isEnabled())
        self.assertFalse(self.window._asciiCheckBox.isEnabled())

        self.window._regexProcessor.setRegexString('')

        self.window._populateEmbeddedFlags()
        self.assertTrue(self.window._ignorecaseCheckBox.isEnabled())
        self.assertTrue(self.window._multilineCheckBox.isEnabled())
        self.assertTrue(self.window._dotallCheckBox.isEnabled())
        self.assertTrue(self.window._verboseCheckBox.isEnabled())
        self.assertTrue(self.window._asciiCheckBox.isEnabled())

        self.window._regexProcessor.setRegexString('(?Lu)')

    def testFileNew(self):
        self.window._fileNew()

    def testFileExit(self):
        self.window._fileExit()

    def testFileSave(self):
        self.window._filename = os.path.join(self.dtmp, 'filesave1.kngs')
        self.window._fileSave()

        # This is a not validi _filename
        self.window._filename = os.path.join(self.dtmp, 'not/a_valid_filename')
        self.window._fileSave()

    def testFileSaveAs(self):

        qfd = mainWindow.QFileDialog

        mainWindow.QFileDialog = FakeQFileDialog(None)
        self.window._fileSave()  # As filemname is empty this will call _fileSaveAs

        dtmp = tempfile.mkdtemp()

        mainWindow.QFileDialog = FakeQFileDialog(filename=os.path.join(dtmp, 'test1'))
        self.window._fileSaveAs()

        shutil.rmtree(dtmp)

        mainWindow.QFileDialog = qfd

    def testFileRevert(self):
        self.window._fileRevert()
        self.window._filename = self.filename1
        self.window._fileRevert()

    def testImportFile(self):

        qfd = mainWindow.QFileDialog

        mainWindow.QFileDialog = FakeQFileDialog(None)
        self.window._importFile()

        mainWindow.QFileDialog = FakeQFileDialog(filename='not_existent_file')
        self.window._importFile()

        ntf = tempfile.NamedTemporaryFile(mode='w')
        ntf.write('abcdef')
        ntf.flush()
        mainWindow.QFileDialog = FakeQFileDialog(filename=ntf.name)
        self.window._importFile()
        self.assertEqual(self.window._stringMultiLineEdit.toPlainText(), 'abcdef')

        mainWindow.QFileDialog = qfd

    def testOpenFile(self):
        self.window.loadFile(self.filename1)

        self.window.loadFile('not_a_valid_filename')

    def testFileOpen(self):

        # TODO check better the opening of the file (also for other methods)
        qfd = mainWindow.QFileDialog

        mainWindow.QFileDialog = FakeQFileDialog(filename=self.filename1)
        self.window._fileOpen()

        mainWindow.QFileDialog = qfd

    def testProcessRegex(self):
        self.window._pause(True)
        self.window._stringMultiLineEdit.setPlainText('abcdabc')
        self.window._pause(False)  # unpause
        self.window._regexMultiLineEdit.setPlainText('e')
        self.window._regexMultiLineEdit.setPlainText('d')
        self.window._regexMultiLineEdit.setPlainText('b')
        self.window._regexMultiLineEdit.setPlainText('(b)')
        self.window._regexMultiLineEdit.setPlainText('(?P<g1>b)')
        self.window._replaceTextEdit.setPlainText('\\1')

        code1 = str(self.window._codeTextBrowser.toPlainText()).split('\n')
        code2 = self.window._regexProcessor.getRegexCode().split('\n')
        for i in range(0, min(len(code1), len(code2))):
            c1 = code1[i]
            c2 = code2[i]
            self.assertEqual(c1, c2)

    def testActionsSlot(self):
        self.window._editCopy()
        self.window._editPaste()
        self.window._editCut()
        self.window._editUndo()
        self.window._editRedo()

        self.window._widgetMethod('xxx', True)

    def testEditPreferences(self):
        old = mainWindow.PreferencesDialog
        mainWindow.PreferencesDialog = FakeDialog

        self.window._editPreferences()

        mainWindow.PreferencesDialog = old

    def testHelpPythonRegex(self):
        wold = mainWindow.webbrowser
        fwb = FakeWebbrowser()
        mainWindow.webbrowser = fwb

        self.window._helpPythonRegex()
        fwb.assertIsWebUrl(self)

        mainWindow.webbrowser = wold

    # def test_helpRegexLib(self):
    #    old = mainWindow.RegexLibraryWindow
    #    mainWindow.RegexLibraryWindow = FakeDialog
    #
    #    self.window.helpRegexLibrary()
    #
    #    mainWindow.RegexLibraryWindow = old

    def testHelpAbout(self):
        old = mainWindow.AboutDialog
        mainWindow.AboutDialog = FakeDialog

        self.window._helpAbout()

        mainWindow.AboutDialog = old

    # def test_referenceGuide(self):
    #    old = mainWindow.RegexReferenceWindow
    #    mainWindow.RegexReferenceWindow = FakeDialog
    #
    #    self.window.helpRegexReferenceGuide()
    #
    #    mainWindow.RegexReferenceWindow = old

    def testShowReportBugDialog(self):
        old = mainWindow.ReportBugDialog
        mainWindow.ReportBugDialog = FakeDialog

        self.window._showReportBugDialog('msg')

        mainWindow.ReportBugDialog = old

    def testSignalException(self):
        old = mainWindow.ReportBugDialog
        mainWindow.ReportBugDialog = FakeDialog

        self.window._signalException('msg')

        mainWindow.ReportBugDialog = old

    def testImportURL(self):
        old = mainWindow.ImportURLDialog
        mainWindow.ImportURLDialog = FakeDialog

        self.window._importURL()

        fakedialog._IMPORTURLDIALOGMODE = ImportURLDialogMode.HTML

        self.window._importURL()

        mainWindow.ImportURLDialog = old

    def testPasteFromRegexLib(self):

        libraryEntry = {'regex': 'regex',
                        'text': 'text',
                        'replace': 'replace',
                        'tab': '1'
                        }

        self.window._pasteFromRegexLibrary(libraryEntry)

        libraryEntry['tab'] = 'tab'  # Not a numeric tab
        self.window._pasteFromRegexLibrary(libraryEntry)

        del libraryEntry['tab']  # tab not defined
        self.window._pasteFromRegexLibrary(libraryEntry)

    def testCheckEditState(self):

        self.window._preferences.askSave = False
        self.window._checkModified()

        self.window._preferences.askSave = True
        self.window._preferences.askSaveOnlyForNamedProjects = True
        self.window._checkModified()

        self.window._preferences.askSave = True
        self.window._preferences.askSaveOnlyForNamedProjects = False
        self.window._checkModified()

        self.window._preferences.askSave = True
        self.window._preferences.askSaveOnlyForNamedProjects = False
        self.window._modified = True

        self.window._filename = os.path.join(util.getConfigDirectory(), 't.kng')
        old = mainWindow.QMessageBox
        mainWindow.QMessageBox = FakeMessageBox
        fakemessagebox._ANSWER = FakeMessageBox.Yes
        self.window._checkModified()
        mainWindow.QMessageBox = old

        self.window._preferences.askSave = False

    def testPasteSymbol(self):
        self.window._pasteSymbol('symbol')

    def testPopulateText(self):
        self.window._stringMultiLineEdit.setPlainText('abcdabc')
        widget = FakeColorizeWidget()

        # No match
        self.window._regexProcessor.setRegexString('X')
        spans = self.window._regexProcessor.getAllSpans()
        self.window._populateText(spans, widget)
        self.assertEqual(widget.colorized, [])

        qColorNormal = self.window._normalTextColor
        qColorEvidence = self.window._highlightTextColor

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

    def testShowRegexReferenceGuide(self):
        self.window._helpRegexReferenceGuide(False)
        self.window._helpRegexReferenceGuide(True)

    def testShowRegexLibrary(self):
        self.window._helpRegexLibrary(False)
        self.window._helpRegexLibrary(True)


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

# if __name__ == "__main__":
#    # unittest.main()
#
#    suite = unittest.TestSuite()
#    suite.addTest(TestMainWindow("testPopulateReplaceTextbrowser"))
#    runner = unittest.TextTestRunner()
#    runner.run(suite)
