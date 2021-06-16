# pylint: disable=protected-access,missing-function-docstring

import unittest

from kang.modules.regexprocessor import RegexProcessor, MATCH_OK, MATCH_NA, MATCH_FAIL


class TestRegexProcessor(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestRegexProcessor, self).__init__(*args, **kwargs)
        self._statusChanged = False

    def testMatch(self):
        rep = RegexProcessor()
        rep.statusChanged.connect(self.statusChanged)

        rep.setMatchString('La donzelletta vien dalla campagna e vien in compagnia di rose e viole')
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_NA)

        # Three matches
        self.resetStatusChanged()
        rep.setRegexString('v')
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_OK)
        spans = rep.getAllSpans()
        self.assertEqual(len(spans), 3)
        self.assertEqual(spans, [(15, 16), (37, 38), (65, 66)])
        self.assertEqual(rep.getSpan(1), (37, 38))
        self.assertEqual(len(rep._groupTuples), 0)
        self.assertStatusChanged()

        # Two matches
        self.resetStatusChanged()
        rep.setRegexString('vien')
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_OK)
        spans = rep.getAllSpans()
        self.assertEqual(len(spans), 2)
        self.assertEqual(spans, [(15, 19), (37, 41)])
        self.assertEqual(len(rep._groupTuples), 0)
        self.assertStatusChanged()

        # No matches
        self.resetStatusChanged()
        rep.setRegexString('xxx')
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_FAIL)
        spans = rep.getAllSpans()
        self.assertEqual(len(spans), 0)
        self.assertEqual(spans, [])
        self.assertEqual(len(rep._groupTuples), 0)
        self.assertStatusChanged()

    def testGroups(self):
        rep = RegexProcessor()
        rep.statusChanged.connect(self.statusChanged)

        rep.setMatchString('La donzelletta vien dalla campagna e vien in compagnia di rose e viole')
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_NA)

        # One group, two matches
        self.resetStatusChanged()
        rep.setRegexString('(vien)')
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_OK)
        spans = rep.getAllSpans()
        self.assertEqual(len(spans), 2)
        self.assertEqual(spans, [(15, 19), (37, 41)])
        self.assertEqual(len(rep._groupTuples), 2)
        groups = rep.getAllGroups()
        self.assertEqual(groups[0], [(1, '', 'vien')])
        self.assertEqual(groups[1], [(1, '', 'vien')])
        self.assertStatusChanged()

        # Two groups, three matches
        self.resetStatusChanged()
        rep.setRegexString('(vien)|(gna)')
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_OK)
        spans = rep.getAllSpans()
        self.assertEqual(len(spans), 3)
        self.assertEqual(spans, [(15, 19), (31, 34), (37, 41)])
        self.assertEqual(len(rep._groupTuples), 3)
        groups = rep.getAllGroups()
        self.assertEqual(groups[0], [(1, '', 'vien'), (2, '', '')])
        self.assertEqual(groups[1], [(1, '', ''), (2, '', 'gna')])
        self.assertEqual(groups[2], [(1, '', 'vien'), (2, '', '')])
        self.assertStatusChanged()

        # Two groups (one named), three matches
        self.resetStatusChanged()
        rep.setRegexString('(?P<n1>vien)|(gna)')
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_OK)
        spans = rep.getAllSpans()
        self.assertEqual(len(spans), 3)
        self.assertEqual(spans, [(15, 19), (31, 34), (37, 41)])
        self.assertEqual(len(rep._groupTuples), 3)
        groups = rep.getAllGroups()
        self.assertEqual(groups[0], [(1, 'n1', 'vien'), (2, '', '')])
        self.assertEqual(groups[1], [(1, 'n1', ''), (2, '', 'gna')])
        self.assertEqual(groups[2], [(1, 'n1', 'vien'), (2, '', '')])
        self.assertStatusChanged()

        # Two groups (both named), three matches
        self.resetStatusChanged()
        rep.setRegexString('(?P<n1>vien)|(?P<n2>gna)')
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_OK)
        spans = rep.getAllSpans()
        self.assertEqual(len(spans), 3)
        self.assertEqual(spans, [(15, 19), (31, 34), (37, 41)])
        self.assertEqual(len(rep._groupTuples), 3)
        groups = rep.getAllGroups()
        self.assertEqual(groups[0], [(1, 'n1', 'vien'), (2, 'n2', '')])
        self.assertEqual(groups[1], [(1, 'n1', ''), (2, 'n2', 'gna')])
        self.assertEqual(groups[2], [(1, 'n1', 'vien'), (2, 'n2', '')])
        self.assertStatusChanged()

        # Two groups (same name)
        self.resetStatusChanged()
        rep.setRegexString('(?P<n1>vien)|(?P<n1>gna)')
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_FAIL)
        self.assertStatusChanged()

        # One group plus one match
        self.resetStatusChanged()
        rep.setRegexString('(vien)|gna')
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_OK)
        spans = rep.getAllSpans()
        self.assertEqual(len(spans), 3)
        self.assertEqual(spans, [(15, 19), (31, 34), (37, 41)])
        self.assertEqual(len(rep._groupTuples), 3)
        groups = rep.getAllGroups()
        self.assertEqual(groups[0], [(1, '', 'vien')])
        self.assertEqual(groups[1], [(1, '', '')])
        self.assertStatusChanged()

    def testReplace(self):
        rep = RegexProcessor()
        rep.setMatchString('abcdabcbc')

        # Normal match (2)
        rep.setRegexString('b')
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_OK)
        rep.setReplaceString('x')
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_OK)

        status, strings = rep.replace(1)
        self.assertEqual(status, MATCH_OK)
        self.assertEqual(strings, ['axcdabcbc'])

        status, strings = rep.replace(2)
        self.assertEqual(status, MATCH_OK)
        self.assertEqual(strings, ['axcdaxcbc'])

        status, strings = rep.replace(0)  # 0 stands for 'all'
        self.assertEqual(status, MATCH_OK)
        self.assertEqual(strings, ['axcdaxcxc'])

        status, strings = rep.replace(3)
        self.assertEqual(status, MATCH_OK)
        self.assertEqual(strings, ['axcdaxcxc'])

        status, strings = rep.replace(4)
        self.assertEqual(status, MATCH_OK)
        self.assertEqual(strings, ['axcdaxcxc'])

        # Group match (2)
        rep.setRegexString('(b)')
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_OK)
        rep.setReplaceString('x')
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_OK)

        status, strings = rep.replace(0)  # 0 stands for 'all'
        self.assertEqual(status, MATCH_OK)
        self.assertEqual(strings, ['axcdaxcxc'])

        rep.setReplaceString(r'x\1')
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_OK)

        status, strings = rep.replace(0)  # 0 stands for 'all'
        self.assertEqual(status, MATCH_OK)
        self.assertEqual(strings, ['axbcdaxbcxbc'])

        rep.setReplaceString(r'x\2')
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_OK)
        status, strings = rep.replace(0)  # 0 stands for 'all'
        self.assertEqual(status, MATCH_FAIL)
        self.assertEqual(strings, 'invalid group reference 2 at position 2')

        rep.setReplaceString('x\\')
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_OK)
        status, strings = rep.replace(0)  # 0 stands for 'all'
        self.assertEqual(status, MATCH_FAIL)
        self.assertEqual(strings, 'bad escape (end of pattern) at position 1')

        # Real case - which would be the correct colorized ?
        rep.setMatchString("""<p><a class="calibre7" id="filepos48765"></a></p>
    <blockquote class="calibre19">
    <a class="calibre8" href="#filepos20421"><span class="calibre9 underline">1</span></a>
    </blockquote>""")
        rep.setRegexString("""<p><a class="calibre7" id="(.*?)"></a></p>
    <blockquote class="calibre19">
    <a class="calibre8" href="(.*?)"><span class="calibre9 underline">(.*?)</span></a>
    </blockquote>""")
        rep.setReplaceString(r'<a class="noteref" id="\1" href="\2">\3</a>')
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_OK)
        status, strings = rep.replace(0)  # 0 stands for 'all'
        self.assertEqual(status, MATCH_OK)
        self.assertEqual(strings, ['<a class="noteref" id="filepos48765" href="#filepos20421">1</a>'])

    def testIgnorecase(self):
        rep = RegexProcessor()
        rep.setMatchString('Newton')

        rep.setIgnorecaseFlag(False)
        rep.setRegexString('newton')
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_FAIL)

        rep.setIgnorecaseFlag(True)
        rep.setRegexString('newton')
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_OK)

        rep.setIgnorecaseFlag(False)
        rep.setRegexString('(?i)newton')
        self.assertTrue(rep._ignorecaseFlagEmbedded)
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_OK)

    def testMultiline(self):
        rep = RegexProcessor()
        rep.setMatchString("""one
two""")

        rep.setMultilineFlag(False)
        rep.setRegexString('^two')
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_FAIL)

        rep.setMultilineFlag(True)
        rep.setRegexString('^two')
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_OK)

        rep.setMultilineFlag(False)
        rep.setRegexString('(?m)^two')
        self.assertTrue(rep._multilineFlagEmbedded)
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_OK)

    def testDotall(self):
        rep = RegexProcessor()
        rep.setMatchString("""one
two""")

        rep.setDotallFlag(False)
        rep.setRegexString('one.')
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_FAIL)

        rep.setDotallFlag(True)
        rep.setRegexString('one.')
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_OK)

        rep.setDotallFlag(False)
        rep.setRegexString('(?s)one.')
        self.assertTrue(rep._dotallFlagEmbedded)
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_OK)

    def testVerbose(self):
        rep = RegexProcessor()
        rep.setMatchString('10.3')

        rep.setVerboseFlag(False)
        rep.setRegexString(r'\d+\.\d*')
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_OK)

        rep.setVerboseFlag(False)
        rep.setRegexString(r"""
                   \d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""")
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_FAIL)

        rep.setVerboseFlag(True)
        rep.setRegexString(r"""
                   \d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""")
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_OK)

        rep.setVerboseFlag(False)
        rep.setRegexString(r"""(?x)
                   \d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""")
        self.assertTrue(rep._verboseFlagEmbedded)
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_OK)

    def testAscii(self):
        rep = RegexProcessor()
        rep.setMatchString('fox:αλεπού')

        rep.setAsciiFlag(False)
        rep.setRegexString(r'\w+')
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_OK)
        spans = rep.getAllSpans()
        self.assertEqual(len(spans), 2)  # find ['fox', 'αλεπού']

        rep.setAsciiFlag(True)
        rep.setRegexString(r'\w+')
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_OK)
        spans = rep.getAllSpans()
        self.assertEqual(len(spans), 1)  # find ['fox'] only

        rep.setAsciiFlag(False)
        rep.setRegexString(r'(?a)\w+')
        self.assertTrue(rep._asciiFlagEmbedded)
        status, __ = rep.getStatus()
        self.assertEqual(status, MATCH_OK)
        spans = rep.getAllSpans()
        self.assertEqual(len(spans), 1)  # find ['fox'] only

    def testPause(self):
        rep = RegexProcessor()
        rep.statusChanged.connect(self.statusChanged)

        self.resetStatusChanged()
        rep.setMatchString('matchString')
        self.assertStatusChanged()

        self.resetStatusChanged()
        rep.pause()
        rep.setMatchString('anotherMatchString')
        self.assertStatusNotChanged()
        rep.unpause()
        self.assertStatusChanged()

    def testExamine(self):
        rep = RegexProcessor()
        rep.setMatchString('123456789')

        rep.setRegexString('1222222345')
        matching, dontmatching = rep.examine()
        self.assertEqual(matching, '12')
        self.assertEqual(dontmatching, '22222345')

        rep.setRegexString('xxx')
        matching, dontmatching = rep.examine()
        self.assertEqual(matching, '')
        self.assertEqual(dontmatching, 'xxx')

        rep.setRegexString('')
        matching, dontmatching = rep.examine()
        self.assertEqual(matching, '')
        self.assertEqual(dontmatching, '')

        rep.setRegexString('(?P<n1>x)|(?P<n1>y)')  # invalid regex
        matching, dontmatching = rep.examine()
        self.assertEqual(matching, '(?P<n1>x)|')
        self.assertEqual(dontmatching, '(?P<n1>y)')

    def testEmbeddedFlags(self):
        rep = RegexProcessor()

        rep.setMatchString('abcdabc')
        rep.setRegexString('(?imsxa)')

        self.assertEqual('(?imsxa)', rep._getEmbeddedFlagsStr())

        self.assertEqual('imsxa', rep.getEmbeddedFlags())

        flagStr = ',  re.IGNORECASE | re.MULTILINE | re.DOTALL | re.VERBOSE | re.ASCII'
        self.assertEqual(flagStr, rep._getFlagsStr())

    def testGetRegexCode(self):
        rep = RegexProcessor()
        rep.statusChanged.connect(self.statusChanged)

        rep.setMatchString('Isaac Newton, physicist, Albert Einstein, physicist')
        rep.setRegexString(r'(?P<name>\w+) (?P<surname>\w+)')
        rep.setReplaceString('XXX')
        code = rep.getRegexCode()
        # Just a basic test
        self.assertTrue(code.index('Isaac Newton') > -1)
        self.assertTrue(code.index(r'(?P<name>\w+)') > -1)
        self.assertTrue(code.index('XXX') > -1)

    def testSet(self):
        rep = RegexProcessor()
        rep.statusChanged.connect(self.statusChanged)

        self.resetStatusChanged()
        rep.setRegexString('regexString')
        self.assertStatusChanged()

        self.resetStatusChanged()
        rep.setMatchString('matchString')
        self.assertStatusChanged()

        self.resetStatusChanged()
        rep.setReplaceString('replaceString')
        self.assertStatusChanged()

        self.resetStatusChanged()
        rep.setIgnorecaseFlag(True)
        self.assertStatusChanged()

        self.resetStatusChanged()
        rep.setMultilineFlag(True)
        self.assertStatusChanged()

        self.resetStatusChanged()
        rep.setDotallFlag(True)
        self.assertStatusChanged()

        self.resetStatusChanged()
        rep.setVerboseFlag(True)
        self.assertStatusChanged()

        self.resetStatusChanged()
        rep.setAsciiFlag(True)
        self.assertStatusChanged()

    def statusChanged(self):
        self._statusChanged = True

    def resetStatusChanged(self):
        self._statusChanged = False

    def assertStatusChanged(self):
        self.assertTrue(self._statusChanged, "Status didn't change as expected.")

    def assertStatusNotChanged(self):
        self.assertFalse(self._statusChanged, "Status unexpectedly changed.")
