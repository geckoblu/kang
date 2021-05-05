# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'regexLibraryWindowBA.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegexLibraryWindowBA(object):
    def setupUi(self, RegexLibraryWindowBA):
        RegexLibraryWindowBA.setObjectName("RegexLibraryWindowBA")
        RegexLibraryWindowBA.resize(530, 600)
        self.widget = QtWidgets.QWidget(RegexLibraryWindowBA)
        self.widget.setObjectName("widget")
        self.gridlayout = QtWidgets.QGridLayout(self.widget)
        self.gridlayout.setObjectName("gridlayout")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.descriptionListBox = QtWidgets.QListWidget(self.groupBox)
        self.descriptionListBox.setObjectName("descriptionListBox")
        self.gridLayout.addWidget(self.descriptionListBox, 0, 0, 1, 1)
        self.gridlayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.widget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.regexTextBrowser = QtWidgets.QTextBrowser(self.tab)
        self.regexTextBrowser.setObjectName("regexTextBrowser")
        self.gridLayout_2.addWidget(self.regexTextBrowser, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.noteTextBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.noteTextBrowser.setObjectName("noteTextBrowser")
        self.gridLayout_3.addWidget(self.noteTextBrowser, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.contribEdit = QtWidgets.QLineEdit(self.tab_2)
        self.contribEdit.setObjectName("contribEdit")
        self.horizontalLayout_2.addWidget(self.contribEdit)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridlayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        RegexLibraryWindowBA.setCentralWidget(self.widget)
        self.editPasteAction = QtWidgets.QAction(RegexLibraryWindowBA)
        self.editPasteAction.setProperty("name", "editPasteAction")
        self.editPasteAction.setObjectName("editPasteAction")
        self.helpHelpAction = QtWidgets.QAction(RegexLibraryWindowBA)
        self.helpHelpAction.setProperty("name", "helpHelpAction")
        self.helpHelpAction.setObjectName("helpHelpAction")
        self.exitAction = QtWidgets.QAction(RegexLibraryWindowBA)
        self.exitAction.setProperty("name", "exitAction")
        self.exitAction.setObjectName("exitAction")

        self.retranslateUi(RegexLibraryWindowBA)
        self.tabWidget.setCurrentIndex(0)
        self.descriptionListBox.itemClicked['QListWidgetItem*'].connect(RegexLibraryWindowBA.descSelectedSlot)
        self.descriptionListBox.doubleClicked['QModelIndex'].connect(RegexLibraryWindowBA.editPaste)
        QtCore.QMetaObject.connectSlotsByName(RegexLibraryWindowBA)

    def retranslateUi(self, RegexLibraryWindowBA):
        _translate = QtCore.QCoreApplication.translate
        RegexLibraryWindowBA.setWindowTitle(_translate("RegexLibraryWindowBA", "Kang - Regex Library"))
        self.groupBox.setTitle(_translate("RegexLibraryWindowBA", "Description"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("RegexLibraryWindowBA", "Regex"))
        self.label.setText(_translate("RegexLibraryWindowBA", "Contributed By:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("RegexLibraryWindowBA", "Notes"))
        self.editPasteAction.setText(_translate("RegexLibraryWindowBA", "&Paste Example Into Kang"))
        self.editPasteAction.setIconText(_translate("RegexLibraryWindowBA", "Paste"))
        self.editPasteAction.setToolTip(_translate("RegexLibraryWindowBA", "Paste This Example Into Kang"))
        self.editPasteAction.setShortcut(_translate("RegexLibraryWindowBA", "Ctrl+V"))
        self.helpHelpAction.setText(_translate("RegexLibraryWindowBA", "&Help"))
        self.helpHelpAction.setIconText(_translate("RegexLibraryWindowBA", "Help"))
        self.helpHelpAction.setShortcut(_translate("RegexLibraryWindowBA", "Ctrl+/"))
        self.exitAction.setText(_translate("RegexLibraryWindowBA", "&Exit"))
        self.exitAction.setIconText(_translate("RegexLibraryWindowBA", "Exit"))
