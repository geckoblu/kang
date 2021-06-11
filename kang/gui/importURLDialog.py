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

        self._parent = parent

        self.setWindowIcon(getIcon('kang-icon'))
        self.setWindowTitle(tr("Import URL"))
        self.resize(440, 0)  # Height will be recalculated
        self.setModal(True)

        label1 = QLabel(tr("Enter URL to import"))

        self._edit = QLineEdit()
        self._edit.setPlaceholderText('https://example.com/')
        self._edit.setText(url)

        label2 = QLabel(tr("Mode"))
        self._combo = QComboBox()
        self._combo.addItem(tr("Text"), ImportURLDialogMode.TEXT)
        self._combo.addItem(tr("Html"), ImportURLDialogMode.HTML)

        hLayout = QHBoxLayout()
        hLayout.addWidget(label2)
        hLayout.addWidget(self._combo)
        hLayout.addStretch()

        vLayout = QVBoxLayout()
        vLayout.addWidget(label1)
        vLayout.addWidget(self._edit)
        vLayout.addLayout(hLayout)
        vLayout.addWidget(QLabel(' '))
        vLayout.addStretch()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        buttonBox.rejected.connect(self.close)
        buttonBox.accepted.connect(self._importURL)

        gridLayout = QGridLayout(self)
        gridLayout.addLayout(vLayout, 0, 0, 1, 1)
        gridLayout.addWidget(buttonBox, 1, 0, 1, 1)

        self._text = ''

    def getURL(self):
        self.exec()
        return (self.result(), self._text, self._edit.text(), self._combo.currentData())

    def _importURL(self):
        url = self._edit.text()
        if url:
            try:
                with urllib.request.urlopen(url) as response:
                    data = response.read()  # a `bytes` object
                    self._text = data.decode('utf-8')  # a `str`; this step can't be used if data is binary
            except Exception as ex:
                QMessageBox.information(self._parent,
                                        "Failed to open URL",
                                        _ERROR_MESSAGE % str(ex))
                return

        QDialog.accept(self)


_ERROR_MESSAGE = """Could not open the specified URL.
Please check to ensure that you have entered the correct URL.

%s
"""
