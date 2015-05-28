from PyQt4.QtCore import QObject
import os
import shutil
import sys
import tempfile
import unittest

from kang.modules import recentfiles, util


class TestRecentFiles(unittest.TestCase):

    def setUp(self):
        # Set config directory
        self.dtmp = tempfile.mkdtemp()
        os.environ['XDG_CONFIG_HOME'] = self.dtmp
        cdir = util.getConfigDirectory()
        self.assertTrue(cdir.startswith(self.dtmp), '%s wrong config directory' % cdir)
        os.mkdir(cdir)

        self._write_msg = ''

    def tearDown(self):
        if self.dtmp:
            shutil.rmtree(self.dtmp)

    def test_recentfiles(self):
        parent = FakeParent()
        r1 = recentfiles.RecentFiles(parent)

        # Test save/load
        r1._recent_files = ['/home/goofy/kng/pippo1.kng', '/home/goofy/kng/pippo2.kng', '/home/goofy/kng/pippo3.kng']
        r1.save()
        r1.load()

        r2 = recentfiles.RecentFiles(parent)
        r2.load()
        self.assertEqual(r1._recent_files, r2._recent_files)

        # Test add
        an = len(r1._actions)
        r1.add('/home/goofy/kng/pippo4.kng')
        self.assertIn('/home/goofy/kng/pippo4.kng', r1._recent_files)
        self.assertEqual(an + 1, len(r1._actions))

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
        r1.save()
        r1.load()
        r1._clearMenu()

    def test_load_IOError(self):
        parent = FakeParent()
        rf = recentfiles.RecentFiles(parent)

        rf._filename = '/etc/shadow'  # something we could surely not read
        stderr = sys.stderr
        sys.stderr = self
        rf.load()
        sys.stderr = stderr
        self.assertTrue(self._write_msg, 'IOError was not raised')

    def test_save_IOError(self):
        parent = FakeParent()
        rf = recentfiles.RecentFiles(parent)

        rf._filename = '/Not_a_valid_path'
        stderr = sys.stderr
        sys.stderr = self
        rf.save()
        sys.stderr = stderr
        self.assertTrue(self._write_msg, 'IOError was not raised')

    def test_remove(self):
        parent = FakeParent()
        rf = recentfiles.RecentFiles(parent)

        fn1 = '/home/goofy/kng/pippo1.kng'
        fn2 = '/home/goofy/kng/pippo2.kng'
        fn3 = '/home/goofy/kng/pippo3.kng'
        rf._recent_files = [fn1, fn2]
        rf.save()
        rf.load()

        # Remove a file in the list
        an = len(rf._actions)
        rf.remove(fn1)
        self.assertNotIn(fn1, rf._recent_files)
        self.assertEqual(an - 1, len(rf._actions))

        # Remove a file not the list
        an = len(rf._actions)
        self.assertNotIn(fn3, rf._recent_files)
        rf.remove(fn3)
        self.assertNotIn(fn3, rf._recent_files)
        self.assertEqual(an, len(rf._actions))

    def write(self, msg):
        self._write_msg = msg


class FakeParent:

    def __init__(self):
        self.fileMenu = FakeMenu()

    def openFile(self, filename):
        pass


class FakeMenu:

    def addAction(self, filename):
        return FakeAction()

    def removeAction(self, action):
        pass


class FakeAction(QObject):
    pass
