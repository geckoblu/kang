#FIXME from PyQt5.QtCore import SIGNAL
from PyQt5.Qt import QMessageBox
import urllib

from kang.gui.importURLDialogBA import Ui_ImportURLDialogBA
from kang.images import getIcon


class ImportURLDialog(Ui_ImportURLDialogBA):

    def __init__(self, parent, url=None):
        Ui_ImportURLDialogBA.__init__(self, parent)
        self.parent = parent

        self.setWindowIcon(getIcon('kang-icon'))

        if url:
            self.URLTextEdit.setText(url)

    def importURL(self):
        url = str(self.URLTextEdit.toPlainText())
        if url:
            try:
                #FIXME fp = urllib.urlopen(url)
                lines = []
                # lines = fp.readlines()
            except Exception as ex:
                QMessageBox.information(None, "Failed to open URL",
                                        "Could not open the specified URL.  Please check to ensure that you have entered the correct URL.\n\n%s" % str(ex))
                return

            html = ''.join(lines)

            #FIXME  self.parent.emit(SIGNAL('urlImported(PyQt_PyObject, PyQt_PyObject)'), html, url)

        #FIXME ImportURLDialogBA.accept(self)
