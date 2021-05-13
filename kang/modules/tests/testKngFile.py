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

    def test_load_pickler(self):
        path = os.path.dirname(__file__)
        picklerfilename = os.path.join(path, 'pickler.kng')

        kng = kngfile.KngFile(picklerfilename)
        kng._load_pickler()

        self.assertEqual(kng.match_string, 'fruit=apple fruit=orange fruit=grapefruit color=red color=blue color=green vehicle=car vehicle=boat')
        self.assertEqual(kng.regex_string, '(?P<key>.*?)=(?P<value>.*?)')
        self.assertEqual(kng.replace_string, 'abc1def')
        self.assertEqual(kng.flag_ignorecase, True)
        self.assertEqual(kng.flag_multiline, True)
        self.assertEqual(kng.flag_dotall, True)
        self.assertEqual(kng.flag_verbose, True)
        self.assertEqual(kng.flag_locale, False)
        self.assertEqual(kng.flag_ascii, False)

        kng = kngfile.KngFile(picklerfilename)
        kng.load()

        self.assertEqual(kng.match_string, 'fruit=apple fruit=orange fruit=grapefruit color=red color=blue color=green vehicle=car vehicle=boat')
        self.assertEqual(kng.regex_string, '(?P<key>.*?)=(?P<value>.*?)')
        self.assertEqual(kng.replace_string, 'abc1def')
        self.assertEqual(kng.flag_ignorecase, True)
        self.assertEqual(kng.flag_multiline, True)
        self.assertEqual(kng.flag_dotall, True)
        self.assertEqual(kng.flag_verbose, True)
        self.assertEqual(kng.flag_locale, False)
        self.assertEqual(kng.flag_ascii, False)

    def test_load_with_exception(self):
        path = os.path.dirname(__file__)
        picklerfilename = os.path.join(path, 'badjson.kng')

        kng = kngfile.KngFile(picklerfilename)
        self.assertRaises(json.decoder.JSONDecodeError, kng.load)

    def test_kngfile(self):

        kngfilename = os.path.join(self.dtmp, 'test.kng')

        regex = 'A regular espression (.*?)'
        matchstring = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
        replace = 'Replace string \1'

        kf1 = kngfile.KngFile(kngfilename, regex, matchstring, replace, True, True, True, True, True)
        kf1.save()

        kf2 = kngfile.KngFile(kngfilename)
        kf2.load()

        self.assertEqual(kf1.match_string, kf2.match_string)
        self.assertEqual(kf1.regex_string, kf2.regex_string)
        self.assertEqual(kf1.replace_string, kf2.replace_string)

        self.assertEqual(kf1.flag_ignorecase, kf2.flag_ignorecase)
        self.assertEqual(kf1.flag_multiline, kf2.flag_multiline)
        self.assertEqual(kf1.flag_dotall, kf2.flag_dotall)
        self.assertEqual(kf1.flag_verbose, kf2.flag_verbose)
        self.assertEqual(kf1.flag_ascii, kf2.flag_ascii)
