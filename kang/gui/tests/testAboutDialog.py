from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QApplication
from PyQt5.QtTest import QTest
import sys
import unittest

from kang.gui import aboutDialog
from kang.gui.tests.fakeparent import FakeParent


class TestAboutDialog(unittest.TestCase):

    def setUp(self):
        self.qApp = QCoreApplication.instance()
        if not self.qApp:
            self.qApp = QApplication(sys.argv)

    def test_dialog(self):
        parent = FakeParent()
        dialog = aboutDialog.AboutDialog(parent)
        QTest.qWaitForWindowShown(dialog)
