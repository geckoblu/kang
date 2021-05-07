# pylint: disable=protected-access

from PySide2.QtCore import QCoreApplication
from PySide2.QtGui import QApplication
from PySide2.QtTest import QTest
import sys
import unittest

from kang.gui.statusbar import StatusBar
from kang.gui.tests.fakeparent import FakeParent
from kang.images import getPixmap


class TestStatusBar(unittest.TestCase):

    def setUp(self):
        self.qApp = QCoreApplication.instance()
        if not self.qApp:
            self.qApp = QApplication(sys.argv)

        self.greenPixmap = getPixmap('greenStatusIcon.xpm')
        self.redPixmap = getPixmap('redStatusIcon.xpm')

    def test_stastusbar(self):
        parent = FakeParent()
        StatusBar(parent)

    def test_setMessage(self):
        parent = FakeParent()
        sb = StatusBar(parent)

        sb.setMessage('Just a message')
        self.assertEqual(sb._statusLabel.text(), 'Just a message')

        sb.setMessage('Just a message', pixmap=self.greenPixmap)
        self.assertEqual(sb._pixmapLabel.pixmap().cacheKey(), self.greenPixmap.cacheKey())

        sb.setMessage('Just another message', duration=1, pixmap=self.redPixmap)
        self.assertEqual(sb._statusLabel.text(), 'Just another message')
        self.assertEqual(sb._pixmapLabel.pixmap().cacheKey(), self.redPixmap.cacheKey())
        QTest.qWait(2000)
        self.assertEqual(sb._statusLabel.text(), 'Just a message')
        # How to test is the right pixmap ?
        # self.assertEqual(sb._pixmapLabel.pixmap().cacheKey(), self.greenPixmap.cacheKey())

    def test_resetMessage(self):
        parent = FakeParent()
        sb = StatusBar(parent)

        sb.setMessage('Just a message')
        sb._resetMessage()
        self.assertEqual(sb._statusLabel.text(), '')
