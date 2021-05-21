from PySide2.QtGui import Qt
from PySide2.QtWidgets import QDialog, QApplication, QGridLayout, QLabel, \
                              QDialogButtonBox, QPushButton, QTextBrowser

from kang.images import getIcon, getPixmap

tr = lambda msg: msg


class ReportBugDialog(QDialog):

    def __init__(self, parent, msg):
        QDialog.__init__(self, parent)

        self.setWindowIcon(getIcon('kang-icon'))
        self.setWindowTitle(tr("ERROR"))
        self.setModal(True)
        self.resize(600, 400)

        gLayout = QGridLayout()

        pixmapLabel = QLabel()
        image1 = getPixmap('bug.svg')
        pixmapLabel.setPixmap(image1)
        gLayout.addWidget(pixmapLabel, 0, 0, 1, 1)

        label = QLabel(tr(_MESSAGE_TEXT))
        # label.setText("<a href=\"http://example.com/\">Click Here!</a>");
        label.setTextFormat(Qt.RichText)
        label.setTextInteractionFlags(Qt.TextBrowserInteraction)
        label.setOpenExternalLinks(True)

        gLayout.addWidget(label, 0, 1, 1, 1)

        self.edit = QTextBrowser()
        self.edit.setReadOnly(True)
        self.edit.setPlainText(msg)
        gLayout.addWidget(self.edit, 1, 1, 1, 1)

        copyButton = QPushButton(tr("Copy to clipboard"))
        copyButton.clicked.connect(self.copyToClipboard)
        gLayout.addWidget(copyButton, 2, 1, 1, 1)

        gLayout.addWidget(QLabel(' '), 3, 1, 1, 1)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Close)
        buttonBox.rejected.connect(self.close)

        gridLayout = QGridLayout(self)
        gridLayout.addLayout(gLayout, 0, 0, 1, 1)
        gridLayout.addWidget(buttonBox, 1, 0, 1, 1)

    def copyToClipboard(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.edit.toPlainText())


_MESSAGE_TEXT = """%s<br/>
%s:<br/>
<br/>
<a href=\"https://github.com/geckoblu/kang/issues/\">https://github.com/geckoblu/kang/issues</a><br/>
<br/>
%s.""" % (tr("An unexpected exception has occurred."),
          tr("Please fill a bug report at"),
          tr("reporting the text below"))
