# pylint: disable=protected-access,missing-function-docstring

import unittest

from kang.modules.regexprocessor import RegexProcessor, MATCH_OK, MATCH_NA, MATCH_FAIL


class TestRegexProcessor(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestRegexProcessor, self).__init__(*args, **kwargs)
        self._statusChanged = False

    def testMatch(self):
        rp = RegexProcessor()
        rp.statusChanged.connect(self.statusChanged)

        rp.setMatchString('La donzelletta vien dalla campagna e vien in compagnia di rose e viole')
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_NA)

        # Three matches
        self.resetStatusChanged()
        rp.setRegexString('v')
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)
        spans = rp.getAllSpans()
        self.assertEqual(len(spans), 3)
        self.assertEqual(spans, [(15, 16), (37, 38), (65, 66)])
        self.assertEqual(rp.getSpan(1), (37, 38))
        self.assertEqual(len(rp._groupTuples), 0)
        self.assertStatusChanged()

        # Two matches
        self.resetStatusChanged()
        rp.setRegexString('vien')
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)
        spans = rp.getAllSpans()
        self.assertEqual(len(spans), 2)
        self.assertEqual(spans, [(15, 19), (37, 41)])
        self.assertEqual(len(rp._groupTuples), 0)
        self.assertStatusChanged()

        # No matches
        self.resetStatusChanged()
        rp.setRegexString('xxx')
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_FAIL)
        spans = rp.getAllSpans()
        self.assertEqual(len(spans), 0)
        self.assertEqual(spans, [])
        self.assertEqual(len(rp._groupTuples), 0)
        self.assertStatusChanged()

    def testGroups(self):
        rp = RegexProcessor()
        rp.statusChanged.connect(self.statusChanged)

        rp.setMatchString('La donzelletta vien dalla campagna e vien in compagnia di rose e viole')
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_NA)

        # One group, two matches
        self.resetStatusChanged()
        rp.setRegexString('(vien)')
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)
        spans = rp.getAllSpans()
        self.assertEqual(len(spans), 2)
        self.assertEqual(spans, [(15, 19), (37, 41)])
        self.assertEqual(len(rp._groupTuples), 2)
        groups = rp.getAllGroups()
        self.assertEqual(groups[0], [(1, '', 'vien')])
        self.assertEqual(groups[1], [(1, '', 'vien')])
        self.assertStatusChanged()

        # Two groups, three matches
        self.resetStatusChanged()
        rp.setRegexString('(vien)|(gna)')
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)
        spans = rp.getAllSpans()
        self.assertEqual(len(spans), 3)
        self.assertEqual(spans, [(15, 19), (31, 34), (37, 41)])
        self.assertEqual(len(rp._groupTuples), 3)
        groups = rp.getAllGroups()
        self.assertEqual(groups[0], [(1, '', 'vien'), (2, '', '')])
        self.assertEqual(groups[1], [(1, '', ''), (2, '', 'gna')])
        self.assertEqual(groups[2], [(1, '', 'vien'), (2, '', '')])
        self.assertStatusChanged()

        # Two groups (one named), three matches
        self.resetStatusChanged()
        rp.setRegexString('(?P<n1>vien)|(gna)')
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)
        spans = rp.getAllSpans()
        self.assertEqual(len(spans), 3)
        self.assertEqual(spans, [(15, 19), (31, 34), (37, 41)])
        self.assertEqual(len(rp._groupTuples), 3)
        groups = rp.getAllGroups()
        self.assertEqual(groups[0], [(1, 'n1', 'vien'), (2, '', '')])
        self.assertEqual(groups[1], [(1, 'n1', ''), (2, '', 'gna')])
        self.assertEqual(groups[2], [(1, 'n1', 'vien'), (2, '', '')])
        self.assertStatusChanged()

        # Two groups (both named), three matches
        self.resetStatusChanged()
        rp.setRegexString('(?P<n1>vien)|(?P<n2>gna)')
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)
        spans = rp.getAllSpans()
        self.assertEqual(len(spans), 3)
        self.assertEqual(spans, [(15, 19), (31, 34), (37, 41)])
        self.assertEqual(len(rp._groupTuples), 3)
        groups = rp.getAllGroups()
        self.assertEqual(groups[0], [(1, 'n1', 'vien'), (2, 'n2', '')])
        self.assertEqual(groups[1], [(1, 'n1', ''), (2, 'n2', 'gna')])
        self.assertEqual(groups[2], [(1, 'n1', 'vien'), (2, 'n2', '')])
        self.assertStatusChanged()

        # Two groups (same name)
        self.resetStatusChanged()
        rp.setRegexString('(?P<n1>vien)|(?P<n1>gna)')
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_FAIL)
        self.assertStatusChanged()

        # One group plus one match
        self.resetStatusChanged()
        rp.setRegexString('(vien)|gna')
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)
        spans = rp.getAllSpans()
        self.assertEqual(len(spans), 3)
        self.assertEqual(spans, [(15, 19), (31, 34), (37, 41)])
        self.assertEqual(len(rp._groupTuples), 3)
        groups = rp.getAllGroups()
        self.assertEqual(groups[0], [(1, '', 'vien')])
        self.assertEqual(groups[1], [(1, '', '')])
        self.assertStatusChanged()

    def testReplace(self):
        rp = RegexProcessor()
        rp.setMatchString('abcdabcbc')

        # Normal match (2)
        rp.setRegexString('b')
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)
        rp.setReplaceString('x')
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)

        status, strings = rp.replace(1)
        self.assertEqual(status, MATCH_OK)
        self.assertEqual(strings, ['axcdabcbc'])

        status, strings = rp.replace(2)
        self.assertEqual(status, MATCH_OK)
        self.assertEqual(strings, ['axcdaxcbc'])

        status, strings = rp.replace(0)  # 0 stands for 'all'
        self.assertEqual(status, MATCH_OK)
        self.assertEqual(strings, ['axcdaxcxc'])

        status, strings = rp.replace(3)
        self.assertEqual(status, MATCH_OK)
        self.assertEqual(strings, ['axcdaxcxc'])

        status, strings = rp.replace(4)
        self.assertEqual(status, MATCH_OK)
        self.assertEqual(strings, ['axcdaxcxc'])

        # Group match (2)
        rp.setRegexString('(b)')
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)
        rp.setReplaceString('x')
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)

        status, strings = rp.replace(0)  # 0 stands for 'all'
        self.assertEqual(status, MATCH_OK)
        self.assertEqual(strings, ['axcdaxcxc'])

        rp.setReplaceString(r'x\1')
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)

        status, strings = rp.replace(0)  # 0 stands for 'all'
        self.assertEqual(status, MATCH_OK)
        self.assertEqual(strings, ['axbcdaxbcxbc'])

        rp.setReplaceString(r'x\2')
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)
        status, strings = rp.replace(0)  # 0 stands for 'all'
        self.assertEqual(status, MATCH_FAIL)
        self.assertEqual(strings, 'invalid group reference 2 at position 2')

        rp.setReplaceString('x\\')
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)
        status, strings = rp.replace(0)  # 0 stands for 'all'
        self.assertEqual(status, MATCH_FAIL)
        self.assertEqual(strings, 'bad escape (end of pattern) at position 1')

        # Real case - which would be the correct colorized ?
        rp.setMatchString("""<p><a class="calibre7" id="filepos48765"></a></p>
    <blockquote class="calibre19">
    <a class="calibre8" href="#filepos20421"><span class="calibre9 underline">1</span></a>
    </blockquote>""")
        rp.setRegexString("""<p><a class="calibre7" id="(.*?)"></a></p>
    <blockquote class="calibre19">
    <a class="calibre8" href="(.*?)"><span class="calibre9 underline">(.*?)</span></a>
    </blockquote>""")
        rp.setReplaceString(r'<a class="noteref" id="\1" href="\2">\3</a>')
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)
        status, strings = rp.replace(0)  # 0 stands for 'all'
        self.assertEqual(status, MATCH_OK)
        self.assertEqual(strings, ['<a class="noteref" id="filepos48765" href="#filepos20421">1</a>'])

    def testIgnorecase(self):
        rp = RegexProcessor()
        rp.setMatchString('Newton')

        rp.setIgnorecaseFlag(False)
        rp.setRegexString('newton')
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_FAIL)

        rp.setIgnorecaseFlag(True)
        rp.setRegexString('newton')
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)

        rp.setIgnorecaseFlag(False)
        rp.setRegexString('(?i)newton')
        self.assertTrue(rp._ignorecaseFlagEmbedded)
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)

    def testMultiline(self):
        rp = RegexProcessor()
        rp.setMatchString("""one
two""")

        rp.setMultilineFlag(False)
        rp.setRegexString('^two')
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_FAIL)

        rp.setMultilineFlag(True)
        rp.setRegexString('^two')
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)

        rp.setMultilineFlag(False)
        rp.setRegexString('(?m)^two')
        self.assertTrue(rp._multilineFlagEmbedded)
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)

    def testDotall(self):
        rp = RegexProcessor()
        rp.setMatchString("""one
two""")

        rp.setDotallFlag(False)
        rp.setRegexString('one.')
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_FAIL)

        rp.setDotallFlag(True)
        rp.setRegexString('one.')
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)

        rp.setDotallFlag(False)
        rp.setRegexString('(?s)one.')
        self.assertTrue(rp._dotallFlagEmbedded)
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)

    def testVerbose(self):
        rp = RegexProcessor()
        rp.setMatchString('10.3')

        rp.setVerboseFlag(False)
        rp.setRegexString(r'\d+\.\d*')
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)

        rp.setVerboseFlag(False)
        rp.setRegexString(r"""
                   \d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""")
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_FAIL)

        rp.setVerboseFlag(True)
        rp.setRegexString(r"""
                   \d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""")
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)

        rp.setVerboseFlag(False)
        rp.setRegexString(r"""(?x)
                   \d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""")
        self.assertTrue(rp._verboseFlagEmbedded)
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)

    def testAscii(self):
        rp = RegexProcessor()
        rp.setMatchString('fox:αλεπού')

        rp.setAsciiFlag(False)
        rp.setRegexString(r'\w+')
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)
        spans = rp.getAllSpans()
        self.assertEqual(len(spans), 2)  # find ['fox', 'αλεπού']

        rp.setAsciiFlag(True)
        rp.setRegexString(r'\w+')
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)
        spans = rp.getAllSpans()
        self.assertEqual(len(spans), 1)  # find ['fox'] only

        rp.setAsciiFlag(False)
        rp.setRegexString(r'(?a)\w+')
        self.assertTrue(rp._asciiFlagEmbedded)
        status, __ = rp.getStatus()
        self.assertEqual(status, MATCH_OK)
        spans = rp.getAllSpans()
        self.assertEqual(len(spans), 1)  # find ['fox'] only

    def testPause(self):
        rp = RegexProcessor()
        rp.statusChanged.connect(self.statusChanged)

        self.resetStatusChanged()
        rp.setMatchString('matchString')
        self.assertStatusChanged()

        self.resetStatusChanged()
        rp.pause()
        rp.setMatchString('anotherMatchString')
        self.assertStatusNotChanged()
        rp.unpause()
        self.assertStatusChanged()

    def testExamine(self):
        rp = RegexProcessor()
        rp.setMatchString('123456789')

        rp.setRegexString('1222222345')
        matching, dontmatching = rp.examine()
        self.assertEqual(matching, '12')
        self.assertEqual(dontmatching, '22222345')

        rp.setRegexString('xxx')
        matching, dontmatching = rp.examine()
        self.assertEqual(matching, '')
        self.assertEqual(dontmatching, 'xxx')

        rp.setRegexString('')
        matching, dontmatching = rp.examine()
        self.assertEqual(matching, '')
        self.assertEqual(dontmatching, '')

        rp.setRegexString('(?P<n1>x)|(?P<n1>y)')  # invalid regex
        matching, dontmatching = rp.examine()
        self.assertEqual(matching, '(?P<n1>x)|')
        self.assertEqual(dontmatching, '(?P<n1>y)')

    def testEmbeddedFlags(self):
        rp = RegexProcessor()

        rp.setMatchString('abcdabc')
        rp.setRegexString('(?imsxa)')

        self.assertEqual('(?imsxa)', rp._getEmbeddedFlagsStr())

        self.assertEqual('imsxa', rp.getEmbeddedFlags())

        flagStr = ',  re.IGNORECASE | re.MULTILINE | re.DOTALL | re.VERBOSE | re.ASCII'
        self.assertEqual(flagStr, rp._getFlagsStr())

    def testGetRegexCode(self):
        rp = RegexProcessor()
        rp.statusChanged.connect(self.statusChanged)

        rp.setMatchString('Isaac Newton, physicist, Albert Einstein, physicist')
        rp.setRegexString(r'(?P<name>\w+) (?P<surname>\w+)')
        rp.setReplaceString('XXX')
        code = rp.getRegexCode()
        # Just a basic test
        self.assertTrue(code.index('Isaac Newton') > -1)
        self.assertTrue(code.index(r'(?P<name>\w+)') > -1)
        self.assertTrue(code.index('XXX') > -1)

    def testSet(self):
        rp = RegexProcessor()
        rp.statusChanged.connect(self.statusChanged)

        self.resetStatusChanged()
        rp.setRegexString('regexString')
        self.assertStatusChanged()

        self.resetStatusChanged()
        rp.setMatchString('matchString')
        self.assertStatusChanged()

        self.resetStatusChanged()
        rp.setReplaceString('replaceString')
        self.assertStatusChanged()

        self.resetStatusChanged()
        rp.setIgnorecaseFlag(True)
        self.assertStatusChanged()

        self.resetStatusChanged()
        rp.setMultilineFlag(True)
        self.assertStatusChanged()

        self.resetStatusChanged()
        rp.setDotallFlag(True)
        self.assertStatusChanged()

        self.resetStatusChanged()
        rp.setVerboseFlag(True)
        self.assertStatusChanged()

        self.resetStatusChanged()
        rp.setAsciiFlag(True)
        self.assertStatusChanged()

    def statusChanged(self):
        self._statusChanged = True

    def resetStatusChanged(self):
        self._statusChanged = False

    def assertStatusChanged(self):
        self.assertTrue(self._statusChanged, "Status didn't change as expected.")

    def assertStatusNotChanged(self):
        self.assertFalse(self._statusChanged, "Status unexpectedly changed.")
