from PyQt5 import QtGui
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QApplication
from PyQt5.QtTest import QTest
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
        clipboard = QtGui.QApplication.clipboard()
        self.assertEqual(msg, clipboard.text())
