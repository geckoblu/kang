# pylint: disable=protected-access,missing-function-docstring

import sys
import unittest

from PySide2.QtCore import QCoreApplication
from PySide2.QtWidgets import QApplication

from kang.gui import preferencesDialog
# from kang.gui.tests.fakeparent import FakeParent
from kang.modules import preferences


class TestPreferencesDialog(unittest.TestCase):

    def setUp(self):
        self.qApp = QCoreApplication.instance()
        if not self.qApp:
            self.qApp = QApplication(sys.argv) # pragma: no cover - This line is executed only in single mode execution

    def testDialog(self):
        # arent = FakeParent()
        prefs = preferences.Preferences()
        dialog = preferencesDialog.PreferencesDialog(None, prefs)

        # Avoid modal input
        dialog.exec = lambda: True

        (ok, prefs2) = dialog.getPreferences()

        self.assertEqual(ok, False)
        self.assertEqual(prefs2, prefs)
