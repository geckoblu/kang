import sys
import unittest

from PySide2.QtCore import QCoreApplication
from PySide2.QtWidgets import QApplication

# from kang.gui import preferencesDialog
# from kang.gui.tests.fakeparent import FakeParent
# from kang.modules import preferences


class TestPreferencesDialog(unittest.TestCase):

    def setUp(self):
        self.qApp = QCoreApplication.instance()
        if not self.qApp:
            self.qApp = QApplication(sys.argv)

    def testDialog(self):
        # TODO: Write a test for PreferencesDialog
        pass
        # arent = FakeParent()
        # prefs = preferences.Preferences()
        # form = preferencesDialog.PreferencesDialog(parent, prefs)
        # form.showPrefsDialog()
        # form.apply()
        # form.accept()
        # form.askSaveCheckboxToogled()
