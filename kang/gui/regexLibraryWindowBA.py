# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'regexLibraryWindowBA4.ui'
#
# Created: Tue Sep  9 16:14:27 2014
#      by: PySide2 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
# pylint: disable=all
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


class Ui_RegexLibraryWindowBA(object):

    def setupUi(self, RegexLibraryWindowBA):
        RegexLibraryWindowBA.setObjectName(_fromUtf8("RegexLibraryWindowBA"))
        RegexLibraryWindowBA.resize(530, 600)
        self.widget = QWidget(RegexLibraryWindowBA)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridlayout = QGridLayout(self.widget)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.descriptionListBox = QListWidget(self.groupBox)
        self.descriptionListBox.setObjectName(_fromUtf8("descriptionListBox"))
        self.gridLayout.addWidget(self.descriptionListBox, 0, 0, 1, 1)
        self.gridlayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tabWidget = QTabWidget(self.widget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.regexTextBrowser = QTextBrowser(self.tab)
        self.regexTextBrowser.setObjectName(_fromUtf8("regexTextBrowser"))
        self.gridLayout_2.addWidget(self.regexTextBrowser, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.noteTextBrowser = QTextBrowser(self.tab_2)
        self.noteTextBrowser.setObjectName(_fromUtf8("noteTextBrowser"))
        self.gridLayout_3.addWidget(self.noteTextBrowser, 0, 0, 1, 1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.contribEdit = QLineEdit(self.tab_2)
        self.contribEdit.setObjectName(_fromUtf8("contribEdit"))
        self.horizontalLayout_2.addWidget(self.contribEdit)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridlayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        RegexLibraryWindowBA.setCentralWidget(self.widget)
        self.editPasteAction = QAction(RegexLibraryWindowBA)
        self.editPasteAction.setProperty("name", _fromUtf8("editPasteAction"))
        self.editPasteAction.setObjectName(_fromUtf8("editPasteAction"))
        self.helpHelpAction = QAction(RegexLibraryWindowBA)
        self.helpHelpAction.setProperty("name", _fromUtf8("helpHelpAction"))
        self.helpHelpAction.setObjectName(_fromUtf8("helpHelpAction"))
        self.exitAction = QAction(RegexLibraryWindowBA)
        self.exitAction.setProperty("name", _fromUtf8("exitAction"))
        self.exitAction.setObjectName(_fromUtf8("exitAction"))

        self.retranslateUi(RegexLibraryWindowBA)
        self.tabWidget.setCurrentIndex(0)
        QObject.connect(self.descriptionListBox, SIGNAL(_fromUtf8("itemClicked(QListWidgetItem*)")), RegexLibraryWindowBA.descSelectedSlot)
        QObject.connect(self.descriptionListBox, SIGNAL(_fromUtf8("doubleClicked(QModelIndex)")), RegexLibraryWindowBA.editPaste)
        QMetaObject.connectSlotsByName(RegexLibraryWindowBA)

    def retranslateUi(self, RegexLibraryWindowBA):
        RegexLibraryWindowBA.setWindowTitle(_translate("RegexLibraryWindowBA", "Kang - Regex Library", None))
        self.groupBox.setTitle(_translate("RegexLibraryWindowBA", "Description", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("RegexLibraryWindowBA", "Regex", None))
        self.label.setText(_translate("RegexLibraryWindowBA", "Contributed By:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("RegexLibraryWindowBA", "Notes", None))
        self.editPasteAction.setText(_translate("RegexLibraryWindowBA", "&Paste Example Into Kang", None))
        self.editPasteAction.setIconText(_translate("RegexLibraryWindowBA", "Paste", None))
        self.editPasteAction.setToolTip(_translate("RegexLibraryWindowBA", "Paste This Example Into Kang", None))
        self.editPasteAction.setShortcut(_translate("RegexLibraryWindowBA", "Ctrl+V", None))
        self.helpHelpAction.setText(_translate("RegexLibraryWindowBA", "&Help", None))
        self.helpHelpAction.setIconText(_translate("RegexLibraryWindowBA", "Help", None))
        self.helpHelpAction.setShortcut(_translate("RegexLibraryWindowBA", "Ctrl+/", None))
        self.exitAction.setText(_translate("RegexLibraryWindowBA", "&Exit", None))
        self.exitAction.setIconText(_translate("RegexLibraryWindowBA", "Exit", None))


class RegexLibraryWindowBA(QMainWindow, Ui_RegexLibraryWindowBA):

    def __init__(self, parent=None, f=Qt.WindowFlags()):
        QMainWindow.__init__(self, parent, f)

        self.setupUi(self)
