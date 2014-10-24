from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QMessageBox
import urllib

from kang.gui.importURLDialogBA import ImportURLDialogBA
from kang.modules.util import getIcon


class ImportURLDialog(ImportURLDialogBA):
    
    def __init__(self, parent, url=None):
        ImportURLDialogBA.__init__(self, parent)
        self.parent = parent
        
        self.setWindowIcon(getIcon('kang-icon'))
        
        if url:
            self.URLTextEdit.setText(url)


    def importURL(self):
        url = str(self.URLTextEdit.toPlainText())
        if url:
            try:
                fp = urllib.urlopen(url)
                lines = fp.readlines()
            except Exception as e:
                QMessageBox.information(None, "Failed to open URL",
                                        "Could not open the specified URL.  Please check to ensure that you have entered the correct URL.\n\n%s" % str(e))
                return
    
            html = ''.join(lines)
    
            self.parent.emit(SIGNAL('urlImported(PyQt_PyObject, PyQt_PyObject)'), html, url)
        
        ImportURLDialogBA.accept(self)
        
        
#     def help_slot(self):
#         f = findFile('help', 'importURL.html')
#         if f:
#             webbrowser.open('file://%s' % f)
#         else:
#             webbrowser.open('%s/help/importURL.html' % KANG_WEBSITE)
