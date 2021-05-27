import os


def getConfigDirectory():
    """
        Return the user-specific configuration directory based on XDG Base Directory Specification.
    """
    home = os.path.expanduser('~')
    xdg_config_home = os.environ.get('XDG_CONFIG_HOME') or os.path.join(home, '.config')

    config_dir = os.path.join(xdg_config_home, 'kang')

    return config_dir


def findFile(dirname, filename):
    """Find application resources"""
    filename = os.path.join(dirname, filename)

    apppath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    dirs = [apppath]

    for d in dirs:
        path = os.path.join(d, filename)
        if os.access(path, os.R_OK):
            return path

    return None


def strtobool(val):
    strval = str(val).lower()

    if strval == 'true':
        return True

    if strval == 'false':
        return False

    raise ValueError('invalid boolean value: %r' % (val))
