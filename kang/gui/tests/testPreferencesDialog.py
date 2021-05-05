from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QApplication
import sys
import unittest

from kang.gui import preferencesDialog
from kang.gui.tests.fakeparent import FakeParent
from kang.modules import preferences


class TestPreferencesDialog(unittest.TestCase):

    def setUp(self):
        self.qApp = QCoreApplication.instance()
        if not self.qApp:
            self.qApp = QApplication(sys.argv)

    def test_dialog(self):
        parent = FakeParent()
        prefs = preferences.Preferences()
        form = preferencesDialog.PreferencesDialog(parent, prefs)
        form.showPrefsDialog()
        form.apply()
        form.accept()
        form.askSaveCheckboxToogled()
