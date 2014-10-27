# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/newUserDialogBA4.ui'
#
# Created: Fri Aug 29 09:21:54 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_NewUserDialogBA(object):
    def setupUi(self, NewUserDialogBA):
        NewUserDialogBA.setObjectName(_fromUtf8("NewUserDialogBA"))
        NewUserDialogBA.resize(352, 326)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NewUserDialogBA.sizePolicy().hasHeightForWidth())
        NewUserDialogBA.setSizePolicy(sizePolicy)
        self.vboxlayout = QtGui.QVBoxLayout(NewUserDialogBA)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.textLabel1 = QtGui.QLabel(NewUserDialogBA)
        self.textLabel1.setAlignment(QtCore.Qt.AlignVCenter)
        self.textLabel1.setWordWrap(True)
        self.textLabel1.setObjectName(_fromUtf8("textLabel1"))
        self.vboxlayout1.addWidget(self.textLabel1)
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.pixmapLabel2 = QtGui.QLabel(NewUserDialogBA)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pixmapLabel2.sizePolicy().hasHeightForWidth())
        self.pixmapLabel2.setSizePolicy(sizePolicy)
        self.pixmapLabel2.setPixmap(QtGui.QPixmap(_fromUtf8("image1")))
        self.pixmapLabel2.setScaledContents(True)
        self.pixmapLabel2.setWordWrap(False)
        self.pixmapLabel2.setObjectName(_fromUtf8("pixmapLabel2"))
        self.gridlayout.addWidget(self.pixmapLabel2, 1, 1, 1, 1)
        self.textLabel4 = QtGui.QLabel(NewUserDialogBA)
        self.textLabel4.setWordWrap(False)
        self.textLabel4.setObjectName(_fromUtf8("textLabel4"))
        self.gridlayout.addWidget(self.textLabel4, 1, 0, 1, 1)
        self.pixmapLabel1 = QtGui.QLabel(NewUserDialogBA)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pixmapLabel1.sizePolicy().hasHeightForWidth())
        self.pixmapLabel1.setSizePolicy(sizePolicy)
        self.pixmapLabel1.setPixmap(QtGui.QPixmap(_fromUtf8("image2")))
        self.pixmapLabel1.setScaledContents(True)
        self.pixmapLabel1.setWordWrap(False)
        self.pixmapLabel1.setObjectName(_fromUtf8("pixmapLabel1"))
        self.gridlayout.addWidget(self.pixmapLabel1, 0, 1, 1, 1)
        self.textLabel3 = QtGui.QLabel(NewUserDialogBA)
        self.textLabel3.setWordWrap(False)
        self.textLabel3.setObjectName(_fromUtf8("textLabel3"))
        self.gridlayout.addWidget(self.textLabel3, 0, 0, 1, 1)
        self.vboxlayout1.addLayout(self.gridlayout)
        self.vboxlayout.addLayout(self.vboxlayout1)
        self.buttonBox = QtGui.QDialogButtonBox(NewUserDialogBA)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(NewUserDialogBA)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), NewUserDialogBA.close)
        QtCore.QMetaObject.connectSlotsByName(NewUserDialogBA)

    def retranslateUi(self, NewUserDialogBA):
        NewUserDialogBA.setWindowTitle(_translate("NewUserDialogBA", "Kang new user information", None))
        self.textLabel1.setText(_translate("NewUserDialogBA", "<html><head/><body><p><span style=\" font-size:large; font-weight:600;\">Welcome to Kang.</span></p><p>It appears that this is your first time using Kang - The Python Regular Expression Tester. </p><p>In order to help you familiarize yourself with Kang, you may wish to explore the Regex Library. Additionally, Kang contains a Python Regex Reference Guide. You can access these tools by clicking on the appropriate toolbar icon.</p></body></html>", None))
        self.textLabel4.setText(_translate("NewUserDialogBA", "<b>Regex Reference Guide</b>", None))
        self.textLabel3.setText(_translate("NewUserDialogBA", "<b>Regex Library</b>", None))


class NewUserDialogBA(QtGui.QDialog, Ui_NewUserDialogBA):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QDialog.__init__(self, parent, f)

        self.setupUi(self)

