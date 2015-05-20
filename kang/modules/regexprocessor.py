class RegexProcessor:

    def __init__(self):
        self._regexString = ''
        self._matchString = ''
        self._replaceString = ''

        self._ignorecaseFlag = False
        self._multilineFlag = False
        self._dotallFlag = False
        self._verboseFlag = False
        self._localeFlag = False
        self._unicodeFlag = False

        self._regexEmbeddedFlagsRemoved = ''
        self._groupTuples = False

    def setRegexString(self, regexString):
        self._regexString = regexString

    def setMatchString(self, matchString):
        self._matchString = matchString

    def setReplaceString(self, replaceString):
        self._replaceString = replaceString

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
            for grp in self.groupTuples:
                i += 1
                code += 'group_%d = match_obj.group(%d)\n' % (i, i)
                if grp[1]:
                    named_grps = 1

            if named_grps:
                code += '\n# Retrieve group(s) by name\n'
                for grp in self.groupTuples:
                    if grp[1]:
                        code += '%s = match_obj.group("%s")\n' % (grp[1], grp[1])

            code += '\n'

        if self._replaceString:
            code += '# Replace string\n'
            code += 'newstr = compile_obj.subn("%s", matchstr)\n' % self._replaceString

        return code
