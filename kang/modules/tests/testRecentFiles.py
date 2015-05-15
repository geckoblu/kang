from PyQt4.QtCore import QObject
import os
import shutil
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

        # Test remove
        an = len(r1._actions)
        r1.remove('/home/goofy/kng/pippo4.kng')
        self.assertNotIn('/home/goofy/kng/pippo4.kng', r1._recent_files)
        self.assertEqual(an - 1, len(r1._actions))

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
