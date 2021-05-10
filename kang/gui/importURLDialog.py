import urllib.request

from PySide2.QtCore import SIGNAL
from PySide2.QtWidgets import QMessageBox

from kang.gui.importURLDialogBA import ImportURLDialogBA
from kang.images import getIcon


class ImportURLDialog(ImportURLDialogBA):

    def __init__(self, parent, url=None):
        ImportURLDialogBA.__init__(self, parent)
        self.parent = parent

        self.setWindowIcon(getIcon('kang-icon'))

        if url:
            self.URLTextEdit.setText(url)

    def importURL(self):
        # TODO: Review importURL
        url = str(self.URLTextEdit.toPlainText())
        if url:
            try:
                response = urllib.request.urlopen(url)
                data = response.read()  # a `bytes` object
                text = data.decode('utf-8')  # a `str`; this step can't be used if data is binary
            except Exception as ex:
                QMessageBox.information(None, "Failed to open URL",
                                        "Could not open the specified URL.  Please check to ensure that you have entered the correct URL.\n\n%s" % str(ex))
                return

            html = ''.join(text)

            self.parent.emit(SIGNAL('urlImported(PyQt_PyObject, PyQt_PyObject)'), html, url)

        ImportURLDialogBA.accept(self)
