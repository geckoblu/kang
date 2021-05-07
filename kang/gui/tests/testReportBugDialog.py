from PySide2 import QtGui
from PySide2.QtCore import QCoreApplication
from PySide2.QtGui import QApplication
from PySide2.QtTest import QTest
import sys
import unittest

from kang.gui import reportBugDialog
from kang.gui.tests.fakeparent import FakeParent


class TestReportBugDialog(unittest.TestCase):

    def setUp(self):
        self.qApp = QCoreApplication.instance()
        if not self.qApp:
            self.qApp = QApplication(sys.argv)

    def test_dialog(self):
        parent = FakeParent()

        msg = 'Error message'
        dialog = reportBugDialog.ReportBugDialog(parent, msg)
        dialog.show()
        QTest.qWaitForWindowShown(dialog)

        dialog.copyToClipboard()
        dialog.close()
        clipboard = QApplication.clipboard()
        self.assertEqual(msg, clipboard.text())
