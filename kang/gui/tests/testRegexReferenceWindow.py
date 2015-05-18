from PyQt4.QtCore import QCoreApplication
from PyQt4.QtGui import QApplication
import sys
import unittest

from kang.gui import regexReferenceWindow
from kang.gui.tests.fakeparent import FakeParent


class TestRegexReferenceWindow(unittest.TestCase):

    def setUp(self):
        self.qApp = QCoreApplication.instance()
        if not self.qApp:
            self.qApp = QApplication(sys.argv)

    def test_window(self):
        parent = FakeParent()
        window = regexReferenceWindow.RegexReferenceWindow(parent)

