import os
import shutil
import tempfile
import unittest

from kang.modules import preferences, util


class TestUtil(unittest.TestCase):

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

    def test_preferences(self):
            pref = preferences.Preferences()

            pref.recentFilesNum = pref._DEFAULTRECENTFILESNUM + 1
            pref.askSave = not pref._ASKSAVE
            pref.askSaveOnlyForNamedProjects = not pref._ASKSAVEONLYFORNAMEDPROJECTS

            pref.save()

            pref2 = preferences.Preferences()

            self.assertEqual(pref.recentFilesNum, pref2.recentFilesNum)
            self.assertEqual(pref.askSave, pref2.askSave)
            self.assertEqual(pref.askSaveOnlyForNamedProjects, pref2.askSaveOnlyForNamedProjects)
