
from PyQt4.QtCore import QString, QObject, SIGNAL
import os
import string
import sys

from modules.util import getConfigDirectory


try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


MAX_SIZE = 50 # max number of files to retain

class RecentFiles:
    def __init__(self, parent, numShown=5, debug=None):
        self.parent = parent
        self.numShown = int(numShown)
        self.debug = debug
        self.filename = os.path.join(getConfigDirectory(), 'recent_files')
        self.__recent_files = []
        self.__actions = []
        self.load()


    def load(self):
        try:
            fp = open(self.filename, "r")
            self.__recent_files = map(string.strip, fp.readlines())
        except Exception:
            #sys.stderr.write("Warning: %s\n" % str(e))
            return
        
        if self.debug: print "recent_files:", self.__recent_files
        self.addToMenu()


    def save(self):
        # truncate list if necessary
        self.__recent_files = self.__recent_files[:MAX_SIZE]
        try:
            fp = open(self.filename, "w")
            for f in self.__recent_files:
                fp.write("%s\n" % f)
            fp.close()
        except Exception as e:
            sys.stderr.write("Could not save recent file list %s\n" & str(e))
            

    def add(self, filename):
        try:
            self.__recent_files.remove(filename)
        except:
            pass

        self.__recent_files.insert(0, filename)
        self.save()
        self.addToMenu()


    def clearMenu(self):
        # clear each menu entry...
        for act in self.__actions:
            self.parent.fileMenu.removeAction(act)

        # clear list of menu entry indecies
        self.__actions = []

        
    def addToMenu(self, clear=1):
        if clear: self.clearMenu()

        # add applicable items to menu
        num = min(self.numShown, len(self.__recent_files))
        for i in range(num):
            filename = self.__recent_files[i]
            act = self.parent.fileMenu.addAction(filename)
            QObject.connect(act, SIGNAL(_fromUtf8('triggered()')), lambda fn=filename: self.openfile(fn));
            self.__actions.append(act)
            
        
    def openfile(self, filename):
        self.parent.fileMenuHandler(filename)


    def setNumShown(self, numShown):
        ns = int(numShown)
        if ns == self.numShown: return

        # clear menu of size X then add entries of size Y
        self.clearMenu()
        self.numShown = ns
        self.addToMenu(0)


#     def move(self, filename, menuid):
#         # fix me....
#         menu = self.parent.fileMenu
#         idx = menu.indexOf(self.__indecies[0])
#         menu.removeItem(menuid)
# #         menu.insertItem(QIconSet(QPixmap(xpm.newIcon)),
# #                         filename,
# #                         -1,
# #                         idx)
#         try:
#             self.__recent_files.remove(filename)
#         except:
#             pass
#         self.__indecies.insert(0, filename)

