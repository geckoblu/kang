# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helpBA4.ui'
#
# Created: Mon Jan 20 15:21:40 2014
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

class Ui_HelpBA(object):
    def setupUi(self, HelpBA):
        HelpBA.setObjectName(_fromUtf8("HelpBA"))
        HelpBA.resize(494, 585)
        self.widget = QtGui.QWidget(HelpBA)
        self.widget.setObjectName(_fromUtf8("widget"))
        HelpBA.setCentralWidget(self.widget)
        self.toolBar = QtGui.QToolBar(HelpBA)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        HelpBA.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menubar = QtGui.QMenuBar(HelpBA)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 494, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.fileMenu = QtGui.QMenu(self.menubar)
        self.fileMenu.setObjectName(_fromUtf8("fileMenu"))
        HelpBA.setMenuBar(self.menubar)
        self.fileHomeAction = QtGui.QAction(HelpBA)
        self.fileHomeAction.setProperty("name", _fromUtf8("fileHomeAction"))
        self.fileHomeAction.setObjectName(_fromUtf8("fileHomeAction"))
        self.fileBackAction = QtGui.QAction(HelpBA)
        self.fileBackAction.setProperty("name", _fromUtf8("fileBackAction"))
        self.fileBackAction.setObjectName(_fromUtf8("fileBackAction"))
        self.fileForwardAction = QtGui.QAction(HelpBA)
        self.fileForwardAction.setProperty("name", _fromUtf8("fileForwardAction"))
        self.fileForwardAction.setObjectName(_fromUtf8("fileForwardAction"))
        self.fileExitAction = QtGui.QAction(HelpBA)
        self.fileExitAction.setProperty("name", _fromUtf8("fileExitAction"))
        self.fileExitAction.setObjectName(_fromUtf8("fileExitAction"))
        self.toolBar.addAction(self.fileBackAction)
        self.toolBar.addAction(self.fileForwardAction)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.fileHomeAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.fileHomeAction)
        self.fileMenu.addAction(self.fileBackAction)
        self.fileMenu.addAction(self.fileForwardAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.fileExitAction)
        self.menubar.addAction(self.fileMenu.menuAction())

        self.retranslateUi(HelpBA)
        QtCore.QObject.connect(self.fileExitAction, QtCore.SIGNAL(_fromUtf8("activated()")), HelpBA.exitSlot)
        QtCore.QObject.connect(self.fileBackAction, QtCore.SIGNAL(_fromUtf8("activated()")), HelpBA.backSlot)
        QtCore.QObject.connect(self.fileForwardAction, QtCore.SIGNAL(_fromUtf8("activated()")), HelpBA.forwardSlot)
        QtCore.QObject.connect(self.fileHomeAction, QtCore.SIGNAL(_fromUtf8("activated()")), HelpBA.homeSlot)
        QtCore.QMetaObject.connectSlotsByName(HelpBA)

    def retranslateUi(self, HelpBA):
        HelpBA.setWindowTitle(_translate("HelpBA", "MainWindow", None))
        self.toolBar.setProperty("label", _translate("HelpBA", "Tools", None))
        self.fileMenu.setTitle(_translate("HelpBA", "&File", None))
        self.fileHomeAction.setText(_translate("HelpBA", "Home", None))
        self.fileHomeAction.setIconText(_translate("HelpBA", "Home", None))
        self.fileHomeAction.setShortcut(_translate("HelpBA", "Ctrl+H", None))
        self.fileBackAction.setText(_translate("HelpBA", "Back", None))
        self.fileBackAction.setIconText(_translate("HelpBA", "Back", None))
        self.fileBackAction.setShortcut(_translate("HelpBA", "Ctrl+B", None))
        self.fileForwardAction.setText(_translate("HelpBA", "Forward", None))
        self.fileForwardAction.setIconText(_translate("HelpBA", "Forward", None))
        self.fileForwardAction.setShortcut(_translate("HelpBA", "Ctrl+F", None))
        self.fileExitAction.setText(_translate("HelpBA", "Exit", None))
        self.fileExitAction.setIconText(_translate("HelpBA", "Exit", None))
        self.fileExitAction.setShortcut(_translate("HelpBA", "Ctrl+Q", None))


class HelpBA(QtGui.QMainWindow, Ui_HelpBA):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)

        self.setupUi(self)

