from PySide2.QtCore import QCoreApplication
from PySide2.QtGui import QApplication
from PySide2.QtTest import QTest
import os
import sys
import tempfile
import unittest

from kang.gui import regexLibraryWindow
from kang.gui.tests.fakeparent import FakeParent
from kang.modules import util


class TestRegexLibraryWindow(unittest.TestCase):

    def setUp(self):
        self.qApp = QCoreApplication.instance()
        if not self.qApp:
            self.qApp = QApplication(sys.argv)

        # Set config directory
        dtmp = tempfile.mkdtemp()
        os.environ['XDG_CONFIG_HOME'] = dtmp
        cdir = util.getConfigDirectory()
        if not os.path.exists(cdir):
            os.mkdir(cdir)

    def test_window(self):
        parent = FakeParent()
        window = regexLibraryWindow.RegexLibraryWindow(parent)
        window.show()
        QTest.qWaitForWindowShown(window)

        window.descSelectedSlot(None)

        window.descSelectedSlot('just something')

        window.editPaste()

        window.close()
