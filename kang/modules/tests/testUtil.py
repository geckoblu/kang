# pylint: disable=protected-access
import os
import shutil
import sys
import tempfile
import unittest

from PySide2.QtCore import QSize

from kang.modules import util


class TestUtil(unittest.TestCase):

    def setUp(self):
        # Set config directory
        self.dtmp = tempfile.mkdtemp()
        os.environ['XDG_CONFIG_HOME'] = self.dtmp
        cdir = util.getConfigDirectory()
        self.assertTrue(cdir.startswith(self.dtmp), '%s wrong config directory' % cdir)
        os.mkdir(cdir)

        self._writeMsg = ''

    def tearDown(self):
        if self.dtmp:
            shutil.rmtree(self.dtmp)

    def testFindFile(self):
        ntfile = tempfile.NamedTemporaryFile()
        dr, filename = os.path.split(ntfile.name)
        fname = util.findFile(dr, filename)
        self.assertEqual(ntfile.name, fname)

        fname = util.findFile(dr, 'not an existing filename')
        self.assertTrue(fname == None)

    def testGetConfigDirectory(self):
        os.environ['XDG_CONFIG_HOME'] = ''
        cdir = util.getConfigDirectory()
        self.assertTrue(os.path.isdir(cdir), '%s is not a directory' % cdir)
        self.assertTrue(os.access(cdir, os.W_OK), '%s is not a user writable directory' % cdir)


class FakeWindow:

    def __init__(self, x=0, y=0, width=0, height=0):
        self._x = x
        self._y = y
        self._size = QSize(width, height)

    def size(self):
        return self._size

    def x(self):
        return self._x

    def y(self):
        return self._y

    def move(self, x, y):
        self._x = x
        self._y = y

    def resize(self, size):
        self._size = QSize(size)

    def __eq__(self, other):
        return self._x == other._x and self._y == other._y and self._size == other._size

    def __repr__(self):
        return 'FWindow[x:%d y:%d w:%d h:%d]' % (self._x, self._y, self._size.width(), self._size.height())
