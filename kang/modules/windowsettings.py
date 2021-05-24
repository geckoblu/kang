import os
import json

from kang.modules.util import getConfigDirectory


class WindowSettings:
    """Store / Load window settings from file"""

    def __init__(self, filename=None):

        self._filename = filename
        if not self._filename:
            self._filename = os.path.join(getConfigDirectory(), 'windowsettings.json')

    def save(self, window):
        """Save settings to file"""
        jdict = {}

        size = window.size()

        jdict['width'] = size.width()
        jdict['height'] = size.height()
        jdict['x'] = window.x()
        jdict['y'] = window.y()

        with open(self._filename, 'w') as jfile:
            json.dump(jdict, jfile, indent=4)

    def restore(self, window):
        """Load preferences from file"""
        if not os.path.isfile(self._filename):
            return

        with open(self._filename, 'r') as jfile:
            jdict = json.load(jfile)

        x = int(jdict['x'])
        y = int(jdict['y'])
        width = int(jdict['width'])
        height = int(jdict['height'])

        window.move(x, y)
        window.resize(width, height)
