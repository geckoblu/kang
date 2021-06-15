import json
import pickle
import re


class KngFile:
    """Used to handle Kang file project"""

    def __init__(
            self,
            filename,
            matchString='',
            regexString='',
            replaceString='',
            flagIgnorecase=False,
            flagMultiline=False,
            flagDotall=False,
            flagVerbose=False,
            flagAscii=False
        ):

        self._filename = filename

        self.matchString = matchString
        self.regexString = regexString
        self.replaceString = replaceString

        self.flagIgnorecase = flagIgnorecase
        self.flagMultiline = flagMultiline
        self.flagDotall = flagDotall
        self.flagVerbose = flagVerbose
        self.flagAscii = flagAscii

    def save(self):
        """Saves Kang project to file"""

        jdict = {}

        jdict['match_string'] = self.matchString
        jdict['regex_string'] = self.regexString
        jdict['replace_string'] = self.replaceString

        jdict['flag_ignorecase'] = self.flagIgnorecase
        jdict['flag_multiline'] = self.flagMultiline
        jdict['flag_dotall'] = self.flagDotall
        jdict['flag_verbose'] = self.flagVerbose
        jdict['flag_ascii'] = self.flagAscii

        with open(self._filename, 'w') as jfile:
            json.dump(jdict, jfile, indent=4)

    def load(self):
        """Loads Kang project from file"""
        try:
            with open(self._filename, 'r') as jfile:
                jdict = json.load(jfile)

            self.matchString = jdict.get('match_string', '')
            self.regexString = jdict.get('regex_string', '')
            self.replaceString = jdict.get('replace_string', '')

            self.flagIgnorecase = jdict.get('flag_ignorecase', False)
            self.flagMultiline = jdict.get('flag_multiline', False)
            self.flagDotall = jdict.get('flag_dotall', False)
            self.flagVerbose = jdict.get('flag_verbose', False)
            self.flagAscii = jdict.get('flag_ascii', False)

        except json.decoder.JSONDecodeError as jsonexception:
            try:
                # Try to load an old pickler version
                self._loadPickler()
            except:
                raise jsonexception

    def _loadPickler(self):
        """Loads Kang project from file (old version using pickle)"""
        with open(self._filename, 'rb') as picklerfile:
            unpickler = pickle.Unpickler(picklerfile)
            self.regexString = unpickler.load()
            self.matchString = unpickler.load()
            flags = unpickler.load()
            self.replaceString = unpickler.load()

            self.flagIgnorecase = bool(flags & re.IGNORECASE)
            self.flagMultiline = bool(flags & re.MULTILINE)
            self.flagDotall = bool(flags & re.DOTALL)
            self.flagVerbose = bool(flags & re.VERBOSE)

#    Deprecated
#    def _savePickler(self):
#        """Save Kang project to file (old version using pickle)"""
#        with open(self._filename, 'wb') as picklerfile:
#            pickler = pickle.Pickler(picklerfile)
#            pickler.dump(self.regexString)
#            pickler.dump(self.matchString)
#            pickler.dump(self.flags)
#            pickler.dump(self.replaceString)
