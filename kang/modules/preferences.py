import os
import string
import sys

from kang.modules.util import getConfigDirectory


class Preferences:
    """Used to handle Kang preferences.
       Stores/load them to file.
    """

    _DEFAULTRECENTFILESNUM = 5
    _ASKSAVE = True
    _ASKSAVEONLYFORNAMEDPROJECTS = False

    def __init__(self):
        self._prefsPath = os.path.join(getConfigDirectory(), 'prefs')

        self.recentFilesNum = self._DEFAULTRECENTFILESNUM
        self.askSave = self._ASKSAVE
        self.askSaveOnlyForNamedProjects = self._ASKSAVEONLYFORNAMEDPROJECTS

        self.load()

    def load(self):
        """Load preferences from file"""
        if not os.path.isfile(self._prefsPath):
            return

        try:
            with open(self._prefsPath, "r") as fp:
                prefsList = fp.readlines()
        except IOError as ex:
            sys.stderr.write("Could not load preferences: %s\n" % str(ex))
            return

        for pref in prefsList:
            if ':' in pref:
                name, value = string.split(pref, ":", 1)
                value = string.strip(value)
                if value:
                    if name == 'Recent Files':
                        try:
                            self.recentFilesNum = int(value)
                        except ValueError:
                            self.recentFilesNum = self._DEFAULTRECENTFILESNUM
                    elif name == 'Ask save':
                        self.askSave = (value == 'True')
                    elif name == 'Ask save only for named projects':
                        self.askSaveOnlyForNamedProjects = (value == 'True')

    def save(self):
        """Save preferences to file"""
        try:
            with open(self._prefsPath, "w") as fp:

                if self.recentFilesNum != self._DEFAULTRECENTFILESNUM:
                    fp.write('Recent Files: %s\n' % str(self.recentFilesNum))
                if self.askSave != self._ASKSAVE:
                    fp.write('Ask save: %s\n' % str(self.askSave))
                if self.askSaveOnlyForNamedProjects != self._ASKSAVEONLYFORNAMEDPROJECTS:
                    fp.write('Ask save only for named projects: %s\n' % str(self.askSaveOnlyForNamedProjects))

        except IOError as ex:
            sys.stderr.write("Could not save preferences: %s\n" % str(ex))
            return
