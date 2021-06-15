# pylint: disable=protected-access

import os
import shutil
import tempfile
import unittest

from PySide2.QtCore import QSize

from kang.modules.windowsettings import WindowSettings


class TestUtil(unittest.TestCase):

    def setUp(self):
        # Set config directory
        self.dtmp = tempfile.mkdtemp()

    def tearDown(self):
        if self.dtmp:
            shutil.rmtree(self.dtmp)

    def testWindowSettings(self):

        filename = os.path.join(self.dtmp, 'windowsettings.json')

        window = FakeWindow()
        windowsettings = WindowSettings(filename)
        windowsettings.save(window)

        window2 = FakeWindow()
        windowsettings2 = WindowSettings(filename)
        windowsettings2.restore(window2)


class FakeWindow:

    # pylint: disable=invalid-name
    def __init__(self):
        self._x = 12
        self._y = 34
        self._size = QSize(123, 456)
        self._showRegexReferenceGuide = True
        self._showRegexLibrary = True
        self._splitter = FakeSplitter()
        self._helpRegexReferenceGuideAction = FakeAction()
        self._helpRegexLibraryAction = FakeAction()

    def size(self):
        return self._size

    def x(self):
        return self._x

    def y(self):
        return self._y

    def move(self, x, y):
        self._x = x
        self._y = y

    def resize(self, width, height):
        self._size = QSize(width, height)

    def _helpRegexReferenceGuide(self, showRegexReferenceGuide):
        self._showRegexReferenceGuide = showRegexReferenceGuide

    def _helpRegexLibrary(self, showRegexLibrary):
        self._showRegexLibrary = showRegexLibrary


class FakeSplitter:

    def sizes(self):
        return [12, 34]

    def setSizes(self, sizes):
        pass


class FakeAction:

    def __init__(self):
        self._status = False

    def setChecked(self, flag):
        self._status = flag
