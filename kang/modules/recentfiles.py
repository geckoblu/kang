from PyQt4.QtCore import QString, QObject, SIGNAL
import os
import string
import sys

from kang.modules.util import getConfigDirectory


try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class RecentFiles:
    """Used to handle the recent file list.
       It stores the list of recent opened projects to a file
       and create the menu for handle them.
       The size of the file list and the number of menu items showed could be different.
    """

    _MAX_SIZE = 50  # max number of files to retain

    def __init__(self, parent, numShown=5):
        self._parent = parent
        self._numShown = int(numShown)
        self._filename = os.path.join(getConfigDirectory(), 'recent_files')
        self._recent_files = []
        self._actions = []
        self.load()

    def load(self):
        """Load recent file list from file and create menu"""
        if os.path.isfile(self._filename):
            try:
                with open(self._filename, "r") as fp:
                    self._recent_files = map(string.strip, fp.readlines())
            except IOError as ex:
                sys.stderr.write("Could not load recent file list: %s\n" % str(ex))

        self._createMenu()

    def save(self):
        """Save recent file list to file"""
        # truncate list if necessary
        self._recent_files = self._recent_files[:self._MAX_SIZE]
        try:
            with open(self._filename, "w") as fp:
                for f in self._recent_files:
                    fp.write("%s\n" % f)
        except IOError as ex:
            sys.stderr.write("Could not save recent file list %s\n" % str(ex))

    def add(self, filename):
        """Add a filename to the recent file list (automatically save and add to menu)"""
        try:
            self._recent_files.remove(filename)
        except:
            pass

        self._recent_files.insert(0, filename)
        self.save()
        self._createMenu()

    def remove(self, filename):
        """Remove a filename from the recent file list (and from menu)"""
        try:
            self._recent_files.remove(filename)
        except:
            pass

        self.save()
        self._createMenu()

    def _clearMenu(self):
        """Clear menu removing each entry (not from recent file list)"""
        # clear each menu entry...
        for act in self._actions:
            self._parent.fileMenu.removeAction(act)

        # clear list of menu entry
        self._actions = []

    def _createMenu(self, clear=1):
        """Create menu list using recent file list"""
        if clear:
            self._clearMenu()

        # add applicable items to menu
        num = min(self._numShown, len(self._recent_files))
        for i in range(num):
            filename = self._recent_files[i]
            act = self._parent.fileMenu.addAction(filename)
            QObject.connect(act, SIGNAL(_fromUtf8('triggered()')), lambda fn=filename: self._openFile(fn))
            self._actions.append(act)

    def _openFile(self, filename):
        """Delegate openFile action to parent"""
        self._parent.openFile(filename)

    def setNumShown(self, numShown):
        """Set maximum number of menu entry to show (update menu)"""
        ns = int(numShown)
        if ns == self._numShown:
            return

        # clear menu of size X then add entries of size Y
        self._clearMenu()
        self._numShown = ns
        self._createMenu(0)
