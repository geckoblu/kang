# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/regexReferenceWindowBA4.ui'
#
# Created: Tue Sep  9 16:04:33 2014
#      by: PySide2 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

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


class Ui_RegexReferenceWindowBA(object):

    def setupUi(self, RegexReferenceWindowBA):
        RegexReferenceWindowBA.setObjectName(_fromUtf8("RegexReferenceWindowBA"))
        RegexReferenceWindowBA.resize(600, 605)
        self.widget = QWidget(RegexReferenceWindowBA)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridlayout = QGridLayout(self.widget)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.referenceTreeWidget = QTreeWidget(self.widget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.referenceTreeWidget.sizePolicy().hasHeightForWidth())
        self.referenceTreeWidget.setSizePolicy(sizePolicy)
        self.referenceTreeWidget.setFrameShape(QFrame.StyledPanel)
        self.referenceTreeWidget.setFrameShadow(QFrame.Sunken)
        self.referenceTreeWidget.setObjectName(_fromUtf8("referenceTreeWidget"))
        self.gridlayout.addWidget(self.referenceTreeWidget, 0, 0, 1, 1)
        RegexReferenceWindowBA.setCentralWidget(self.widget)
        self.fileExitAction = QAction(RegexReferenceWindowBA)
        self.fileExitAction.setShortcut(_fromUtf8(""))
        self.fileExitAction.setProperty("name", _fromUtf8("fileExitAction"))
        self.fileExitAction.setObjectName(_fromUtf8("fileExitAction"))
        self.editPasteAction = QAction(RegexReferenceWindowBA)
        self.editPasteAction.setProperty("name", _fromUtf8("editPasteAction"))
        self.editPasteAction.setObjectName(_fromUtf8("editPasteAction"))
        self.helpAction = QAction(RegexReferenceWindowBA)
        self.helpAction.setProperty("name", _fromUtf8("helpAction"))
        self.helpAction.setObjectName(_fromUtf8("helpAction"))
        self.helpPythonAction = QAction(RegexReferenceWindowBA)
        self.helpPythonAction.setProperty("name", _fromUtf8("helpPythonAction"))
        self.helpPythonAction.setObjectName(_fromUtf8("helpPythonAction"))

        self.retranslateUi(RegexReferenceWindowBA)
        QObject.connect(self.referenceTreeWidget, SIGNAL(_fromUtf8("doubleClicked(QModelIndex)")), RegexReferenceWindowBA.editPaste)
        QMetaObject.connectSlotsByName(RegexReferenceWindowBA)

    def retranslateUi(self, RegexReferenceWindowBA):
        RegexReferenceWindowBA.setWindowTitle(_translate("RegexReferenceWindowBA", "Kang - Regex Reference Guide", None))
        self.referenceTreeWidget.headerItem().setText(0, _translate("RegexReferenceWindowBA", "Symbol", None))
        self.referenceTreeWidget.headerItem().setText(1, _translate("RegexReferenceWindowBA", "Definition", None))
        self.fileExitAction.setText(_translate("RegexReferenceWindowBA", "E&xit", None))
        self.fileExitAction.setIconText(_translate("RegexReferenceWindowBA", "Exit", None))
        self.editPasteAction.setText(_translate("RegexReferenceWindowBA", "&Paste", None))
        self.editPasteAction.setIconText(_translate("RegexReferenceWindowBA", "Paste", None))
        self.editPasteAction.setToolTip(_translate("RegexReferenceWindowBA", "Paste selection into Kang", None))
        self.editPasteAction.setShortcut(_translate("RegexReferenceWindowBA", "Ctrl+V", None))
        self.helpAction.setText(_translate("RegexReferenceWindowBA", "&Help", None))
        self.helpAction.setIconText(_translate("RegexReferenceWindowBA", "Help", None))
        self.helpPythonAction.setText(_translate("RegexReferenceWindowBA", "&Python Regex Help", None))
        self.helpPythonAction.setIconText(_translate("RegexReferenceWindowBA", "Python Regex Help", None))


class RegexReferenceWindowBA(QMainWindow, Ui_RegexReferenceWindowBA):

    def __init__(self, parent=None, f=Qt.WindowFlags()):
        QMainWindow.__init__(self, parent, f)

        self.setupUi(self)

