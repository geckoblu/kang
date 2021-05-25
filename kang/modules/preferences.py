import json
import os

from kang.modules.util import getConfigDirectory, strtobool


class Preferences:
    """Used to handle Kang preferences.
       Stores/load them to file.
    """

    def __init__(self, filename=None):

        self._filename = filename
        if not self._filename:
            self._filename = os.path.join(getConfigDirectory(), 'preferences.json')

        # Default values
        self.recentFilesNum = 5
        self.askSave = True
        self.askSaveOnlyForNamedProjects = False

    def load(self):
        """Load preferences from file"""
        if not os.path.isfile(self._filename):
            return

        with open(self._filename, 'r') as jfile:
            jdict = json.load(jfile)

        try:
            self.recentFilesNum = int(jdict.get('recent_files_num', self.recentFilesNum))
        except ValueError:
            pass  # Ignore and let to default value

        try:
            self.askSave = strtobool(jdict.get('ask_save', self.askSave))
        except ValueError:
            pass  # Ignore and let to default value

        try:
            self.askSaveOnlyForNamedProjects = strtobool(jdict.get('ask_save_projects',
                                                                   self.askSaveOnlyForNamedProjects))
        except ValueError:
            pass  # Ignore and let to default value

    def save(self):
        """Save preferences to file"""

        jdict = {}

        jdict['recent_files_num'] = self.recentFilesNum
        jdict['ask_save'] = self.askSave
        jdict['ask_save_projects'] = self.askSaveOnlyForNamedProjects

        with open(self._filename, 'w') as jfile:
            json.dump(jdict, jfile, indent=4)

    def __str__(self):
        """Just a basic implementation for debug"""
        s = '['
        s += str(self.recentFilesNum)
        s += ', '
        s += str(self.askSave)
        s += ', '

        s += str(self.askSaveOnlyForNamedProjects)
        s += ']'
        return s
