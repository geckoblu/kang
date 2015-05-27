from PyQt4.QtCore import pyqtSignal, QObject
import difflib
import re

from kang import MATCH_NA, MSG_NA, MATCH_FAIL, MSG_FAIL, MSG_MATCH_FOUND, MATCH_OK, MSG_MATCHES_FOUND


EMBEDDED_FLAGS = r'^ *\(\?(?P<flags>[iLmsux]*)\)'


class RegexProcessor(QObject):

    _statusSignal = pyqtSignal()

    def __init__(self):
        super(RegexProcessor, self).__init__()

        self._regexString = ''
        self._matchString = ''
        self._replaceString = ''

        self._flags = 0
        self._ignorecaseFlag = False
        self._multilineFlag = False
        self._dotallFlag = False
        self._verboseFlag = False
        self._localeFlag = False
        self._unicodeFlag = False

        self._status = (MATCH_NA, MSG_NA)

        self._groupTuples = []
        self._spans = []
        self._embeddedFlagsObj = re.compile(EMBEDDED_FLAGS)
        self._embeddedFlags = ''
        self._regexEmbeddedFlagsRemoved = ''
        self._ignorecaseFlagEmbedded = False
        self._multilineFlagEmbedded = False
        self._dotallFlagEmbedded = False
        self._verboseFlagEmbedded = False
        self._localeFlagEmbedded = False
        self._unicodeFlagEmbedded = False

        self._paused = False

    def setRegexString(self, regexString):
        old = self._regexString
        self._regexString = unicode(regexString)
        if regexString != old:
            self._process()

    def setMatchString(self, matchString):
        old = self._matchString
        self._matchString = unicode(matchString)
        if matchString != old:
            self._process()

    def setReplaceString(self, replaceString):
        old = self._replaceString
        self._replaceString = unicode(replaceString)
        if replaceString != old:
            self._process()

    def setIgnorecaseFlag(self, flag):
        old = self._ignorecaseFlag
        self._ignorecaseFlag = flag
        if flag != old:
            self._setFlags()
            self._process()

    def setMultilineFlag(self, flag):
        old = self._multilineFlag
        self._multilineFlag = flag
        if flag != old:
            self._setFlags()
            self._process()

    def setDotallFlag(self, flag):
        old = self._dotallFlag
        self._dotallFlag = flag
        if flag != old:
            self._setFlags()
            self._process()

    def setVerboseFlag(self, flag):
        old = self._verboseFlag
        self._verboseFlag = flag
        if flag != old:
            self._setFlags()
            self._process()

    def setLocaleFlag(self, flag):
        old = self._localeFlag
        self._localeFlag = flag
        if flag != old:
            self._setFlags()
            self._process()

    def setUnicodeFlag(self, flag):
        old = self._unicodeFlag
        self._unicodeFlag = flag
        if flag != old:
            self._setFlags()
            self._process()

    def _setFlags(self):
        self._flags = 0

        if self._ignorecaseFlag:
            self._flags = self._flags + re.IGNORECASE

        if self._multilineFlag:
            self._flags = self._flags + re.MULTILINE

        if self._dotallFlag:
            self._flags = self._flags + re.DOTALL

        if self._verboseFlag:
            self._flags = self._flags + re.VERBOSE

        if self._localeFlag:
            self._flags = self._flags + re.LOCALE

        if self._unicodeFlag:
            self._flags = self._flags + re.UNICODE

    def pause(self):
        self._paused = True

    def unpause(self):
        old = self._paused
        self._paused = False
        if old == True:
            self._process()

    def connect(self, slot):
        self._statusSignal.connect(slot)

    def getStatus(self):
        return self._status

    def getAllSpans(self):
        return self._spans

    def getSpan(self, index):
        try:
            return self._spans[index]
        except IndexError:
            return None

    def getGroups(self, index):
        try:
            return self._groupTuples[index]
        except IndexError:
            return []

    def getEmbeddedFlags(self):
        return self._embeddedFlags

    def _process(self):

        if self._paused:
            return

        # print('rp_process')

        self._spans = []
        self._groupTuples = []

        self._processEmbeddedFlags()

        if not self._regexString or not self._matchString:
            self._status = (MATCH_NA, MSG_NA)
            self._statusSignal.emit()
            return

        try:
            compileObj = re.compile(self._regexString, self._flags)
            matches = compileObj.finditer(self._matchString)
        except re.error as ex:
            self._status = (MATCH_FAIL, str(ex))
            self._statusSignal.emit()
            return

        # compileObj.groupindex is a dictionary mapping group name to group number
        # groupname is a dictionary mapping group number to group name
        groupname = {}
        if compileObj.groupindex:
            keys = compileObj.groupindex.keys()
            for key in keys:
                groupname[compileObj.groupindex[key]] = key

        for match in matches:
            start = match.start()
            end = match.end()
            span = (start, end)

            self._spans.append(span)

            gs = []
            g = match.groups('')
            for i in range(len(g)):
                gt = (i + 1, groupname.get(i + 1, ''), g[i])
                gs.append(gt)
            if gs:
                self._groupTuples.append(gs)

        found = len(self._spans)
        if found == 0:
            self._status = (MATCH_FAIL, MSG_FAIL)
        elif found == 1:
            msg = MSG_MATCH_FOUND
            self._status = (MATCH_OK, msg)
        else:
            msg = MSG_MATCHES_FOUND % len(self._spans)
            self._status = (MATCH_OK, msg)

        self._statusSignal.emit()

    def _processEmbeddedFlags(self):

        self._ignorecaseFlagEmbedded = False
        self._multilineFlagEmbedded = False
        self._dotallFlagEmbedded = False
        self._verboseFlagEmbedded = False
        self._localeFlagEmbedded = False
        self._unicodeFlagEmbedded = False

        match = self._embeddedFlagsObj.match(self._regexString)
        if not match:
            self._embeddedFlags = ''
            self._regexEmbeddedFlagsRemoved = self._regexString
            return

        self._embeddedFlags = match.group('flags')
        self._regexEmbeddedFlagsRemoved = self._embeddedFlagsObj.sub('', self._regexString, 1)

        for flag in self._embeddedFlags:
            if flag == 'i':
                self._ignorecaseFlagEmbedded = True
            elif flag == 'L':
                self._localeFlagEmbedded = True
            elif flag == 'm':
                self._multilineFlagEmbedded = True
            elif flag == 's':
                self._dotallFlagEmbedded = True
            elif flag == 'u':
                self._unicodeFlagEmbedded = True
            elif flag == 'x':
                self._verboseFlagEmbedded = True

    def replace(self, count):
        try:
            replaced = re.sub(self._regexString, self._replaceString, self._matchString, count)
        except re.error as ex:
            return (MATCH_FAIL, str(ex))

        strings = []
        seq = difflib.SequenceMatcher(None, unicode(self._matchString), replaced)
        for _, _, _, j1, j2 in seq.get_opcodes():
            strings.append(replaced[j1:j2])

        return (MATCH_OK, strings)

    def examine(self):
        regex = self._regexString
        regexSaved = self._regexString
        length = len(regex)

        for i in range(length, 0, -1):
            regex = regex[:i]
            try:
                m = re.search(regex, self._matchString, self._flags)
                if m:
                    return (regexSaved, regex)
            except re.error:
                pass

        return (regexSaved, '')

    def _getFlagsStr(self):
        flagsStr = ''

        if self._ignorecaseFlag:
            flagsStr += '| re.IGNORECASE '

        if self._multilineFlag:
            flagsStr += '| re.MULTILINE '

        if self._dotallFlag:
            flagsStr += '| re.DOTALL '

        if self._verboseFlag:
            flagsStr += '| re.VERBOSE '

        if self._localeFlag:
            flagsStr += '| re.LOCALE '

        if self._unicodeFlag:
            flagsStr += '| re.UNICODE'

        if flagsStr:
            flagsStr = ', ' + flagsStr[1:]

        return flagsStr

    def _getEmbeddedFlagsStr(self):
        flags = ''

        if self._ignorecaseFlag:
            flags += 'i'

        if self._multilineFlag:
            flags += 'm'

        if self._dotallFlag:
            flags += 's'

        if self._verboseFlag:
            flags += 'x'

        if self._localeFlag:
            flags += 'L'

        if self._unicodeFlag:
            flags += 'u'

        if flags:
            flagsStr = '(?' + flags + ')'
        else:
            flagsStr = ''

        return flagsStr

    def getRegexCode(self):

        code = 'import re\n\n'
        code += '# common variables\n\n'
        code += 'rawstr = r"""' + self._regexEmbeddedFlagsRemoved + '"""\n'
        code += 'embedded_rawstr = r"""' + self._getEmbeddedFlagsStr() + \
                self._regexEmbeddedFlagsRemoved + '"""\n'
        code += 'matchstr = \"\"\"' + self._matchString + '\"\"\"'
        code += '\n\n'
        code += '# method 1: using a compile object\n'
        code += 'compile_obj = re.compile(rawstr'
        code += self._getFlagsStr()
        code += ')\n'
        code += 'match_obj = compile_obj.search(matchstr)\n\n'

        code += '# method 2: using search function (w/ external flags)\n'
        code += 'match_obj = re.search(rawstr, matchstr'
        code += self._getFlagsStr()
        code += ')\n\n'

        code += '# method 3: using search function (w/ embedded flags)\n'
        code += 'match_obj = re.search(embedded_rawstr, matchstr)\n\n'

        if self._groupTuples:
            code += '# Retrieve group(s) from match_obj\n'
            code += 'all_groups = match_obj.groups()\n\n'
            code += '# Retrieve group(s) by index\n'
            i = 0
            named_grps = 0
            for grp in self._groupTuples[0]:
                i += 1
                code += 'group_%d = match_obj.group(%d)\n' % (i, i)
                if grp[1]:
                    named_grps = 1

            if named_grps:
                code += '\n# Retrieve group(s) by name\n'
                for grp in self._groupTuples[0]:
                    if grp[1]:
                        code += '%s = match_obj.group("%s")\n' % (grp[1], grp[1])

            code += '\n'

        if self._replaceString:
            code += '# Replace string\n'
            code += 'newstr = compile_obj.subn("%s", matchstr)\n' % self._replaceString

        return code
