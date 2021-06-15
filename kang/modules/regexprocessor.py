import re

from PySide2.QtCore import QObject, Signal

from kang import MATCH_NA, MSG_NA, MATCH_FAIL, MSG_FAIL, MSG_MATCH_FOUND, MATCH_OK, MSG_MATCHES_FOUND

EMBEDDED_FLAGS = r'^ *\(\?(?P<flags>[imsaxLu]*)\)'


class RegexProcessor(QObject):

    statusChanged = Signal()

    def __init__(self):
        super(RegexProcessor, self).__init__()

        self._matchString = ''
        self._regexString = ''
        self._replaceString = ''

        self._ignorecaseFlag = False
        self._multilineFlag = False
        self._dotallFlag = False
        self._verboseFlag = False
        self._asciiFlag = False

        self._status = (MATCH_NA, MSG_NA)

        self._groupTuples = []
        self._spans = []

        self._embeddedFlagsObj = re.compile(EMBEDDED_FLAGS)
        self._embeddedFlags = ''
        self._regexStringEFR = ''
        self._ignorecaseFlagEmbedded = False
        self._multilineFlagEmbedded = False
        self._dotallFlagEmbedded = False
        self._verboseFlagEmbedded = False
        self._asciiFlagEmbedded = False

        self._paused = False

    def setRegexString(self, regexString):
        """Sets regexString string"""
        old = self._regexString
        self._regexString = regexString
        if regexString != old:
            self._process()

    def setMatchString(self, matchString):
        """Sets matchString string"""
        old = self._matchString
        self._matchString = matchString
        if matchString != old:
            self._process()

    def setReplaceString(self, replaceString):
        """Sets replaceString string"""
        old = self._replaceString
        self._replaceString = replaceString
        if replaceString != old:
            self._process()

    def setIgnorecaseFlag(self, flag):
        """Sets ignore case flag"""
        old = self._ignorecaseFlag
        self._ignorecaseFlag = flag
        if flag != old:
            self._process()

    def setMultilineFlag(self, flag):
        """Sets multi line flag"""
        old = self._multilineFlag
        self._multilineFlag = flag
        if flag != old:
            self._process()

    def setDotallFlag(self, flag):
        """Sets dot all flag"""
        old = self._dotallFlag
        self._dotallFlag = flag
        if flag != old:
            self._process()

    def setVerboseFlag(self, flag):
        """Sets verbose flag"""
        old = self._verboseFlag
        self._verboseFlag = flag
        if flag != old:
            self._process()

    def setAsciiFlag(self, flag):
        """Sets ascii flag"""
        old = self._asciiFlag
        self._asciiFlag = flag
        if flag != old:
            self._process()

    def pause(self):
        """Pauses processing"""
        self._paused = True

    def unpause(self):
        """Unpauses processing"""
        waspaused = self._paused
        self._paused = False
        if waspaused:
            self._process()

    def getStatus(self):
        """Returns the current status"""
        return self._status

    def getAllSpans(self):
        """Returns all spans"""
        return self._spans

    def getSpan(self, index):
        """Return span at index"""
        return self._spans[index]

    def getAllGroups(self):
        """Returns all groups"""
        return self._groupTuples

    def getEmbeddedFlags(self):
        """Returns embedded flags"""
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
            self.statusChanged.emit()
            return

        try:
            compileObj = re.compile(self._regexStringEFR, self._flags())
            matches = compileObj.finditer(self._matchString)
        except re.error as ex:
            self._status = (MATCH_FAIL, str(ex))
            self.statusChanged.emit()
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
            for i, g in enumerate(match.groups(''), 1):
                gt = (i, groupname.get(i, ''), g)
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

        self.statusChanged.emit()

    def _flags(self):
        flags = 0

        if self._ignorecaseFlag or self._ignorecaseFlagEmbedded:
            flags = flags + re.IGNORECASE

        if self._multilineFlag or self._multilineFlagEmbedded:
            flags = flags + re.MULTILINE

        if self._dotallFlag or self._dotallFlagEmbedded:
            flags = flags + re.DOTALL

        if self._verboseFlag or self._verboseFlagEmbedded:
            flags = flags + re.VERBOSE

        if self._asciiFlag or self._asciiFlagEmbedded:
            flags = flags + re.ASCII

        return flags

    def _processEmbeddedFlags(self):

        self._ignorecaseFlagEmbedded = False
        self._multilineFlagEmbedded = False
        self._dotallFlagEmbedded = False
        self._verboseFlagEmbedded = False
        self._asciiFlagEmbedded = False

        match = self._embeddedFlagsObj.match(self._regexString)
        if not match:
            self._embeddedFlags = ''
            self._regexStringEFR = self._regexString
            return

        self._embeddedFlags = match.group('flags')
        self._regexStringEFR = self._embeddedFlagsObj.sub('', self._regexString, 1)

        for flag in self._embeddedFlags:
            if flag == 'i':
                self._ignorecaseFlagEmbedded = True
            elif flag == 'm':
                self._multilineFlagEmbedded = True
            elif flag == 's':
                self._dotallFlagEmbedded = True
            elif flag == 'x':
                self._verboseFlagEmbedded = True
            elif flag == 'a':
                self._asciiFlagEmbedded = True

    def replace(self, count):
        try:
            replaced = re.sub(self._regexString, self._replaceString, self._matchString, count)
        except re.error as ex:
            return (MATCH_FAIL, str(ex))

        strings = []
        # TODO: I couldn't define which is the correct behavior so I disable it completely
        # seq = difflib.SequenceMatcher(None, self._matchString, replaced, None)
        # for _, _, _, j1, j2 in seq.get_opcodes():
        #    strings.append(replaced[j1:j2])
        strings.append(replaced)

        return (MATCH_OK, strings)

    def examine(self):

        regex = self._regexStringEFR
        length = len(regex)

        for i in range(length, 0, -1):
            regex = regex[:i]
            try:
                match = re.search(regex, self._matchString, self._flags())
                if match:
                    return (regex, self._regexString[len(regex):])
            except re.error:
                pass

        return ('', self._regexString)

    def getRegexCode(self):
        """Returns the python code for the current regex"""

        code = 'import re\n\n'

        code += '# common variables\n\n'
        code += 'rawstr = r"""' + self._regexStringEFR + '"""\n\n'
        code += 'embedded_rawstr = r"""' + self._getEmbeddedFlagsStr() + \
                self._regexStringEFR + '"""\n\n'
        code += 'matchstr = """' + self._matchString + '"""\n\n'
        if self._replaceString:
            code += 'replacestr = r"""' + self._replaceString + '"""\n\n'
        code += '\n'

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
            namedGrps = 0
            for grp in self._groupTuples[0]:
                i += 1
                code += 'group_%d = match_obj.group(%d)\n' % (i, i)
                if grp[1]:
                    namedGrps = 1

            if namedGrps:
                code += '\n# Retrieve group(s) by name\n'
                for grp in self._groupTuples[0]:
                    if grp[1]:
                        code += '%s = match_obj.group("%s")\n' % (grp[1], grp[1])

            code += '\n'

        if self._replaceString:
            code += '# Replace string\n'
            code += 'newstr = compile_obj.subn(replacestr, matchstr)\n'

        return code

    def _getFlagsStr(self):
        flagsStr = ''

        if self._ignorecaseFlag or self._ignorecaseFlagEmbedded:
            flagsStr += '| re.IGNORECASE '

        if self._multilineFlag or self._multilineFlagEmbedded:
            flagsStr += '| re.MULTILINE '

        if self._dotallFlag or self._dotallFlagEmbedded:
            flagsStr += '| re.DOTALL '

        if self._verboseFlag or self._verboseFlagEmbedded:
            flagsStr += '| re.VERBOSE '

        if self._asciiFlag or self._asciiFlagEmbedded:
            flagsStr += '| re.ASCII'

        if flagsStr:
            flagsStr = ', ' + flagsStr[1:]

        return flagsStr

    def _getEmbeddedFlagsStr(self):
        flags = ''

        if self._ignorecaseFlag or self._ignorecaseFlagEmbedded:
            flags += 'i'

        if self._multilineFlag or self._multilineFlagEmbedded:
            flags += 'm'

        if self._dotallFlag or self._dotallFlagEmbedded:
            flags += 's'

        if self._verboseFlag or self._verboseFlagEmbedded:
            flags += 'x'

        if self._asciiFlag or self._asciiFlagEmbedded:
            flags += 'a'

        if flags:
            flagsStr = '(?' + flags + ')'
        else:
            flagsStr = ''

        return flagsStr
