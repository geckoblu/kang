from urlDialogBA import URLDialogBA
import help
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import urllib


class URLDialog(URLDialogBA):
    def __init__(self, parent, url=None):
        URLDialogBA.__init__(self, parent)
        self.parent = parent
        if url:
            self.URLTextEdit.setText(url)
            
        self.show()
        
    def help_slot(self):
        self.helpWindow = help.Help(self, "importURL.html")

    def ok_slot(self):
        url = str(self.URLTextEdit.toPlainText())
        try:
            fp = urllib.urlopen(url)
            lines = fp.readlines()
        except Exception, e:
            QMessageBox.information(None, "Failed to open URL",
                                    "Could not open the specified URL.  Please check to ensure that you have entered the correct URL.\n\n%s" % str(e))
            return


        html = ''.join(lines)

        # TODO: Review this
        self.parent.emit(SIGNAL('urlImported()'), (html, url))
        
        URLDialogBA.accept(self)
