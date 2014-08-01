# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'referenceBA4.ui'
#
# Created: Wed Jul 30 09:25:22 2014
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

class Ui_ReferenceBA(object):
    def setupUi(self, ReferenceBA):
        ReferenceBA.setObjectName(_fromUtf8("ReferenceBA"))
        ReferenceBA.resize(600, 605)
        self.widget = QtGui.QWidget(ReferenceBA)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridlayout = QtGui.QGridLayout(self.widget)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.referenceTreeWidget = QtGui.QTreeWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.referenceTreeWidget.sizePolicy().hasHeightForWidth())
        self.referenceTreeWidget.setSizePolicy(sizePolicy)
        self.referenceTreeWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.referenceTreeWidget.setFrameShadow(QtGui.QFrame.Sunken)
        self.referenceTreeWidget.setObjectName(_fromUtf8("referenceTreeWidget"))
        self.gridlayout.addWidget(self.referenceTreeWidget, 0, 0, 1, 1)
        ReferenceBA.setCentralWidget(self.widget)
        self.toolBar = QtGui.QToolBar(ReferenceBA)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        ReferenceBA.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.MenuBar = QtGui.QMenuBar(ReferenceBA)
        self.MenuBar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.MenuBar.setObjectName(_fromUtf8("MenuBar"))
        self.fileMenu = QtGui.QMenu(self.MenuBar)
        self.fileMenu.setObjectName(_fromUtf8("fileMenu"))
        self.editMenu = QtGui.QMenu(self.MenuBar)
        self.editMenu.setObjectName(_fromUtf8("editMenu"))
        self.helpMenu = QtGui.QMenu(self.MenuBar)
        self.helpMenu.setObjectName(_fromUtf8("helpMenu"))
        ReferenceBA.setMenuBar(self.MenuBar)
        self.fileExitAction = QtGui.QAction(ReferenceBA)
        self.fileExitAction.setShortcut(_fromUtf8(""))
        self.fileExitAction.setProperty("name", _fromUtf8("fileExitAction"))
        self.fileExitAction.setObjectName(_fromUtf8("fileExitAction"))
        self.editPasteAction = QtGui.QAction(ReferenceBA)
        self.editPasteAction.setProperty("name", _fromUtf8("editPasteAction"))
        self.editPasteAction.setObjectName(_fromUtf8("editPasteAction"))
        self.helpAction = QtGui.QAction(ReferenceBA)
        self.helpAction.setProperty("name", _fromUtf8("helpAction"))
        self.helpAction.setObjectName(_fromUtf8("helpAction"))
        self.helpPythonAction = QtGui.QAction(ReferenceBA)
        self.helpPythonAction.setProperty("name", _fromUtf8("helpPythonAction"))
        self.helpPythonAction.setObjectName(_fromUtf8("helpPythonAction"))
        self.toolBar.addAction(self.editPasteAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.fileExitAction)
        self.editMenu.addAction(self.editPasteAction)
        self.editMenu.addSeparator()
        self.helpMenu.addAction(self.helpAction)
        self.helpMenu.addAction(self.helpPythonAction)
        self.MenuBar.addAction(self.fileMenu.menuAction())
        self.MenuBar.addAction(self.editMenu.menuAction())
        self.MenuBar.addAction(self.helpMenu.menuAction())

        self.retranslateUi(ReferenceBA)
        QtCore.QObject.connect(self.fileExitAction, QtCore.SIGNAL(_fromUtf8("activated()")), ReferenceBA.close)
        QtCore.QObject.connect(self.editPasteAction, QtCore.SIGNAL(_fromUtf8("activated()")), ReferenceBA.editPaste)
        QtCore.QObject.connect(self.helpAction, QtCore.SIGNAL(_fromUtf8("activated()")), ReferenceBA.help_slot)
        QtCore.QObject.connect(self.helpPythonAction, QtCore.SIGNAL(_fromUtf8("activated()")), ReferenceBA.help_python_slot)
        QtCore.QObject.connect(self.referenceTreeWidget, QtCore.SIGNAL(_fromUtf8("doubleClicked(QModelIndex)")), ReferenceBA.editPaste)
        QtCore.QMetaObject.connectSlotsByName(ReferenceBA)

    def retranslateUi(self, ReferenceBA):
        ReferenceBA.setWindowTitle(_translate("ReferenceBA", "Kodos - Regex Reference Guide", None))
        self.referenceTreeWidget.headerItem().setText(0, _translate("ReferenceBA", "Symbol", None))
        self.referenceTreeWidget.headerItem().setText(1, _translate("ReferenceBA", "Definition", None))
        self.toolBar.setProperty("label", _translate("ReferenceBA", "Tools", None))
        self.fileMenu.setTitle(_translate("ReferenceBA", "&File", None))
        self.editMenu.setTitle(_translate("ReferenceBA", "&Edit", None))
        self.helpMenu.setTitle(_translate("ReferenceBA", "&Help", None))
        self.fileExitAction.setText(_translate("ReferenceBA", "E&xit", None))
        self.fileExitAction.setIconText(_translate("ReferenceBA", "Exit", None))
        self.editPasteAction.setText(_translate("ReferenceBA", "&Paste", None))
        self.editPasteAction.setIconText(_translate("ReferenceBA", "Paste", None))
        self.editPasteAction.setToolTip(_translate("ReferenceBA", "Paste selection into Kodos", None))
        self.editPasteAction.setShortcut(_translate("ReferenceBA", "Ctrl+V", None))
        self.helpAction.setText(_translate("ReferenceBA", "&Help", None))
        self.helpAction.setIconText(_translate("ReferenceBA", "Help", None))
        self.helpPythonAction.setText(_translate("ReferenceBA", "&Python Regex Help", None))
        self.helpPythonAction.setIconText(_translate("ReferenceBA", "Python Regex Help", None))


class ReferenceBA(QtGui.QMainWindow, Ui_ReferenceBA):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)

        self.setupUi(self)

