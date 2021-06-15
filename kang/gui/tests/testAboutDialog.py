# pylint: disable=protected-access,missing-function-docstring

import sys
import unittest

from PySide2.QtCore import QCoreApplication
from PySide2.QtWidgets import QApplication
from PySide2.QtTest import QTest

from kang.gui import aboutDialog


class TestAboutDialog(unittest.TestCase):

    def setUp(self):
        self.qApp = QCoreApplication.instance()
        if not self.qApp:
            self.qApp = QApplication(sys.argv) # pragma: no cover - This line is executed only in single mode execution

    def testDialog(self):
        dialog = aboutDialog.AboutDialog(None)
        QTest.qWaitForWindowExposed(dialog)
