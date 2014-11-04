import cPickle


class KngFile:

    def __init__(self, filename, regex='', matchstring='', replace='', flags=0):

        self.filename = filename

        self.regex = regex
        self.matchstring = matchstring
        self.flags = flags
        self.replace = replace

    def save(self):
        fp = open(self.filename, "w")

        p = cPickle.Pickler(fp)
        p.dump(self.regex)
        p.dump(self.matchstring)
        p.dump(self.flags)
        p.dump(self.replace)

        fp.close()

    def load(self):

        fp = open(self.filename, 'r')

        u = cPickle.Unpickler(fp)
        self.regex = u.load()
        self.matchstring = u.load()
        self.flags = u.load()

        try:
            self.replace = u.load()
        except:
            # versions prior to 1.7 did not have replace functionality
            # so kds files saved w/ these versions will throw exception
            # here.
            self.replace = ""

        fp.close()
