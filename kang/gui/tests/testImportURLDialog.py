import sys
import unittest

from PySide2.QtCore import QCoreApplication
from PySide2.QtWidgets import QApplication

# from kang.gui import importURLDialog
# from kang.gui.tests.fakemessagebox import FakeMessageBox
# from kang.gui.tests.fakeparent import FakeParent


class TestImportURLDialog(unittest.TestCase):

    def setUp(self):
        self.qApp = QCoreApplication.instance()
        if not self.qApp:
            self.qApp = QApplication(sys.argv)

    def testDialog(self):
        # TODO: Write a test for IportURLDialog
        pass
        # parent = FakeParent()
        # dialog = importURLDialog.ImportURLDialog(parent, 'file://%s' % __file__)
        # dialog.getURL()
        # QTest.qWaitForWindowExposed(dialog)
        # #dialog._lastImportedURL()
        #
        # qmessagebox = FakeMessageBox()
        # importURLDialog.QMessageBox = qmessagebox
        # dialog.URLTextEdit.setText('fake url')
        # dialog._lastImportedURL()
        # self.assertTrue(qmessagebox.informationCalled)
