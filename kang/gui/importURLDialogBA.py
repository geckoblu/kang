# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'importURLDialogBA.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ImportURLDialogBA(object):
    def setupUi(self, ImportURLDialogBA):
        ImportURLDialogBA.setObjectName("ImportURLDialogBA")
        ImportURLDialogBA.resize(443, 203)
        ImportURLDialogBA.setSizeGripEnabled(True)
        ImportURLDialogBA.setModal(True)
        self.gridlayout = QtWidgets.QGridLayout(ImportURLDialogBA)
        self.gridlayout.setContentsMargins(11, 11, 11, 11)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(ImportURLDialogBA)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.groupBox1 = QtWidgets.QGroupBox(ImportURLDialogBA)
        self.groupBox1.setObjectName("groupBox1")
        self.gridlayout1 = QtWidgets.QGridLayout(self.groupBox1)
        self.gridlayout1.setContentsMargins(11, 11, 11, 11)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")
        self.URLTextEdit = QtWidgets.QTextEdit(self.groupBox1)
        self.URLTextEdit.setProperty("text", "")
        self.URLTextEdit.setObjectName("URLTextEdit")
        self.gridlayout1.addWidget(self.URLTextEdit, 0, 0, 1, 1)
        self.gridlayout.addWidget(self.groupBox1, 0, 0, 1, 1)

        self.retranslateUi(ImportURLDialogBA)
        self.buttonBox.rejected.connect(ImportURLDialogBA.close)
        self.buttonBox.accepted.connect(ImportURLDialogBA.importURL)
        QtCore.QMetaObject.connectSlotsByName(ImportURLDialogBA)

    def retranslateUi(self, ImportURLDialogBA):
        _translate = QtCore.QCoreApplication.translate
        ImportURLDialogBA.setWindowTitle(_translate("ImportURLDialogBA", "Import URL"))
        self.groupBox1.setTitle(_translate("ImportURLDialogBA", "Enter URL to import"))
