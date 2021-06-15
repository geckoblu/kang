# pylint: disable=protected-access

import sys
import unittest

from PySide2.QtCore import QCoreApplication
from PySide2.QtWidgets import QApplication

from kang.gui.regexLibraryWidget import RegexLibraryWidget


class TestRegexLibraryWidget(unittest.TestCase):

    def setUp(self):
        self.qApp = QCoreApplication.instance()
        if not self.qApp:
            self.qApp = QApplication(sys.argv)  # pragma: no cover - This line is executed only in single mode execution

    def testRegexLibraryWidget(self):
        widget = RegexLibraryWidget()

        # Just code coverage
        widget._emitEntry(FakeModelIndex())

        widget._currentItemChanged(widget._refTable.currentItem())


class FakeModelIndex:

    def row(self):
        return 0
