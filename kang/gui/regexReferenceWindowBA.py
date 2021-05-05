# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'regexReferenceWindowBA.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegexReferenceWindowBA(object):
    def setupUi(self, RegexReferenceWindowBA):
        RegexReferenceWindowBA.setObjectName("RegexReferenceWindowBA")
        RegexReferenceWindowBA.resize(600, 605)
        self.widget = QtWidgets.QWidget(RegexReferenceWindowBA)
        self.widget.setObjectName("widget")
        self.gridlayout = QtWidgets.QGridLayout(self.widget)
        self.gridlayout.setContentsMargins(11, 11, 11, 11)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")
        self.referenceTreeWidget = QtWidgets.QTreeWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.referenceTreeWidget.sizePolicy().hasHeightForWidth())
        self.referenceTreeWidget.setSizePolicy(sizePolicy)
        self.referenceTreeWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.referenceTreeWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.referenceTreeWidget.setObjectName("referenceTreeWidget")
        self.gridlayout.addWidget(self.referenceTreeWidget, 0, 0, 1, 1)
        RegexReferenceWindowBA.setCentralWidget(self.widget)
        self.fileExitAction = QtWidgets.QAction(RegexReferenceWindowBA)
        self.fileExitAction.setShortcut("")
        self.fileExitAction.setProperty("name", "fileExitAction")
        self.fileExitAction.setObjectName("fileExitAction")
        self.editPasteAction = QtWidgets.QAction(RegexReferenceWindowBA)
        self.editPasteAction.setProperty("name", "editPasteAction")
        self.editPasteAction.setObjectName("editPasteAction")
        self.helpAction = QtWidgets.QAction(RegexReferenceWindowBA)
        self.helpAction.setProperty("name", "helpAction")
        self.helpAction.setObjectName("helpAction")
        self.helpPythonAction = QtWidgets.QAction(RegexReferenceWindowBA)
        self.helpPythonAction.setProperty("name", "helpPythonAction")
        self.helpPythonAction.setObjectName("helpPythonAction")

        self.retranslateUi(RegexReferenceWindowBA)
        self.referenceTreeWidget.doubleClicked['QModelIndex'].connect(RegexReferenceWindowBA.editPaste)
        QtCore.QMetaObject.connectSlotsByName(RegexReferenceWindowBA)

    def retranslateUi(self, RegexReferenceWindowBA):
        _translate = QtCore.QCoreApplication.translate
        RegexReferenceWindowBA.setWindowTitle(_translate("RegexReferenceWindowBA", "Kang - Regex Reference Guide"))
        self.referenceTreeWidget.headerItem().setText(0, _translate("RegexReferenceWindowBA", "Symbol"))
        self.referenceTreeWidget.headerItem().setText(1, _translate("RegexReferenceWindowBA", "Definition"))
        self.fileExitAction.setText(_translate("RegexReferenceWindowBA", "E&xit"))
        self.fileExitAction.setIconText(_translate("RegexReferenceWindowBA", "Exit"))
        self.editPasteAction.setText(_translate("RegexReferenceWindowBA", "&Paste"))
        self.editPasteAction.setIconText(_translate("RegexReferenceWindowBA", "Paste"))
        self.editPasteAction.setToolTip(_translate("RegexReferenceWindowBA", "Paste selection into Kang"))
        self.editPasteAction.setShortcut(_translate("RegexReferenceWindowBA", "Ctrl+V"))
        self.helpAction.setText(_translate("RegexReferenceWindowBA", "&Help"))
        self.helpAction.setIconText(_translate("RegexReferenceWindowBA", "Help"))
        self.helpPythonAction.setText(_translate("RegexReferenceWindowBA", "&Python Regex Help"))
        self.helpPythonAction.setIconText(_translate("RegexReferenceWindowBA", "Python Regex Help"))
