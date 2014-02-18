# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'urlDialogBA4.ui'
#
# Created: Thu Jan 16 08:49:34 2014
#      by: PyQt4 UI code generator 4.10
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

class Ui_URLDialogBA(object):
    def setupUi(self, URLDialogBA):
        URLDialogBA.setObjectName(_fromUtf8("URLDialogBA"))
        URLDialogBA.resize(443, 170)
        URLDialogBA.setSizeGripEnabled(True)
        self.gridlayout = QtGui.QGridLayout(URLDialogBA)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.buttonHelp = QtGui.QPushButton(URLDialogBA)
        self.buttonHelp.setAutoDefault(True)
        self.buttonHelp.setObjectName(_fromUtf8("buttonHelp"))
        self.hboxlayout.addWidget(self.buttonHelp)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.buttonOk = QtGui.QPushButton(URLDialogBA)
        self.buttonOk.setShortcut(_fromUtf8(""))
        self.buttonOk.setAutoDefault(True)
        self.buttonOk.setDefault(True)
        self.buttonOk.setObjectName(_fromUtf8("buttonOk"))
        self.hboxlayout.addWidget(self.buttonOk)
        self.buttonCancel = QtGui.QPushButton(URLDialogBA)
        self.buttonCancel.setShortcut(_fromUtf8(""))
        self.buttonCancel.setAutoDefault(True)
        self.buttonCancel.setObjectName(_fromUtf8("buttonCancel"))
        self.hboxlayout.addWidget(self.buttonCancel)
        self.gridlayout.addLayout(self.hboxlayout, 1, 0, 1, 1)
        self.groupBox1 = QtGui.QGroupBox(URLDialogBA)
        self.groupBox1.setObjectName(_fromUtf8("groupBox1"))
        self.gridlayout1 = QtGui.QGridLayout(self.groupBox1)
        self.gridlayout1.setObjectName(_fromUtf8("gridlayout1"))
        self.URLTextEdit = QtGui.QTextEdit(self.groupBox1)
        self.URLTextEdit.setProperty("text", _fromUtf8(""))
        self.URLTextEdit.setObjectName(_fromUtf8("URLTextEdit"))
        self.gridlayout1.addWidget(self.URLTextEdit, 0, 0, 1, 1)
        self.gridlayout.addWidget(self.groupBox1, 0, 0, 1, 1)

        self.retranslateUi(URLDialogBA)
        QtCore.QObject.connect(self.buttonOk, QtCore.SIGNAL(_fromUtf8("clicked()")), URLDialogBA.ok_slot)
        QtCore.QObject.connect(self.buttonCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), URLDialogBA.reject)
        QtCore.QObject.connect(self.buttonHelp, QtCore.SIGNAL(_fromUtf8("clicked()")), URLDialogBA.help_slot)
        QtCore.QMetaObject.connectSlotsByName(URLDialogBA)

    def retranslateUi(self, URLDialogBA):
        URLDialogBA.setWindowTitle(_translate("URLDialogBA", "Import URL", None))
        self.buttonHelp.setText(_translate("URLDialogBA", "&Help", None))
        self.buttonHelp.setShortcut(_translate("URLDialogBA", "F1", None))
        self.buttonOk.setText(_translate("URLDialogBA", "&OK", None))
        self.buttonCancel.setText(_translate("URLDialogBA", "&Cancel", None))
        self.groupBox1.setTitle(_translate("URLDialogBA", "Enter URL to import", None))


class URLDialogBA(QtGui.QDialog, Ui_URLDialogBA):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QDialog.__init__(self, parent, f)

        self.setupUi(self)

