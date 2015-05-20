import unittest

from kang.modules.regexprocessor import RegexProcessor


class TestRegexProcessor(unittest.TestCase):

    def test_getRegexCode(self):
        rp = RegexProcessor()
        code = rp.getRegexCode()
        print(code)
