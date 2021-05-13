import json
import pickle
import re


class KngFile:
    """Used to handle Kang file prject"""

    def __init__(
            self, filename,
            match_string='',
            regex_string='',
            replace_string='',
            flag_ignorecase=False,
            flag_multiline=False,
            flag_dotall=False,
            flag_verbose=False,
            flag_unicode=False
        ):

        self.filename = filename

        self.match_string = match_string
        self.regex_string = regex_string
        self.replace_string = replace_string

        self.flag_ignorecase = flag_ignorecase
        self.flag_multiline = flag_multiline
        self.flag_dotall = flag_dotall
        self.flag_verbose = flag_verbose
        self.flag_unicode = flag_unicode

    def save(self):
        """Save Kang project to file"""

        jdict = {}

        jdict['match_string'] = self.match_string
        jdict['regex_string'] = self.regex_string
        jdict['replace_string'] = self.replace_string

        jdict['flag_ignorecase'] = self.flag_ignorecase
        jdict['flag_multiline'] = self.flag_multiline
        jdict['flag_dotall'] = self.flag_dotall
        jdict['flag_verbose'] = self.flag_verbose
        jdict['flag_unicode'] = self.flag_unicode

        with open(self.filename, 'w') as jfile:
            json.dump(jdict, jfile, indent=4)

    def load(self):
        try:
            with open(self.filename, 'r') as jfile:
                jdict = json.load(jfile)

            self.match_string = jdict.get('match_string', '')
            self.regex_string = jdict.get('regex_string', '')
            self.replace_string = jdict.get('replace_string', '')

            self.flag_ignorecase = jdict.get('flag_ignorecase', False)
            self.flag_multiline = jdict.get('flag_multiline', False)
            self.flag_dotall = jdict.get('flag_dotall', False)
            self.flag_verbose = jdict.get('flag_verbose', False)
            self.flag_unicode = jdict.get('flag_unicode', False)

        except json.decoder.JSONDecodeError as jsonexception:
            try:
                # Try to load an old pickler version
                self._load_pickler()
            except:
                raise jsonexception

    def _load_pickler(self):
        """Load Kang project from file (old version using pickle)"""
        with open(self.filename, 'rb') as picklerfile:
            unpickler = pickle.Unpickler(picklerfile)
            self.regex_string = unpickler.load()
            self.match_string = unpickler.load()
            flags = unpickler.load()
            self.replace_string = unpickler.load()

            self.flag_ignorecase = bool(flags & re.IGNORECASE)
            self.flag_multiline = bool(flags & re.MULTILINE)
            self.flag_dotall = bool(flags & re.DOTALL)
            self.flag_verbose = bool(flags & re.VERBOSE)
            self.flag_locale = bool(flags & re.LOCALE)
            self.flag_unicode = bool(flags & re.UNICODE)

#    Deprecated
#    def _save_pickler(self):
#        """Save Kang project to file (old version using pickle)"""
#        with open(self.filename, 'wb') as picklerfile:
#            pickler = pickle.Pickler(picklerfile)
#            pickler.dump(self.regex_string)
#            pickler.dump(self.match_string)
#            pickler.dump(self.flags)
#            pickler.dump(self.replace_string)


if __name__ == "__main__":
    import sys
    print(sys.argv)

    filename = sys.argv[1]

    kng = KngFile(filename)
    kng._load_pickler()
    kng.save()
