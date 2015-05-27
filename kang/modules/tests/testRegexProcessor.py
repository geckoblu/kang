import re
import unittest

from kang.modules.regexprocessor import RegexProcessor, MATCH_OK, MATCH_NA, MATCH_FAIL


class TestRegexProcessor(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestRegexProcessor, self).__init__(*args, **kwargs)
        self._statusChanged = False

    def test_match(self):
        rp = RegexProcessor()
        rp.connect(self.statusChanged)

        rp.setMatchString('La donzelletta vien dalla campagna e vien in compagnia di rose e viole')
        status, _ = rp.getStatus()
        self.assertEqual(status, MATCH_NA)

        # Three matches
        self._statusChanged = False
        rp.setRegexString('v')
        status, _ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)
        spans = rp.getAllSpans()
        self.assertEqual(len(spans), 3)
        self.assertEqual(spans, [(15, 16), (37, 38), (65, 66)])
        self.assertEqual(len(rp._groupTuples), 0)
        self.assertTrue(self._statusChanged)

        # Two matches
        self._statusChanged = False
        rp.setRegexString('vien')
        status, _ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)
        spans = rp.getAllSpans()
        self.assertEqual(len(spans), 2)
        self.assertEqual(spans, [(15, 19), (37, 41)])
        self.assertEqual(len(rp._groupTuples), 0)
        self.assertTrue(self._statusChanged)

        # No matches
        self._statusChanged = False
        rp.setRegexString('xxx')
        status, _ = rp.getStatus()
        self.assertEqual(status, MATCH_FAIL)
        spans = rp.getAllSpans()
        self.assertEqual(len(spans), 0)
        self.assertEqual(spans, [])
        self.assertEqual(len(rp._groupTuples), 0)
        self.assertTrue(self._statusChanged)

    def test_groups(self):
        rp = RegexProcessor()
        rp.connect(self.statusChanged)

        rp.setMatchString('La donzelletta vien dalla campagna e vien in compagnia di rose e viole')
        status, _ = rp.getStatus()
        self.assertEqual(status, MATCH_NA)

        # One group, two matches
        self._statusChanged = False
        rp.setRegexString('(vien)')
        status, _ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)
        spans = rp.getAllSpans()
        self.assertEqual(len(spans), 2)
        self.assertEqual(spans, [(15, 19), (37, 41)])
        self.assertEqual(len(rp._groupTuples), 2)
        self.assertEqual(rp.getGroups(0), [(1, '', 'vien')])
        self.assertEqual(rp.getGroups(1), [(1, '', 'vien')])
        self.assertEqual(rp.getGroups(2), [])  # out of index
        self.assertTrue(self._statusChanged)

        # Two groups, three matches
        self._statusChanged = False
        rp.setRegexString('(vien)|(gna)')
        status, _ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)
        spans = rp.getAllSpans()
        self.assertEqual(len(spans), 3)
        self.assertEqual(spans, [(15, 19), (31, 34), (37, 41)])
        self.assertEqual(len(rp._groupTuples), 3)
        self.assertEqual(rp.getGroups(0), [(1, '', 'vien'), (2, '', '')])
        self.assertEqual(rp.getGroups(1), [(1, '', ''), (2, '', 'gna')])
        self.assertEqual(rp.getGroups(2), [(1, '', 'vien'), (2, '', '')])
        self.assertTrue(self._statusChanged)

        # Two groups (one named), three matches
        self._statusChanged = False
        rp.setRegexString('(?P<n1>vien)|(gna)')
        status, _ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)
        spans = rp.getAllSpans()
        self.assertEqual(len(spans), 3)
        self.assertEqual(spans, [(15, 19), (31, 34), (37, 41)])
        self.assertEqual(len(rp._groupTuples), 3)
        self.assertEqual(rp.getGroups(0), [(1, 'n1', 'vien'), (2, '', '')])
        self.assertEqual(rp.getGroups(1), [(1, 'n1', ''), (2, '', 'gna')])
        self.assertEqual(rp.getGroups(2), [(1, 'n1', 'vien'), (2, '', '')])
        self.assertTrue(self._statusChanged)

        # Two groups (both named), three matches
        self._statusChanged = False
        rp.setRegexString('(?P<n1>vien)|(?P<n2>gna)')
        status, _ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)
        spans = rp.getAllSpans()
        self.assertEqual(len(spans), 3)
        self.assertEqual(spans, [(15, 19), (31, 34), (37, 41)])
        self.assertEqual(len(rp._groupTuples), 3)
        self.assertEqual(rp.getGroups(0), [(1, 'n1', 'vien'), (2, 'n2', '')])
        self.assertEqual(rp.getGroups(1), [(1, 'n1', ''), (2, 'n2', 'gna')])
        self.assertEqual(rp.getGroups(2), [(1, 'n1', 'vien'), (2, 'n2', '')])
        self.assertTrue(self._statusChanged)

        # Two groups (same name)
        self._statusChanged = False
        rp.setRegexString('(?P<n1>vien)|(?P<n1>gna)')
        status, _ = rp.getStatus()
        self.assertEqual(status, MATCH_FAIL)
        self.assertTrue(self._statusChanged)

        # One group plus one match
        self._statusChanged = False
        rp.setRegexString('(vien)|gna')
        status, _ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)
        spans = rp.getAllSpans()
        self.assertEqual(len(spans), 3)
        self.assertEqual(spans, [(15, 19), (31, 34), (37, 41)])
        self.assertEqual(len(rp._groupTuples), 3)
        self.assertEqual(rp.getGroups(0), [(1, '', 'vien')])
        self.assertEqual(rp.getGroups(1), [(1, '', '')])
        self.assertTrue(self._statusChanged)

    def test_replace(self):
        rp = RegexProcessor()
        rp.setMatchString('abcdabc')

        # Normal match (2)
        rp.setRegexString('b')
        status, _ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)
        rp.setReplaceString('x')
        status, _ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)

        status, strings = rp.replace(1)
        self.assertEqual(status, MATCH_OK)
        self.assertEqual(strings, ['a', 'x', 'cdabc'])

        status, strings = rp.replace(2)
        self.assertEqual(status, MATCH_OK)
        self.assertEqual(strings, ['a', 'x', 'cda', 'x', 'c'])

        status, strings = rp.replace(0)  # 0 stands for 'all'
        self.assertEqual(status, MATCH_OK)
        self.assertEqual(strings, ['a', 'x', 'cda', 'x', 'c'])

        status, strings = rp.replace(3)
        self.assertEqual(status, MATCH_OK)
        self.assertEqual(strings, ['a', 'x', 'cda', 'x', 'c'])

        # Group match (2)
        rp.setRegexString('(b)')
        status, _ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)
        rp.setReplaceString('x')
        status, _ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)

        status, strings = rp.replace(0)  # 0 stands for 'all'
        self.assertEqual(status, MATCH_OK)
        self.assertEqual(strings, ['a', 'x', 'cda', 'x', 'c'])

        rp.setReplaceString(r'x\1')
        status, _ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)

        status, strings = rp.replace(0)  # 0 stands for 'all'
        self.assertEqual(status, MATCH_OK)
        self.assertEqual(strings, [u'a', u'x', u'bcda', u'x', u'bc'])

        rp.setReplaceString(r'x\2')
        status, _ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)
        status, strings = rp.replace(0)  # 0 stands for 'all'
        self.assertEqual(status, MATCH_FAIL)
        self.assertEqual(strings, 'invalid group reference')

        rp.setReplaceString('x\\')
        status, _ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)
        status, strings = rp.replace(0)  # 0 stands for 'all'
        self.assertEqual(status, MATCH_FAIL)
        self.assertEqual(strings, 'bogus escape (end of line)')

    def test_ignorecase(self):
        rp = RegexProcessor()
        rp.setMatchString('V')

        rp.setRegexString('v')
        status, _ = rp.getStatus()
        self.assertEqual(status, MATCH_FAIL)

        rp.setIgnorecaseFlag(True)
        self.assertEqual(rp._flags, re.IGNORECASE)
        rp.setRegexString('v')
        status, _ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)

        rp.setIgnorecaseFlag(True)
        rp.setRegexString('(?i)v')
        status, _ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)

    def test_getRegexCode(self):
        rp = RegexProcessor()
        rp.connect(self.statusChanged)

        rp.setMatchString('abcdabc')
        code = rp.getRegexCode()
        rp.setRegexString('(b)')
        code = rp.getRegexCode()

    def test_embeddedFlags(self):
        rp = RegexProcessor()

        rp.setMatchString('abcdabc')
        rp.setRegexString('(?iLmsux)')

    def test_examine(self):
        rp = RegexProcessor()
        rp.setMatchString('123456789')

        rp.setRegexString('1222222345')
        old, new = rp.examine()
        self.assertEqual(old, '1222222345')
        self.assertEqual(new, '12')

        rp.setRegexString('xxx')
        old, new = rp.examine()
        self.assertEqual(old, 'xxx')
        self.assertEqual(new, '')

        rp.setRegexString('')
        old, new = rp.examine()
        self.assertEqual(old, '')
        self.assertEqual(new, '')

        rp.setRegexString('(?P<n1>x)|(?P<n1>y)')  # invalid regex
        old, new = rp.examine()
        self.assertEqual(old, '(?P<n1>x)|(?P<n1>y)')
        self.assertEqual(new, '(?P<n1>x)|')

    def statusChanged(self):
        self._statusChanged = True
