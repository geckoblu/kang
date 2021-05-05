import pickle


class KngFile:
    """Used to handle Kang file prject"""

    def __init__(self, filename, regex='', matchstring='', replace='', flags=0):

        self.filename = filename

        self.regex = regex
        self.matchstring = matchstring
        self.flags = flags
        self.replace = replace

    def save(self):
        """Save Kang project to file"""
        with open(self.filename, 'wb') as fp:
            fp = pickle.Pickler(fp)
            fp.dump(self.regex)
            fp.dump(self.matchstring)
            fp.dump(self.flags)
            fp.dump(self.replace)

    def load(self):
        """Load Kang project from file"""
        with open(self.filename, 'rb') as fp:
            u = pickle.Unpickler(fp)
            self.regex = u.load()
            self.matchstring = u.load()
            self.flags = u.load()
            self.replace = u.load()
