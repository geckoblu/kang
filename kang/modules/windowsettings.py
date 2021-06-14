import os
import json
import traceback

from kang.modules.util import getConfigDirectory, strtobool

# Friend class
# pylint: disable=protected-access
class WindowSettings:
    """Store / Load window settings from file"""

    def __init__(self, filename=None):

        self._filename = filename
        if not self._filename:
            self._filename = os.path.join(getConfigDirectory(), 'windowsettings.json')

    def save(self, window):
        """Save settings to file"""
        try:
            jdict = {}

            size = window.size()

            jdict['width'] = size.width()
            jdict['height'] = size.height()
            jdict['x'] = window.x()
            jdict['y'] = window.y()

            jdict['showRegexReferenceGuide'] = window._showRegexReferenceGuide
            jdict['showRegexLibrary'] = window._showRegexLibrary
            jdict['_splitter'] = window._splitter.sizes()

            # return

            with open(self._filename, 'w') as jfile:
                json.dump(jdict, jfile, indent=4)
        except Exception:
            traceback.print_exc()

    def restore(self, window):
        """Load preferences from file"""
        if not os.path.isfile(self._filename):
            return

        try:

            with open(self._filename, 'r') as jfile:
                jdict = json.load(jfile)

            # Load window properties
            x = int(jdict['x'])
            y = int(jdict['y'])
            width = int(jdict['width'])
            height = int(jdict['height'])
            sizes = jdict['_splitter']

            showRegexReferenceGuide = strtobool(jdict['showRegexReferenceGuide'])
            showRegexLibrary = strtobool(jdict['showRegexLibrary'])

            # Set window properties

            window.move(x, y)
            window.resize(width, height)

            window._helpRegexReferenceGuideAction.setChecked(showRegexReferenceGuide)
            window.helpRegexReferenceGuide(showRegexReferenceGuide)

            window._helpRegexLibraryAction.setChecked(showRegexLibrary)
            window.helpRegexLibrary(showRegexLibrary)

            if int(sizes[0] > 0 and int(sizes[1]) > 0):
                window._splitter.setSizes(sizes)
        except Exception:
            traceback.print_exc()
