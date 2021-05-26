# pylint: disable=protected-access
import json
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

    def testLoadPickler(self):
        path = os.path.dirname(__file__)
        picklerfilename = os.path.join(path, 'pickler.kng')

        kng = kngfile.KngFile(picklerfilename)
        kng._loadPickler()

        matchString = 'fruit=apple fruit=orange color=red color=green vehicle=car vehicle=boat'

        self.assertEqual(kng.matchString, matchString)
        self.assertEqual(kng.regexString, '(?P<key>.*?)=(?P<value>.*?)')
        self.assertEqual(kng.replaceString, 'abc1def')
        self.assertEqual(kng.flagIgnorecase, True)
        self.assertEqual(kng.flagMultiline, True)
        self.assertEqual(kng.flagDotall, True)
        self.assertEqual(kng.flagVerbose, True)
        self.assertEqual(kng.flagAscii, False)

        kng = kngfile.KngFile(picklerfilename)
        kng.load()

        self.assertEqual(kng.matchString, matchString)
        self.assertEqual(kng.regexString, '(?P<key>.*?)=(?P<value>.*?)')
        self.assertEqual(kng.replaceString, 'abc1def')
        self.assertEqual(kng.flagIgnorecase, True)
        self.assertEqual(kng.flagMultiline, True)
        self.assertEqual(kng.flagDotall, True)
        self.assertEqual(kng.flagVerbose, True)
        self.assertEqual(kng.flagAscii, False)

    def testLoadWithException(self):
        path = os.path.dirname(__file__)
        picklerfilename = os.path.join(path, 'badjson.kng')

        kng = kngfile.KngFile(picklerfilename)
        self.assertRaises(json.decoder.JSONDecodeError, kng.load)

    def testKngfile(self):

        kngfilename = os.path.join(self.dtmp, 'test.kng')

        regex = 'A regular espression (.*?)'
        matchstring = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
        replace = 'Replace string \1'

        kf1 = kngfile.KngFile(kngfilename, regex, matchstring, replace, True, True, True, True, True)
        kf1.save()

        kf2 = kngfile.KngFile(kngfilename)
        kf2.load()

        self.assertEqual(kf1.matchString, kf2.matchString)
        self.assertEqual(kf1.regexString, kf2.regexString)
        self.assertEqual(kf1.replaceString, kf2.replaceString)

        self.assertEqual(kf1.flagIgnorecase, kf2.flagIgnorecase)
        self.assertEqual(kf1.flagMultiline, kf2.flagMultiline)
        self.assertEqual(kf1.flagDotall, kf2.flagDotall)
        self.assertEqual(kf1.flagVerbose, kf2.flagVerbose)
        self.assertEqual(kf1.flagAscii, kf2.flagAscii)
