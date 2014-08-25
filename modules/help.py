#  help.py: -*- Python -*-  DESCRIPTIVE TEXT.

from PyQt4.QtCore import QUrl
from PyQt4.QtGui import QTextBrowser
import webbrowser

from helpBA import HelpBA
from util import findFile, getIcon


class textbrowser(QTextBrowser):
    # reimplemented textbrowser that filters out external sources
    # future: launch web browser
    def __init__(self, parent=None):
        self.parent = parent
        QTextBrowser.__init__(self, parent)


    def setSource(self, src):
        #print('setSource:', src)
        s = str(src)
        if s[:7] == 'http://':
            webbrowser.open(s)
            return

        QTextBrowser.setSource(self, QUrl(src))
                
    
                

class Help(HelpBA):
    def __init__(self, parent, filename, external_browser=None):
        HelpBA.__init__(self, None)
        #Qt.WType_TopLevel | Qt.WDestructiveClose)
        
        self.external_browser = external_browser
        self.setGeometry(100, 50, 800, 600)
        self.setWindowTitle('Help')        
        
        self.textBrowser = textbrowser(self)
        absPath = self.getHelpFile(filename)

        self.setCentralWidget(self.textBrowser)
        self.textBrowser.setSource(absPath)
        
        self.loadToolbarIcons()
        
        self.fwdAvailable = 0
        self.show()


    def exitSlot(self):
        self.close()

    def backSlot(self):
        self.textBrowser.backward()

    def forwardSlot(self):
        self.textBrowser.forward()

    def homeSlot(self):
        self.textBrowser.home()



    def setForwardAvailable(self, b):
        #print 'bool: ', b
        self.fwdAvailable = b


    def forwardHandler(self):
        #print 'fwdAvail?: ', self.fwdAvailable
        if self.fwdAvailable:
            self.textBrowser.forward()
    
    def getHelpFile(self, filename):
        f = findFile('help', filename)
        return f
    
    def loadToolbarIcons(self):
        filehomeicon = getIcon('go-home');
        self.fileHomeAction.setIcon(filehomeicon)
        filebackicon = getIcon('go-previous');
        self.fileBackAction.setIcon(filebackicon)
        fileforwardicon = getIcon('go-next');
        self.fileForwardAction.setIcon(fileforwardicon)
        fileexiticon = getIcon('application-exit');
        self.fileExitAction.setIcon(fileexiticon)    

        
