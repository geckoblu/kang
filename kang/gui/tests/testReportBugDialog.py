# pylint: disable=protected-access

import sys
import unittest

from PySide2.QtCore import QCoreApplication
from PySide2.QtWidgets import QApplication
from PySide2.QtTest import QTest

from kang.gui import reportBugDialog


class TestReportBugDialog(unittest.TestCase):

    def setUp(self):
        self.qApp = QCoreApplication.instance()
        if not self.qApp:
            self.qApp = QApplication(sys.argv)

    def testDialog(self):
        msg = 'Error message'
        dialog = reportBugDialog.ReportBugDialog(None, msg)
        dialog.show()
        QTest.qWaitForWindowExposed(dialog)

        dialog._copyToClipboard()
        dialog.close()
        clipboard = QApplication.clipboard()
        self.assertEqual(msg, clipboard.text())
