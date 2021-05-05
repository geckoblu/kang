# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reportBugDialogBA.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ReportBugDialogBA(object):
    def setupUi(self, ReportBugDialogBA):
        ReportBugDialogBA.setObjectName("ReportBugDialogBA")
        ReportBugDialogBA.resize(400, 300)
        ReportBugDialogBA.setSizeGripEnabled(True)
        ReportBugDialogBA.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(ReportBugDialogBA)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout1 = QtWidgets.QGridLayout()
        self.gridLayout1.setSpacing(6)
        self.gridLayout1.setObjectName("gridLayout1")
        self.bugIcon = QtWidgets.QLabel(ReportBugDialogBA)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bugIcon.sizePolicy().hasHeightForWidth())
        self.bugIcon.setSizePolicy(sizePolicy)
        self.bugIcon.setText("")
        self.bugIcon.setObjectName("bugIcon")
        self.gridLayout1.addWidget(self.bugIcon, 0, 0, 1, 1)
        self.labelMessage = QtWidgets.QLabel(ReportBugDialogBA)
        self.labelMessage.setObjectName("labelMessage")
        self.gridLayout1.addWidget(self.labelMessage, 0, 1, 1, 1)
        self.textMessage = QtWidgets.QPlainTextEdit(ReportBugDialogBA)
        self.textMessage.setReadOnly(True)
        self.textMessage.setPlainText("")
        self.textMessage.setObjectName("textMessage")
        self.gridLayout1.addWidget(self.textMessage, 1, 1, 1, 1)
        self.copyButton = QtWidgets.QPushButton(ReportBugDialogBA)
        self.copyButton.setAutoDefault(True)
        self.copyButton.setObjectName("copyButton")
        self.gridLayout1.addWidget(self.copyButton, 2, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout1, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(ReportBugDialogBA)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.actionCopyToClipoard = QtWidgets.QAction(ReportBugDialogBA)
        self.actionCopyToClipoard.setObjectName("actionCopyToClipoard")

        self.retranslateUi(ReportBugDialogBA)
        self.buttonBox.rejected.connect(ReportBugDialogBA.close)
        self.copyButton.clicked.connect(ReportBugDialogBA.copyToClipboard)
        QtCore.QMetaObject.connectSlotsByName(ReportBugDialogBA)

    def retranslateUi(self, ReportBugDialogBA):
        _translate = QtCore.QCoreApplication.translate
        ReportBugDialogBA.setWindowTitle(_translate("ReportBugDialogBA", "ERROR"))
        self.labelMessage.setText(_translate("ReportBugDialogBA", "An unexpected exception has occurred.\n"
"Please fill a bug report at:\n"
"https://github.com/geckoblu/kang/issues\n"
"reporting the text below."))
        self.copyButton.setText(_translate("ReportBugDialogBA", "Copy to clipboard"))
        self.actionCopyToClipoard.setText(_translate("ReportBugDialogBA", "copyToClipoard"))
        self.actionCopyToClipoard.setToolTip(_translate("ReportBugDialogBA", "Copy to clipboard"))
