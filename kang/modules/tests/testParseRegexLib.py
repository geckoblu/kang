import unittest

from kang.modules import parseRegexLib


class TestParseRegexLib(unittest.TestCase):

    def test_parse(self):
        rl = parseRegexLib.ParseRegexLib()
        rl.parse()
