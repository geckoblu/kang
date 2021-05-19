import sys
import urllib.request

from PySide2.QtWidgets import QDialog, QApplication, QDialogButtonBox, QGridLayout, \
                              QVBoxLayout, QLabel, QLineEdit, QMessageBox

from kang.images import getIcon

tr = lambda msg: msg


class ImportURLDialog(QDialog):

    def __init__(self, parent=None, url=''):
        QDialog.__init__(self, parent)

        self.setWindowIcon(getIcon('kang-icon'))
        self.setWindowTitle(tr("Import URL"))
        self.resize(440, 0)  # Height will be recalculated
        self.setModal(True)

        label = QLabel(tr("Enter URL to import"))
        self.edit = QLineEdit()
        self.edit.setPlaceholderText('https://example.com/')
        self.edit.setText(url)

        verticalLayout = QVBoxLayout()
        verticalLayout.addWidget(label)
        verticalLayout.addWidget(self.edit)
        verticalLayout.addWidget(QLabel(' '))
        verticalLayout.addStretch()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        buttonBox.rejected.connect(self.close)
        buttonBox.accepted.connect(self._importURL)

        gridLayout = QGridLayout(self)
        gridLayout.addLayout(verticalLayout, 0, 0, 1, 1)
        gridLayout.addWidget(buttonBox, 1, 0, 1, 1)

        self.text = ''

    def getURL(self):
        self.exec()
        return (self.result(), self.text, self.edit.text())

    def _importURL(self):
        url = self.edit.text()
        if url:
            try:
                with urllib.request.urlopen(url) as response:
                    data = response.read()  # a `bytes` object
                    self.text = data.decode('utf-8')  # a `str`; this step can't be used if data is binary
            except Exception as ex:
                QMessageBox.information(None,
                                        "Failed to open URL",
                                        ERROR_MESSAGE % str(ex))
                return

        QDialog.accept(self)


ERROR_MESSAGE = "Could not open the specified URL.\nPlease check to ensure that you have entered the correct URL.\n\n%s"

if __name__ == '__main__':
    qApp = QApplication(sys.argv)

    dialog = ImportURLDialog(None, 'http://example.com/')
    # dialog._importURL()
    # dialog.show()
    (ok, text, url) = dialog.getURL()

    if ok:
        print('Accepted:' + url)
        print(text)
    else:
        print('Rejected')
    print('End')

    sys.exit(qApp.exec_())
