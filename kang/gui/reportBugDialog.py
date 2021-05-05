from PyQt5 import QtGui

from kang.gui.reportBugDialogBA import ReportBugDialogBA
from kang.images import getPixmap, getIcon


class ReportBugDialog(ReportBugDialogBA):

    def __init__(self, parent, msg):
        ReportBugDialogBA.__init__(self, parent)
        self.parent = parent

        self.setWindowIcon(getIcon('kang-icon'))

        bugImage = getPixmap("bug.svg")
        self.bugIcon.setPixmap(bugImage)
        self.textMessage.setPlainText(msg)

    def copyToClipboard(self):
        clipboard = QtGui.QApplication.clipboard()
        clipboard.setText(self.textMessage.toPlainText())
