from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QApplication
from PyQt5.QtTest import QTest
import os
import sys
import tempfile
import unittest

from kang.gui import regexReferenceWindow
from kang.gui.tests.fakeparent import FakeParent
from kang.modules import util


class TestRegexReferenceWindow(unittest.TestCase):

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
        window = regexReferenceWindow.RegexReferenceWindow(parent)
        window.show()
        QTest.qWaitForWindowShown(window)

        item = window.referenceTreeWidget.topLevelItem(0)
        window.referenceTreeWidget.setItemSelected(item, True)
        window.editPaste()

        window.close()
