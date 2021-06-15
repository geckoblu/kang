# pylint: disable=protected-access,missing-function-docstring

import os
import shutil
import tempfile
import unittest

from kang.modules import util


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

    def testGetConfigDirectory(self):
        # os.environ['XDG_CONFIG_HOME'] = ''
        configdir = util.getConfigDirectory()
        self.assertTrue(os.path.isdir(configdir), '%s is not a directory' % configdir)
        self.assertTrue(os.access(configdir, os.W_OK), '%s is not a user writable directory' % configdir)

    def testStrtobool(self):
        self.assertTrue(util.strtobool('True'))
        self.assertFalse(util.strtobool('False'))
        self.assertRaises(ValueError, util.strtobool, 1)

    def testFindFile(self):
        ntfile = tempfile.NamedTemporaryFile()
        dr, filename = os.path.split(ntfile.name)
        fname = util.findFile(dr, filename)
        self.assertEqual(ntfile.name, fname)

        fname = util.findFile(dr, 'not an existing filename')
        self.assertTrue(fname is None)
