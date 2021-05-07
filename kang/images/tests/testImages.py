from PySide2.QtCore import QCoreApplication
from PySide2.QtGui import QApplication
import sys
import unittest

from kang import images


class TestImages(unittest.TestCase):

    def setUp(self):
        self.qApp = QCoreApplication.instance()
        if not self.qApp:
            self.qApp = QApplication(sys.argv)

    def test_getPixmap(self):
        ibug = images.getPixmap('bug')
        self.assertFalse(ibug.isNull())

        # Not an existing pixmap
        ibug2 = images.getPixmap('bug2')
        self.assertTrue(ibug2.isNull())

    def test_getIcon(self):
        iopen = images.getIcon('document-open')
        self.assertFalse(iopen.isNull())

        ilibrary = images.getIcon('library')
        self.assertFalse(ilibrary.isNull())

        # Not an existing icon
        ilibrary2 = images.getIcon('library2')
        self.assertTrue(ilibrary2.isNull())
