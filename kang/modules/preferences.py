import os
import string
import sys

from kang.modules.util import getConfigDirectory


class Preferences:

    def __init__(self):
        prefsFilename = "prefs"
        self.prefsPath = os.path.join(getConfigDirectory(), prefsFilename)

        self.defaultRecentFilesNum = 5

        self.recentFilesNum = self.defaultRecentFilesNum

        self.load()

    def load(self):
        try:
            fp = open(self.prefsPath, "r")
        except:
            return

        prefsList = fp.readlines()
        for pref in prefsList:
            if ':' in pref:
                preference, setting = string.split(pref, ":", 1)
                setting = string.strip(setting)
                if preference == 'Recent Files' and setting:
                    self.recentFilesNum = int(setting)

    def save(self):
        try:
            fp = open(self.prefsPath, "w")
        except:
            sys.stderr.write("Could not save preferences: %s\n" & self.prefsPath)
            return

        # Recent Files
        if self.recentFilesNum != self.defaultRecentFilesNum:
            fp.write("Recent Files: %s\n" % str(self.recentFilesNum))

        fp.close()
