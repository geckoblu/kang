# pylint: disable=protected-access,missing-function-docstring

import os
import shutil
import sys
import tempfile
import unittest

from PySide2.QtCore import QObject, Signal

from kang.modules import recentfiles, util


class TestRecentFiles(unittest.TestCase):

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

    def testRecentfiles(self):
        parent = FakeParent()
        r1 = recentfiles.RecentFiles(parent)

        # Test save/load
        r1._recentFiles = ['/home/goofy/kng/pippo1.kng',
                           '/home/goofy/kng/pippo2.kng',
                           '/home/goofy/kng/pippo3.kng']
        r1._save()
        # r1._load()

        r2 = recentfiles.RecentFiles(parent)
        r2._load()
        self.assertEqual(r1._recentFiles, r2._recentFiles)

        # Test add
        r3 = recentfiles.RecentFiles(parent)
        an = len(r3._actions)
        r3.add('/home/goofy/kng/pippo4.kng')
        self.assertIn('/home/goofy/kng/pippo4.kng', r3._recentFiles)
        self.assertEqual(an + 1, len(r3._actions))

        # Test setNumShown
        numShow = 2
        r1.setNumShown(numShow)
        self.assertEqual(numShow, len(r1._actions))
        # Set again with same value
        r1.setNumShown(numShow)
        self.assertEqual(numShow, len(r1._actions))
        # Set again incrementing
        numShow += 1
        r1.setNumShown(numShow)
        self.assertEqual(numShow, len(r1._actions))

        # Test openfile
        r1._openFile('/home/goofy/kng/pippo.kng')

        # Test clearMenu
        r1._save()
        r1._load()
        r1._clearMenu()

    def testRemove(self):
        parent = FakeParent()
        rf = recentfiles.RecentFiles(parent)

        fn1 = '/home/goofy/kng/pippo1.kng'
        fn2 = '/home/goofy/kng/pippo2.kng'
        fn3 = '/home/goofy/kng/pippo3.kng'
        rf._recentFiles = [fn1, fn2]
        rf._save()
        rf._load()

        # Remove a file in the list
        an = len(rf._actions)
        rf.remove(fn1)
        self.assertNotIn(fn1, rf._recentFiles)
        self.assertEqual(an - 1, len(rf._actions))

        # Remove a file not the list
        an = len(rf._actions)
        self.assertNotIn(fn3, rf._recentFiles)
        rf.remove(fn3)
        self.assertNotIn(fn3, rf._recentFiles)
        self.assertEqual(an, len(rf._actions))

    def testLoadIOError(self):
        parent = FakeParent()
        rf = recentfiles.RecentFiles(parent)

        rf._filename = '/etc/shadow'  # something we could surely not read
        stderr = sys.stderr
        sys.stderr = self
        self.resetMsg()
        rf._load()
        sys.stderr = stderr
        self.assertMsgRaised()

    def testSaveIOError(self):
        parent = FakeParent()
        rf = recentfiles.RecentFiles(parent)

        rf._filename = '/Not_a_valid_path'
        stderr = sys.stderr
        sys.stderr = self
        self.resetMsg()
        rf._save()
        sys.stderr = stderr
        self.assertMsgRaised()

    def resetMsg(self):
        self._writeMsg = ''

    def assertMsgRaised(self):
        self.assertTrue(self._writeMsg, 'IOError was not raised')

    def write(self, msg):
        self._writeMsg = msg


class FakeParent:

    def __init__(self):
        self._fileMenu = FakeMenu()
        self._placeholderAction = FakeAction()

    def loadFile(self, filename):
        pass

# pylint: disable=unused-argument
class FakeMenu:

    def insertAction(self, before, action):
        return action

    def removeAction(self, action):
        pass


class FakeAction(QObject):
    triggered = Signal()
