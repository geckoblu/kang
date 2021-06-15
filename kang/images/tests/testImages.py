# pylint: disable=protected-access,missing-function-docstring

import sys
import unittest

from PySide2.QtCore import QCoreApplication
from PySide2.QtWidgets import QApplication

from kang import images


class TestImages(unittest.TestCase):

    def setUp(self):
        self.qApp = QCoreApplication.instance()
        if not self.qApp:
            self.qApp = QApplication(sys.argv) # pragma: no cover - This line is executed only in single mode execution

    def testGetPixmap(self):
        ibug = images.getPixmap('bug')
        self.assertFalse(ibug.isNull())

        # Not an existing pixmap
        ibug2 = images.getPixmap('bug2')
        self.assertTrue(ibug2.isNull())

    def testGetIcon(self):
        iopen = images.getIcon('document-open')
        self.assertFalse(iopen.isNull())

        ilibrary = images.getIcon('library')
        self.assertFalse(ilibrary.isNull())

        # Not an existing icon
        ilibrary2 = images.getIcon('library2')
        self.assertTrue(ilibrary2.isNull())
