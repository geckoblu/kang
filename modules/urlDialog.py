from urlDialogBA import URLDialogBA
import help as khelp
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QMessageBox
import urllib


class URLDialog(URLDialogBA):
    def __init__(self, parent, url=None):
        URLDialogBA.__init__(self, parent)
        self.parent = parent
        if url:
            self.URLTextEdit.setText(url)
            
        self.show()
        
    def help_slot(self):
        self.helpWindow = khelp.Help(self, "importURL.html")

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

        self.parent.emit(SIGNAL('urlImported(PyQt_PyObject, PyQt_PyObject)'), html, url)
        
        URLDialogBA.accept(self)
