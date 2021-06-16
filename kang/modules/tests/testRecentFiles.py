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
        recents1 = recentfiles.RecentFiles(parent)

        # Test save/load
        recents1._recentFiles = ['/home/goofy/kng/pippo1.kng',
                                 '/home/goofy/kng/pippo2.kng',
                                 '/home/goofy/kng/pippo3.kng']
        recents1._save()
        # recents1._load()

        recents2 = recentfiles.RecentFiles(parent)
        recents2._load()
        self.assertEqual(recents1._recentFiles, recents2._recentFiles)

        # Test add
        recents3 = recentfiles.RecentFiles(parent)
        actionsLenBefore = len(recents3._actions)
        recents3.add('/home/goofy/kng/pippo4.kng')
        self.assertIn('/home/goofy/kng/pippo4.kng', recents3._recentFiles)
        actionsLenAfter = len(recents3._actions)
        self.assertEqual(actionsLenAfter, actionsLenBefore + 1)

        # Test setNumShown
        numShow = 2
        recents1.setNumShown(numShow)
        self.assertEqual(numShow, len(recents1._actions))
        # Set again with same value
        recents1.setNumShown(numShow)
        self.assertEqual(numShow, len(recents1._actions))
        # Set again incrementing
        numShow += 1
        recents1.setNumShown(numShow)
        self.assertEqual(numShow, len(recents1._actions))

        # Test openfile
        recents1._openFile('/home/goofy/kng/pippo.kng')

        # Test clearMenu
        recents1._save()
        recents1._load()
        recents1._clearMenu()

    def testRemove(self):
        parent = FakeParent()
        recents = recentfiles.RecentFiles(parent)

        fn1 = '/home/goofy/kng/pippo1.kng'
        fn2 = '/home/goofy/kng/pippo2.kng'
        fn3 = '/home/goofy/kng/pippo3.kng'
        recents._recentFiles = [fn1, fn2]
        recents._save()
        recents._load()

        # Remove a file in the list
        actionsLenBefore = len(recents._actions)
        recents.remove(fn1)
        self.assertNotIn(fn1, recents._recentFiles)
        actionsLenAfter = len(recents._actions)
        self.assertEqual(actionsLenAfter, actionsLenBefore - 1)

        # Remove a file not the list
        actionsLenBefore = len(recents._actions)
        self.assertNotIn(fn3, recents._recentFiles)
        recents.remove(fn3)
        self.assertNotIn(fn3, recents._recentFiles)
        actionsLenAfter = len(recents._actions)
        self.assertEqual(actionsLenAfter, actionsLenBefore)

    def testLoadIOError(self):
        parent = FakeParent()
        recents = recentfiles.RecentFiles(parent)

        recents._filename = '/etc/shadow'  # something we could surely not read
        stderr = sys.stderr
        sys.stderr = self
        self.resetMsg()
        recents._load()
        sys.stderr = stderr
        self.assertMsgRaised()

    def testSaveIOError(self):
        parent = FakeParent()
        recents = recentfiles.RecentFiles(parent)

        recents._filename = '/Not_a_valid_path'
        stderr = sys.stderr
        sys.stderr = self
        self.resetMsg()
        recents._save()
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
