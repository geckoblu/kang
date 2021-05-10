# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reportBugDialogBA4.ui'
#
# Created: Fri Aug  8 16:33:56 2014
#      by: PySide2 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
# pylint: disable=all
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# try:
    # _fromUtf8 = QString.fromUtf8
# except AttributeError:


def _fromUtf8(s):
    return s


try:
    _encoding = QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)

except AttributeError:

    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)


class Ui_ReportBugDialogBA(object):

    def setupUi(self, ReportBugDialogBA):
        ReportBugDialogBA.setObjectName(_fromUtf8("ReportBugDialogBA"))
        ReportBugDialogBA.resize(400, 300)
        ReportBugDialogBA.setSizeGripEnabled(True)
        ReportBugDialogBA.setModal(True)
        self.gridLayout = QGridLayout(ReportBugDialogBA)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout1 = QGridLayout()
        self.gridLayout1.setObjectName(_fromUtf8("gridLayout1"))
        self.bugIcon = QLabel(ReportBugDialogBA)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bugIcon.sizePolicy().hasHeightForWidth())
        self.bugIcon.setSizePolicy(sizePolicy)
        self.bugIcon.setText(_fromUtf8(""))
        self.bugIcon.setObjectName(_fromUtf8("bugIcon"))
        self.gridLayout1.addWidget(self.bugIcon, 0, 0, 1, 1)
        self.labelMessage = QLabel(ReportBugDialogBA)
        self.labelMessage.setObjectName(_fromUtf8("labelMessage"))
        self.gridLayout1.addWidget(self.labelMessage, 0, 1, 1, 1)
        self.textMessage = QPlainTextEdit(ReportBugDialogBA)
        self.textMessage.setReadOnly(True)
        self.textMessage.setPlainText(_fromUtf8(""))
        self.textMessage.setObjectName(_fromUtf8("textMessage"))
        self.gridLayout1.addWidget(self.textMessage, 1, 1, 1, 1)
        self.copyButton = QPushButton(ReportBugDialogBA)
        self.copyButton.setAutoDefault(True)
        self.copyButton.setObjectName(_fromUtf8("copyButton"))
        self.gridLayout1.addWidget(self.copyButton, 2, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout1, 0, 0, 1, 1)
        self.buttonBox = QDialogButtonBox(ReportBugDialogBA)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.actionCopyToClipoard = QAction(ReportBugDialogBA)
        self.actionCopyToClipoard.setObjectName(_fromUtf8("actionCopyToClipoard"))

        self.retranslateUi(ReportBugDialogBA)
        QObject.connect(self.buttonBox, SIGNAL(_fromUtf8("rejected()")), ReportBugDialogBA.close)
        QObject.connect(self.copyButton, SIGNAL(_fromUtf8("clicked()")), ReportBugDialogBA.copyToClipboard)
        QMetaObject.connectSlotsByName(ReportBugDialogBA)

    def retranslateUi(self, ReportBugDialogBA):
        ReportBugDialogBA.setWindowTitle(_translate("ReportBugDialogBA", "ERROR", None))
        self.labelMessage.setText(_translate("ReportBugDialogBA", "An unexpected exception has occurred.\n"
"Please fill a bug report at:\n"
"https://github.com/geckoblu/kang/issues\n"
"reporting the text below.", None))
        self.copyButton.setText(_translate("ReportBugDialogBA", "Copy to clipboard", None))
        self.actionCopyToClipoard.setText(_translate("ReportBugDialogBA", "copyToClipoard", None))
        self.actionCopyToClipoard.setToolTip(_translate("ReportBugDialogBA", "Copy to clipboard", None))


class ReportBugDialogBA(QDialog, Ui_ReportBugDialogBA):

    def __init__(self, parent=None, f=Qt.WindowFlags()):
        QDialog.__init__(self, parent, f)

        self.setupUi(self)
