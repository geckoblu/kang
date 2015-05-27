import os
import shutil
import tempfile
import unittest

from kang.modules import kngfile


class TestKngFile(unittest.TestCase):

    def setUp(self):
        # Set config directory
        self.dtmp = tempfile.mkdtemp()

    def tearDown(self):
        if self.dtmp:
            shutil.rmtree(self.dtmp)

    def test_kngFile(self):

        kn = os.path.join(self.dtmp, 'test.kng')

        regex = 'A regular espression (.*?)'
        matchstring = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
        replace = 'Replace string \1'
        flags = 90

        kf1 = kngfile.KngFile(kn, regex, matchstring, replace, flags)
        kf1.save()

        kf2 = kngfile.KngFile(kn)
        kf2.load()

        self.assertEqual(kf1.regex, kf2.regex)
        self.assertEqual(kf1.matchstring, kf2.matchstring)
        self.assertEqual(kf1.replace, kf2.replace)
        self.assertEqual(kf1.flags, kf2.flags)
