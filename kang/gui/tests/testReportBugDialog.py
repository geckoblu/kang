from PyQt4.QtCore import QCoreApplication
from PyQt4.QtGui import QApplication
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
        form = reportBugDialog.ReportBugDialog(parent, 'Error message')
