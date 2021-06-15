# pylint: disable=protected-access,missing-function-docstring

import sys
import unittest

from PySide2.QtCore import QCoreApplication
from PySide2.QtWidgets import QApplication

from kang.gui.regexReferenceWidget import RegexReferenceWidget


class TestRegexReferenceWidget(unittest.TestCase):

    def setUp(self):
        self.qApp = QCoreApplication.instance()
        if not self.qApp:
            self.qApp = QApplication(sys.argv)  # pragma: no cover - This line is executed only in single mode execution

    def testRegexReferenceWidget(self):
        widget = RegexReferenceWidget()

        # Just code coverage
        widget._emitSymbol(FakeModelIndex())


class FakeModelIndex:

    def row(self):
        return 0
