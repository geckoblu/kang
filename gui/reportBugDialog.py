from PyQt4 import QtGui

from modules.util import getPixmap, getIcon
from reportBugDialogBA import ReportBugDialogBA


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
        