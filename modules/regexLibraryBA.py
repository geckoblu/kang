# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'regexLibraryBA4.ui'
#
# Created: Tue Aug  5 07:45:41 2014
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

class Ui_RegexLibraryBA(object):
    def setupUi(self, RegexLibraryBA):
        RegexLibraryBA.setObjectName(_fromUtf8("RegexLibraryBA"))
        RegexLibraryBA.resize(530, 600)
        self.widget = QtGui.QWidget(RegexLibraryBA)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridlayout = QtGui.QGridLayout(self.widget)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.groupBox = QtGui.QGroupBox(self.widget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.descriptionListBox = QtGui.QListWidget(self.groupBox)
        self.descriptionListBox.setObjectName(_fromUtf8("descriptionListBox"))
        self.gridLayout.addWidget(self.descriptionListBox, 0, 0, 1, 1)
        self.gridlayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.widget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.regexTextBrowser = QtGui.QTextBrowser(self.tab)
        self.regexTextBrowser.setObjectName(_fromUtf8("regexTextBrowser"))
        self.gridLayout_2.addWidget(self.regexTextBrowser, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.noteTextBrowser = QtGui.QTextBrowser(self.tab_2)
        self.noteTextBrowser.setObjectName(_fromUtf8("noteTextBrowser"))
        self.gridLayout_3.addWidget(self.noteTextBrowser, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.contribEdit = QtGui.QLineEdit(self.tab_2)
        self.contribEdit.setObjectName(_fromUtf8("contribEdit"))
        self.horizontalLayout_2.addWidget(self.contribEdit)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridlayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        RegexLibraryBA.setCentralWidget(self.widget)
        self.menubar = QtGui.QMenuBar(RegexLibraryBA)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 530, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        RegexLibraryBA.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(RegexLibraryBA)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        RegexLibraryBA.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.editPasteAction = QtGui.QAction(RegexLibraryBA)
        self.editPasteAction.setProperty("name", _fromUtf8("editPasteAction"))
        self.editPasteAction.setObjectName(_fromUtf8("editPasteAction"))
        self.helpHelpAction = QtGui.QAction(RegexLibraryBA)
        self.helpHelpAction.setProperty("name", _fromUtf8("helpHelpAction"))
        self.helpHelpAction.setObjectName(_fromUtf8("helpHelpAction"))
        self.exitAction = QtGui.QAction(RegexLibraryBA)
        self.exitAction.setProperty("name", _fromUtf8("exitAction"))
        self.exitAction.setObjectName(_fromUtf8("exitAction"))
        self.menuFile.addAction(self.exitAction)
        self.menuEdit.addAction(self.editPasteAction)
        self.menuHelp.addAction(self.helpHelpAction)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.editPasteAction)

        self.retranslateUi(RegexLibraryBA)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.editPasteAction, QtCore.SIGNAL(_fromUtf8("activated()")), RegexLibraryBA.editPaste)
        QtCore.QObject.connect(self.exitAction, QtCore.SIGNAL(_fromUtf8("activated()")), RegexLibraryBA.close)
        QtCore.QObject.connect(self.descriptionListBox, QtCore.SIGNAL(_fromUtf8("itemClicked(QListWidgetItem*)")), RegexLibraryBA.descSelectedSlot)
        QtCore.QObject.connect(self.descriptionListBox, QtCore.SIGNAL(_fromUtf8("doubleClicked(QModelIndex)")), RegexLibraryBA.editPaste)
        QtCore.QMetaObject.connectSlotsByName(RegexLibraryBA)

    def retranslateUi(self, RegexLibraryBA):
        RegexLibraryBA.setWindowTitle(_translate("RegexLibraryBA", "Kang - Regex Library", None))
        self.groupBox.setTitle(_translate("RegexLibraryBA", "Description", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("RegexLibraryBA", "Regex", None))
        self.label.setText(_translate("RegexLibraryBA", "Contributed By:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("RegexLibraryBA", "Notes", None))
        self.menuFile.setTitle(_translate("RegexLibraryBA", "&File", None))
        self.menuEdit.setTitle(_translate("RegexLibraryBA", "&Edit", None))
        self.menuHelp.setTitle(_translate("RegexLibraryBA", "&Help", None))
        self.toolBar.setWindowTitle(_translate("RegexLibraryBA", "toolBar", None))
        self.editPasteAction.setText(_translate("RegexLibraryBA", "&Paste Example Into Kang", None))
        self.editPasteAction.setIconText(_translate("RegexLibraryBA", "Paste", None))
        self.editPasteAction.setToolTip(_translate("RegexLibraryBA", "Paste This Example Into Kang", None))
        self.editPasteAction.setShortcut(_translate("RegexLibraryBA", "Ctrl+V", None))
        self.helpHelpAction.setText(_translate("RegexLibraryBA", "&Help", None))
        self.helpHelpAction.setIconText(_translate("RegexLibraryBA", "Help", None))
        self.helpHelpAction.setShortcut(_translate("RegexLibraryBA", "Ctrl+/", None))
        self.exitAction.setText(_translate("RegexLibraryBA", "&Exit", None))
        self.exitAction.setIconText(_translate("RegexLibraryBA", "Exit", None))


class RegexLibraryBA(QtGui.QMainWindow, Ui_RegexLibraryBA):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)

        self.setupUi(self)

