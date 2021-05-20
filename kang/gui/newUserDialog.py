import sys

from PySide2.QtWidgets import QDialog, QApplication, QDialogButtonBox, QGridLayout, \
                              QVBoxLayout, QLabel

from kang.images import getIcon, getPixmap

tr = lambda msg: msg


class NewUserDialog(QDialog):

    def __init__(self, parent):
        QDialog.__init__(self, parent)

        self.setWindowIcon(getIcon('kang-icon'))
        self.setWindowTitle(tr("Kang new user information"))
        self.setModal(True)

        verticalLayout = QVBoxLayout()

        label = QLabel(WELCOME_MESSAGE)
        verticalLayout.addWidget(label)

        gridLayout = QGridLayout()
        verticalLayout.addLayout(gridLayout)

        label = QLabel("<b>" + tr("Regex Reference Guide") + "</b>")
        gridLayout.addWidget(label, 0, 0, 1, 1)

        pixmapLabel = QLabel()
        image1 = getPixmap("library.svg")
        pixmapLabel.setPixmap(image1)
        gridLayout.addWidget(pixmapLabel, 0, 1, 1, 1)

        label = QLabel("<b>" + tr("Regex Library") + "</b>")
        gridLayout.addWidget(label, 1, 0, 1, 1)

        pixmapLabel = QLabel()
        image1 = getPixmap("book.svg")
        pixmapLabel.setPixmap(image1)
        gridLayout.addWidget(pixmapLabel, 1, 1, 1, 1)

        label = QLabel(' ')
        verticalLayout.addWidget(label)

        verticalLayout.addStretch()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok)
        buttonBox.accepted.connect(self.close)

        gridLayout = QGridLayout(self)
        gridLayout.addLayout(verticalLayout, 0, 0, 1, 1)
        gridLayout.addWidget(buttonBox, 1, 0, 1, 1)


WELCOME_MESSAGE_TITLE = tr("Welcome to Kang.")

WELCOME_MESSAGE_LINE1 = tr("""It appears that this is your first time using Kang -<br/>
The Python Regular Expression Editor.""")

WELCOME_MESSAGE_LINE2 = tr("""In order to help you familiarize yourself with Kang,<br/>
you may wish to explore the Regex Library.<br/>
Additionally, Kang contains a Python Regex Reference Guide.<br/>
You can access these tools by clicking on the appropriate toolbar icon.<br/>""")

WELCOME_MESSAGE = """
<html><head/><body><p><span style=\" font-size:large; font-weight:600;\">%s</span></p><p>%s</p><p>%s</p></body></html>
""" % (WELCOME_MESSAGE_TITLE, WELCOME_MESSAGE_LINE1, WELCOME_MESSAGE_LINE2)

if __name__ == '__main__':
    qApp = QApplication(sys.argv)

    dialog = NewUserDialog(None)
    dialog.show()

    sys.exit(qApp.exec_())
