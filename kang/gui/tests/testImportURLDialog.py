from PySide2.QtCore import QCoreApplication
from PySide2.QtGui import QApplication
from PySide2.QtTest import QTest
import sys
import unittest

from kang.gui import importURLDialog
from kang.gui.tests.fakemessagebox import FakeMessageBox
from kang.gui.tests.fakeparent import FakeParent


class TestImportURLDialog(unittest.TestCase):

    def setUp(self):
        self.qApp = QCoreApplication.instance()
        if not self.qApp:
            self.qApp = QApplication(sys.argv)

    def test_dialog(self):
        parent = FakeParent()
        dialog = importURLDialog.ImportURLDialog(parent, 'file://%s' % __file__)
        dialog.show()
        QTest.qWaitForWindowShown(dialog)
        dialog.importURL()

        qmessagebox = FakeMessageBox()
        importURLDialog.QMessageBox = qmessagebox
        dialog.URLTextEdit.setText('fake url')
        dialog.importURL()
        self.assertTrue(qmessagebox.informationCalled)
