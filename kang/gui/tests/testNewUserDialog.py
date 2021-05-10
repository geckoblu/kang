import sys
import unittest

from PySide2.QtCore import QCoreApplication
from PySide2.QtWidgets import QApplication
from PySide2.QtTest import QTest

from kang.gui import newUserDialog
from kang.gui.tests.fakeparent import FakeParent


class TestNewUserDialog(unittest.TestCase):

    def setUp(self):
        self.qApp = QCoreApplication.instance()
        if not self.qApp:
            self.qApp = QApplication(sys.argv)

    def test_dialog(self):
        parent = FakeParent()
        dialog = newUserDialog.NewUserDialog(parent)
        QTest.qWaitForWindowExposed(dialog)
