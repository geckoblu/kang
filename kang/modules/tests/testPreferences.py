# pylint: disable=protected-access

import os
import shutil
import tempfile
import unittest

from kang.modules import util
from kang.modules.preferences import Preferences


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

    def testPreferences(self):
        pref = Preferences()

        pref.recentFilesNum = pref.recentFilesNum + 1
        pref.askSave = not pref.askSave
        pref.askSaveOnlyForNamedProjects = not pref.askSaveOnlyForNamedProjects

        pref.save()

        pref2 = Preferences()
        pref2.load()

        self.assertEqual(pref.recentFilesNum, pref2.recentFilesNum)
        self.assertEqual(pref.askSave, pref2.askSave)
        self.assertEqual(pref.askSaveOnlyForNamedProjects, pref2.askSaveOnlyForNamedProjects)

    def testLoadValueError(self):
        pref = Preferences()
        pref.recentFilesNum = 'NaN'
        pref.askSave = 'NaBool'
        pref.askSaveOnlyForNamedProjects = 'NaBool'
        pref.save()

        default = Preferences()

        pref2 = Preferences()
        pref2.load()

        self.assertEqual(pref2.recentFilesNum, default.recentFilesNum)
        self.assertEqual(pref2.askSave, default.askSave)
        self.assertEqual(pref2.askSaveOnlyForNamedProjects, default.askSaveOnlyForNamedProjects)
        
    def testToStr(self):
        pref = Preferences()
        
        _prefStr = str(pref)
        # Nothing to check? Only code execution
        
    def testBadFilename(self):
        pref = Preferences('thisisnotafilename')
        pref.load()
        # Nothing to check? Only code execution
