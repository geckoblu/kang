# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newUserDialogBA.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewUserDialogBA(object):
    def setupUi(self, NewUserDialogBA):
        NewUserDialogBA.setObjectName("NewUserDialogBA")
        NewUserDialogBA.resize(352, 326)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NewUserDialogBA.sizePolicy().hasHeightForWidth())
        NewUserDialogBA.setSizePolicy(sizePolicy)
        self.vboxlayout = QtWidgets.QVBoxLayout(NewUserDialogBA)
        self.vboxlayout.setContentsMargins(11, 11, 11, 11)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")
        self.vboxlayout1 = QtWidgets.QVBoxLayout()
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.textLabel1 = QtWidgets.QLabel(NewUserDialogBA)
        self.textLabel1.setAlignment(QtCore.Qt.AlignVCenter)
        self.textLabel1.setWordWrap(True)
        self.textLabel1.setObjectName("textLabel1")
        self.vboxlayout1.addWidget(self.textLabel1)
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")
        self.pixmapLabel2 = QtWidgets.QLabel(NewUserDialogBA)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pixmapLabel2.sizePolicy().hasHeightForWidth())
        self.pixmapLabel2.setSizePolicy(sizePolicy)
        self.pixmapLabel2.setPixmap(QtGui.QPixmap("image1"))
        self.pixmapLabel2.setScaledContents(True)
        self.pixmapLabel2.setWordWrap(False)
        self.pixmapLabel2.setObjectName("pixmapLabel2")
        self.gridlayout.addWidget(self.pixmapLabel2, 1, 1, 1, 1)
        self.textLabel4 = QtWidgets.QLabel(NewUserDialogBA)
        self.textLabel4.setWordWrap(False)
        self.textLabel4.setObjectName("textLabel4")
        self.gridlayout.addWidget(self.textLabel4, 1, 0, 1, 1)
        self.pixmapLabel1 = QtWidgets.QLabel(NewUserDialogBA)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pixmapLabel1.sizePolicy().hasHeightForWidth())
        self.pixmapLabel1.setSizePolicy(sizePolicy)
        self.pixmapLabel1.setPixmap(QtGui.QPixmap("image2"))
        self.pixmapLabel1.setScaledContents(True)
        self.pixmapLabel1.setWordWrap(False)
        self.pixmapLabel1.setObjectName("pixmapLabel1")
        self.gridlayout.addWidget(self.pixmapLabel1, 0, 1, 1, 1)
        self.textLabel3 = QtWidgets.QLabel(NewUserDialogBA)
        self.textLabel3.setWordWrap(False)
        self.textLabel3.setObjectName("textLabel3")
        self.gridlayout.addWidget(self.textLabel3, 0, 0, 1, 1)
        self.vboxlayout1.addLayout(self.gridlayout)
        self.vboxlayout.addLayout(self.vboxlayout1)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewUserDialogBA)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(NewUserDialogBA)
        self.buttonBox.accepted.connect(NewUserDialogBA.close)
        QtCore.QMetaObject.connectSlotsByName(NewUserDialogBA)

    def retranslateUi(self, NewUserDialogBA):
        _translate = QtCore.QCoreApplication.translate
        NewUserDialogBA.setWindowTitle(_translate("NewUserDialogBA", "Kang new user information"))
        self.textLabel1.setText(_translate("NewUserDialogBA", "<html><head/><body><p><span style=\" font-size:large; font-weight:600;\">Welcome to Kang.</span></p><p>It appears that this is your first time using Kang - The Python Regular Expression Editor. </p><p>In order to help you familiarize yourself with Kang, you may wish to explore the Regex Library. Additionally, Kang contains a Python Regex Reference Guide. You can access these tools by clicking on the appropriate toolbar icon.</p></body></html>"))
        self.textLabel4.setText(_translate("NewUserDialogBA", "<b>Regex Reference Guide</b>"))
        self.textLabel3.setText(_translate("NewUserDialogBA", "<b>Regex Library</b>"))
