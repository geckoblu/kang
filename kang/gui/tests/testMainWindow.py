from PyQt4.QtCore import QCoreApplication
from PyQt4.QtGui import QApplication
import os
import sys
import tempfile
import unittest

from kang.gui import mainWindow
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
        self.window.preferences.askSave = False

    def tearDown(self):
        self.window.close()

    def test_window(self):
        window = mainWindow.MainWindow(self.filename1)
        window.close()

    def test_checkForKangDir(self):
        # Set config directory
        self.dtmp = tempfile.mkdtemp()
        os.environ['XDG_CONFIG_HOME'] = self.dtmp

        # checkForKangDir is called in the __init__ so it creates the directory
        window = mainWindow.MainWindow()
        window.preferences.askSave = False
        # here the user configuration directory exists
        window.checkForKangDir()
        window.close()

    def test_openFile(self):
        self.window.openFile(self.filename1)

    def test_flags(self):
        flags = self.window.getFlagsStr()
        self.assertEqual(flags, '')
        self.window.setFlags(126)
        flags = self.window.getFlagsStr()
        self.assertEqual(flags, ',  re.IGNORECASE| re.MULTILINE| re.DOTALL| re.VERBOSE| re.LOCALE| re.UNICODE')
        self.window.setFlags(0)
        flags = self.window.getFlagsStr()
        self.assertEqual(flags, '')

    def test_pause(self):
        self.window.pause()  # pause
        self.window.pause()  # unpause

    def test_examine(self):
        self.window.regex = 'abc'
        self.window.examine()
        self.window.examine()

    def tests_matchNumSlot(self):
        self.window.openFile(self.filename1)
        self.window.matchNumSlot(1)

    def tests_replaceNumSlot(self):
        self.window.openFile(self.filename1)
        self.window.replaceNumSlot(1)

    def test_fileNew(self):
        self.window.fileNew()

    def test_fileSave(self):
        self.window.filename = os.path.join(self.dtmp, 'filesave1.kngs')
        self.window.fileSave()

    def test_fileRevert(self):
        self.window.fileRevert()
        self.window.filename = self.filename1
        self.window.fileRevert()
