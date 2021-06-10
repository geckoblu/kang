import urllib.request
from enum import Enum

from PySide2.QtWidgets import QDialog, QDialogButtonBox, QGridLayout, QVBoxLayout, QLabel, \
                              QLineEdit, QMessageBox, QComboBox, QHBoxLayout

from kang.images import getIcon

tr = lambda msg: msg


class ImportURLDialogMode(Enum):
    TEXT = 1
    HTML = 0


class ImportURLDialog(QDialog):

    def __init__(self, parent=None, url=''):
        QDialog.__init__(self, parent)
        
        self.parent = parent

        self.setWindowIcon(getIcon('kang-icon'))
        self.setWindowTitle(tr("Import URL"))
        self.resize(440, 0)  # Height will be recalculated
        self.setModal(True)

        label1 = QLabel(tr("Enter URL to import"))

        self.edit = QLineEdit()
        self.edit.setPlaceholderText('https://example.com/')
        self.edit.setText(url)

        label2 = QLabel(tr("Mode"))
        self.combo = QComboBox()
        self.combo.addItem(tr("Text"), ImportURLDialogMode.TEXT)
        self.combo.addItem(tr("Html"), ImportURLDialogMode.HTML)

        hLayout = QHBoxLayout()
        hLayout.addWidget(label2)
        hLayout.addWidget(self.combo)
        hLayout.addStretch()

        vLayout = QVBoxLayout()
        vLayout.addWidget(label1)
        vLayout.addWidget(self.edit)
        vLayout.addLayout(hLayout)
        vLayout.addWidget(QLabel(' '))
        vLayout.addStretch()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        buttonBox.rejected.connect(self.close)
        buttonBox.accepted.connect(self._importURL)

        gridLayout = QGridLayout(self)
        gridLayout.addLayout(vLayout, 0, 0, 1, 1)
        gridLayout.addWidget(buttonBox, 1, 0, 1, 1)

        self.text = ''

    def getURL(self):
        self.exec()
        return (self.result(), self.text, self.edit.text(), self.combo.currentData())

    def _importURL(self):
        url = self.edit.text()
        if url:
            try:
                with urllib.request.urlopen(url) as response:
                    data = response.read()  # a `bytes` object
                    self.text = data.decode('utf-8')  # a `str`; this step can't be used if data is binary
            except Exception as ex:
                QMessageBox.information(self.parent,
                                        "Failed to open URL",
                                        _ERROR_MESSAGE % str(ex))
                return

        QDialog.accept(self)


_ERROR_MESSAGE = """Could not open the specified URL.
Please check to ensure that you have entered the correct URL.

%s
"""
