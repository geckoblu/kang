# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/importURLDialogBA4.ui'
#
# Created: Fri Aug 29 08:48:27 2014
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

class Ui_ImportURLDialogBA(object):
    def setupUi(self, ImportURLDialogBA):
        ImportURLDialogBA.setObjectName(_fromUtf8("ImportURLDialogBA"))
        ImportURLDialogBA.resize(443, 203)
        ImportURLDialogBA.setSizeGripEnabled(True)
        ImportURLDialogBA.setModal(True)
        self.gridlayout = QtGui.QGridLayout(ImportURLDialogBA)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.buttonBox = QtGui.QDialogButtonBox(ImportURLDialogBA)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridlayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.groupBox1 = QtGui.QGroupBox(ImportURLDialogBA)
        self.groupBox1.setObjectName(_fromUtf8("groupBox1"))
        self.gridlayout1 = QtGui.QGridLayout(self.groupBox1)
        self.gridlayout1.setObjectName(_fromUtf8("gridlayout1"))
        self.URLTextEdit = QtGui.QTextEdit(self.groupBox1)
        self.URLTextEdit.setProperty("text", _fromUtf8(""))
        self.URLTextEdit.setObjectName(_fromUtf8("URLTextEdit"))
        self.gridlayout1.addWidget(self.URLTextEdit, 0, 0, 1, 1)
        self.gridlayout.addWidget(self.groupBox1, 0, 0, 1, 1)

        self.retranslateUi(ImportURLDialogBA)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ImportURLDialogBA.close)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ImportURLDialogBA.importURL)
        QtCore.QMetaObject.connectSlotsByName(ImportURLDialogBA)

    def retranslateUi(self, ImportURLDialogBA):
        ImportURLDialogBA.setWindowTitle(_translate("ImportURLDialogBA", "Import URL", None))
        self.groupBox1.setTitle(_translate("ImportURLDialogBA", "Enter URL to import", None))


class ImportURLDialogBA(QtGui.QDialog, Ui_ImportURLDialogBA):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QDialog.__init__(self, parent, f)

        self.setupUi(self)

