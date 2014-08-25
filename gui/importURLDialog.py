from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QMessageBox
import urllib
import webbrowser

from importURLDialogBA import importURLDialogBA
from modules import KANG_WEBSITE
from modules.util import getIcon, findFile


class importURLDialog(importURLDialogBA):
    
    def __init__(self, parent, url=None):
        importURLDialogBA.__init__(self, parent)
        self.parent = parent
        
        self.setWindowIcon(getIcon('kang-icon'))
        
        if url:
            self.URLTextEdit.setText(url)
            
        
    def help_slot(self):
        f = findFile('help', 'importURL.html')
        if f:
            webbrowser.open('file://%s' % f)
        else:
            webbrowser.open('%s/help/importURL.html' % KANG_WEBSITE)


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
        
        importURLDialogBA.accept(self)
