import os
import sys

from PySide2.QtCore import QSize


def getConfigDirectory():
    """
        Return the user-specific configuration directory based on XDG Base Directory Specification.
    """
    home = os.path.expanduser('~')
    xdg_config_home = os.environ.get('XDG_CONFIG_HOME') or os.path.join(home, '.config')

    config_dir = os.path.join(xdg_config_home, 'kang')

    return config_dir


def _getSavedWindowSettings(path):
    """Load window settings from file"""
    if not os.path.isfile(path):
        return

    try:
        with open(path, 'r') as fp:
            line = fp.readline()[:-1]
    except IOError as ex:
        sys.stderr.write("Could not load window settings: %s\n" % str(ex))
        return

    geo = line.split(' ')

    x = int(geo[0])
    y = int(geo[1])
    width = int(geo[2])
    height = int(geo[3])

    return {'x': x,
            'y': y,
            'width': width,
            'height': height}


def saveWindowSettings(window, filename):
    """Save window position/size to file"""
    path = os.path.join(getConfigDirectory(), filename)

    s = window.size()
    x = window.x()
    y = window.y()

    try:
        with open(path, 'w') as fp:
            fp.write('%d %d %d %d\n' % (x, y, s.width(), s.height()))
    except IOError as ex:
        sys.stderr.write("Could not save window settings: %s\n" % str(ex))


def restoreWindowSettings(window, filename):
    """Restore window position/size to the last saved values"""
    path = os.path.join(getConfigDirectory(), filename)

    d = _getSavedWindowSettings(path)

    if d:
        x = d['x']
        y = d['y']
        width = d['width']
        height = d['height']
        sz = QSize(width, height)

        window.move(x, y)
        window.resize(sz)


def findFile(dr, filename):
    """Find application resources"""
    filename = os.path.join(dr, filename)

    apppath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    dirs = [apppath]

    for d in dirs:
        path = os.path.join(d, filename)
        if os.access(path, os.R_OK):
            return path

    return None
