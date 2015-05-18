from PyQt4.QtCore import QCoreApplication
from PyQt4.QtGui import QApplication
import sys
import unittest

from kang.gui import importURLDialog
from kang.gui.tests.fakeparent import FakeParent


class TestImportURLDialog(unittest.TestCase):

    def setUp(self):
        self.qApp = QCoreApplication.instance()
        if not self.qApp:
            self.qApp = QApplication(sys.argv)

    def test_dialog(self):
        parent = FakeParent()
        form = importURLDialog.ImportURLDialog(parent, "fake.url")

