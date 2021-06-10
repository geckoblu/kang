# pylint: disable=protected-access

import sys
import unittest

from PySide2.QtCore import QCoreApplication
from PySide2.QtWidgets import QApplication
from PySide2.QtTest import QTest

from kang.gui import newUserDialog


class TestNewUserDialog(unittest.TestCase):

    def setUp(self):
        self.qApp = QCoreApplication.instance()
        if not self.qApp:
            self.qApp = QApplication(sys.argv)

    def testDialog(self):
        dialog = newUserDialog.NewUserDialog(None)
        QTest.qWaitForWindowExposed(dialog)
