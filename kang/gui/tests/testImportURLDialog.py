# pylint: disable=protected-access

import sys
import unittest

from PySide2.QtCore import QCoreApplication
from PySide2.QtWidgets import QApplication
from PySide2.QtTest import QTest

from kang.gui import importURLDialog
from kang.gui.tests.fakemessagebox import FakeMessageBox

class TestImportURLDialog(unittest.TestCase):

    def setUp(self):
        self.qApp = QCoreApplication.instance()
        if not self.qApp:
            self.qApp = QApplication(sys.argv)

    def testDialog(self):
        localURL = 'file://%s' % __file__
        dialog = importURLDialog.ImportURLDialog(None, localURL)
        QTest.qWaitForWindowExposed(dialog)

        # Avoid modal input
        dialog.exec = lambda: True
        dialog._importURL()

        (ok, text, url, mode) = dialog.getURL()

        self.assertEqual(ok, True)
        self.assertEqual(url, localURL)
        self.assertEqual(mode, importURLDialog.ImportURLDialogMode.TEXT)
        self.assertEqual(text[0:34], '# pylint: disable=protected-access')

    def testDialogException(self):
        importURLDialog.QMessageBox = FakeMessageBox
        
        localURL = 'fake url'
        dialog = importURLDialog.ImportURLDialog(None, localURL)
        QTest.qWaitForWindowExposed(dialog)

        # Avoid modal input
        dialog.exec = lambda: True
        dialog._importURL()

        dialog.getURL()
