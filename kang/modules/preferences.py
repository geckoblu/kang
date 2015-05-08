import os
import string
import sys

from kang.modules.util import getConfigDirectory


class Preferences:

    DEFAULTRECENTFILESNUM = 5
    ASKSAVE = True
    ASKSAVEONLYFORNAMEDPROJECTS = False

    def __init__(self):
        prefsFilename = "prefs"
        self.prefsPath = os.path.join(getConfigDirectory(), prefsFilename)

        self.recentFilesNum = self.DEFAULTRECENTFILESNUM
        self.askSave = self.ASKSAVE
        self.askSaveOnlyForNamedProjects = self.ASKSAVEONLYFORNAMEDPROJECTS

        self.load()

    def load(self):
        try:
            fp = open(self.prefsPath, "r")
        except:
            return

        prefsList = fp.readlines()
        for pref in prefsList:
            if ':' in pref:
                name, value = string.split(pref, ":", 1)
                value = string.strip(value)
                if value:
                    if name == 'Recent Files':
                        try:
                            self.recentFilesNum = int(value)
                        except ValueError:
                            self.recentFilesNum = self.DEFAULTRECENTFILESNUM
                    elif name == 'Ask save':
                        self.askSave = (value == 'True')
                    elif name == 'Ask save only for named projects':
                        self.askSaveOnlyForNamedProjects = (value == 'True')

    def save(self):
        try:
            fp = open(self.prefsPath, "w")
        except:
            #TODO: better error handling when no save preferences
            sys.stderr.write("Could not save preferences: %s\n" & self.prefsPath)
            return

        # Recent Files
        if self.recentFilesNum != self.DEFAULTRECENTFILESNUM:
            fp.write('Recent Files: %s\n' % str(self.recentFilesNum))
        if self.askSave != self.ASKSAVE:
            fp.write('Ask save: %s\n' % str(self.askSave))
        if self.askSaveOnlyForNamedProjects != self.ASKSAVEONLYFORNAMEDPROJECTS:
            fp.write('Ask save only for named projects: %s\n' % str(self.askSaveOnlyForNamedProjects))

        fp.close()
