import os
import sys

from kang.modules.util import getConfigDirectory


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
        self._recentFiles = []
        self._actions = []
        self.load()

    def load(self):
        """Load recent file list from file and create menu"""
        self._recentFiles = []
        if os.path.isfile(self._filename):
            try:
                with open(self._filename, "r") as fp:
                    self._recentFiles = [filename.strip() for filename in fp.readlines()]
            except IOError as ex:
                sys.stderr.write("Could not load recent file list: %s\n" % str(ex))

        self._createMenu()

    def save(self):
        """Save recent file list to file"""
        # truncate list if necessary
        self._recentFiles = self._recentFiles[:self._MAX_SIZE]
        try:
            with open(self._filename, "w") as fp:
                for f in self._recentFiles:
                    fp.write("%s\n" % f)
        except IOError as ex:
            sys.stderr.write("Could not save recent file list %s\n" % str(ex))

    def add(self, filename):
        """Add a filename to the recent file list (automatically save and add to menu)"""
        try:
            self._recentFiles.remove(filename)
        except:
            pass

        self._recentFiles.insert(0, filename)
        self.save()
        self._createMenu()

    def remove(self, filename):
        """Remove a filename from the recent file list (and from menu)"""
        try:
            self._recentFiles.remove(filename)
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

        # TODO: create recent files menu before exit/quit menu
        # TODO: show only filename in menu and full path as tooltip

        # add applicable items to menu
        num = min(self._numShown, len(self._recentFiles))
        for i in range(num):
            filename = self._recentFiles[i]
            action = self._parent.fileMenu.addAction(filename)
            action.triggered.connect(lambda: self._openFile(filename))
            self._actions.append(action)

    def _openFile(self, filename):
        """Delegate loadFile action to parent"""
        self._parent.loadFile(filename)

    def setNumShown(self, numShown):
        """Set maximum number of menu entry to show (update menu)"""
        ns = int(numShown)
        if ns == self._numShown:
            return

        # clear menu of size X then add entries of size Y
        self._clearMenu()
        self._numShown = ns
        self._createMenu(0)
