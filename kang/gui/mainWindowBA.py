# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindowBA.ui'
#
# Created: Fri May  8 09:14:50 2015
#      by: PyQt5 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui

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

class Ui_MainWindowBA(object):
    def setupUi(self, MainWindowBA):
        MainWindowBA.setObjectName(_fromUtf8("MainWindowBA"))
        MainWindowBA.resize(497, 718)
        self.widget = QtGui.QWidget(MainWindowBA)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridlayout = QtGui.QGridLayout(self.widget)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.groupBox2 = QtGui.QGroupBox(self.widget)
        self.groupBox2.setCheckable(False)
        self.groupBox2.setObjectName(_fromUtf8("groupBox2"))
        self.buttonGroup2 = QtGui.QButtonGroup(self.groupBox2)
        self.buttonGroup2.setObjectName(_fromUtf8("buttonGroup2"))
        self.hboxlayout = QtGui.QHBoxLayout(self.groupBox2)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.ignorecaseCheckBox = QtGui.QCheckBox(self.groupBox2)
        self.ignorecaseCheckBox.setObjectName(_fromUtf8("ignorecaseCheckBox"))
        self.hboxlayout.addWidget(self.ignorecaseCheckBox)
        self.multilineCheckBox = QtGui.QCheckBox(self.groupBox2)
        self.multilineCheckBox.setObjectName(_fromUtf8("multilineCheckBox"))
        self.hboxlayout.addWidget(self.multilineCheckBox)
        self.dotallCheckBox = QtGui.QCheckBox(self.groupBox2)
        self.dotallCheckBox.setObjectName(_fromUtf8("dotallCheckBox"))
        self.hboxlayout.addWidget(self.dotallCheckBox)
        self.verboseCheckBox = QtGui.QCheckBox(self.groupBox2)
        self.verboseCheckBox.setObjectName(_fromUtf8("verboseCheckBox"))
        self.hboxlayout.addWidget(self.verboseCheckBox)
        self.localeCheckBox = QtGui.QCheckBox(self.groupBox2)
        self.localeCheckBox.setObjectName(_fromUtf8("localeCheckBox"))
        self.hboxlayout.addWidget(self.localeCheckBox)
        self.unicodeCheckBox = QtGui.QCheckBox(self.groupBox2)
        self.unicodeCheckBox.setObjectName(_fromUtf8("unicodeCheckBox"))
        self.hboxlayout.addWidget(self.unicodeCheckBox)
        self.gridlayout.addWidget(self.groupBox2, 1, 0, 1, 1)
        self.groupBox1 = QtGui.QGroupBox(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox1.sizePolicy().hasHeightForWidth())
        self.groupBox1.setSizePolicy(sizePolicy)
        self.groupBox1.setCheckable(False)
        self.groupBox1.setProperty("lineWidth", 1)
        self.groupBox1.setObjectName(_fromUtf8("groupBox1"))
        self.gridlayout1 = QtGui.QGridLayout(self.groupBox1)
        self.gridlayout1.setObjectName(_fromUtf8("gridlayout1"))
        self.regexMultiLineEdit = QtGui.QTextEdit(self.groupBox1)
        self.regexMultiLineEdit.setProperty("text", _fromUtf8(""))
        self.regexMultiLineEdit.setObjectName(_fromUtf8("regexMultiLineEdit"))
        self.gridlayout1.addWidget(self.regexMultiLineEdit, 0, 0, 1, 1)
        self.gridlayout.addWidget(self.groupBox1, 0, 0, 1, 1)
        self.resultTabWidget = QtGui.QTabWidget(self.widget)
        self.resultTabWidget.setObjectName(_fromUtf8("resultTabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridlayout2 = QtGui.QGridLayout(self.tab)
        self.gridlayout2.setObjectName(_fromUtf8("gridlayout2"))
        self.groupTable = QtGui.QTableWidget(self.tab)
        self.groupTable.setColumnCount(2)
        self.groupTable.setObjectName(_fromUtf8("groupTable"))
        self.groupTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.groupTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.groupTable.setHorizontalHeaderItem(1, item)
        self.gridlayout2.addWidget(self.groupTable, 0, 0, 1, 1)
        self.resultTabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self.gridlayout3 = QtGui.QGridLayout(self.tab1)
        self.gridlayout3.setObjectName(_fromUtf8("gridlayout3"))
        self.matchTextBrowser = QtGui.QTextBrowser(self.tab1)
        self.matchTextBrowser.setObjectName(_fromUtf8("matchTextBrowser"))
        self.gridlayout3.addWidget(self.matchTextBrowser, 0, 0, 1, 1)
        self.resultTabWidget.addTab(self.tab1, _fromUtf8(""))
        self.TabPage = QtGui.QWidget()
        self.TabPage.setObjectName(_fromUtf8("TabPage"))
        self.gridlayout4 = QtGui.QGridLayout(self.TabPage)
        self.gridlayout4.setObjectName(_fromUtf8("gridlayout4"))
        self.matchAllTextBrowser = QtGui.QTextBrowser(self.TabPage)
        self.matchAllTextBrowser.setObjectName(_fromUtf8("matchAllTextBrowser"))
        self.gridlayout4.addWidget(self.matchAllTextBrowser, 0, 0, 1, 1)
        self.resultTabWidget.addTab(self.TabPage, _fromUtf8(""))
        self.TabPage1 = QtGui.QWidget()
        self.TabPage1.setObjectName(_fromUtf8("TabPage1"))
        self.vboxlayout = QtGui.QVBoxLayout(self.TabPage1)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.replaceTextBrowser = QtGui.QTextBrowser(self.TabPage1)
        self.replaceTextBrowser.setObjectName(_fromUtf8("replaceTextBrowser"))
        self.vboxlayout.addWidget(self.replaceTextBrowser)
        self.resultTabWidget.addTab(self.TabPage1, _fromUtf8(""))
        self.TabPage2 = QtGui.QWidget()
        self.TabPage2.setObjectName(_fromUtf8("TabPage2"))
        self.gridlayout5 = QtGui.QGridLayout(self.TabPage2)
        self.gridlayout5.setObjectName(_fromUtf8("gridlayout5"))
        self.codeTextBrowser = QtGui.QTextBrowser(self.TabPage2)
        self.codeTextBrowser.setObjectName(_fromUtf8("codeTextBrowser"))
        self.gridlayout5.addWidget(self.codeTextBrowser, 0, 0, 1, 1)
        self.resultTabWidget.addTab(self.TabPage2, _fromUtf8(""))
        self.gridlayout.addWidget(self.resultTabWidget, 4, 0, 1, 1)
        self.tabWidget3 = QtGui.QTabWidget(self.widget)
        self.tabWidget3.setObjectName(_fromUtf8("tabWidget3"))
        self.tab2 = QtGui.QWidget()
        self.tab2.setObjectName(_fromUtf8("tab2"))
        self.gridlayout6 = QtGui.QGridLayout(self.tab2)
        self.gridlayout6.setObjectName(_fromUtf8("gridlayout6"))
        self.stringMultiLineEdit = QtGui.QTextEdit(self.tab2)
        self.stringMultiLineEdit.setObjectName(_fromUtf8("stringMultiLineEdit"))
        self.gridlayout6.addWidget(self.stringMultiLineEdit, 0, 0, 1, 1)
        self.tabWidget3.addTab(self.tab2, _fromUtf8(""))
        self.tab3 = QtGui.QWidget()
        self.tab3.setObjectName(_fromUtf8("tab3"))
        self.gridlayout7 = QtGui.QGridLayout(self.tab3)
        self.gridlayout7.setObjectName(_fromUtf8("gridlayout7"))
        self.replaceTextEdit = QtGui.QTextEdit(self.tab3)
        self.replaceTextEdit.setObjectName(_fromUtf8("replaceTextEdit"))
        self.gridlayout7.addWidget(self.replaceTextEdit, 0, 0, 1, 1)
        self.tabWidget3.addTab(self.tab3, _fromUtf8(""))
        self.gridlayout.addWidget(self.tabWidget3, 2, 0, 1, 1)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))
        spacerItem = QtGui.QSpacerItem(70, 31, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)
        self.textLabel1 = QtGui.QLabel(self.widget)
        self.textLabel1.setWordWrap(False)
        self.textLabel1.setObjectName(_fromUtf8("textLabel1"))
        self.hboxlayout1.addWidget(self.textLabel1)
        self.matchNumberSpinBox = QtGui.QSpinBox(self.widget)
        self.matchNumberSpinBox.setMinimum(1)
        self.matchNumberSpinBox.setMaximum(9999)
        self.matchNumberSpinBox.setObjectName(_fromUtf8("matchNumberSpinBox"))
        self.hboxlayout1.addWidget(self.matchNumberSpinBox)
        self.spacerLabel = QtGui.QLabel(self.widget)
        self.spacerLabel.setPixmap(QtGui.QPixmap(_fromUtf8("image1")))
        self.spacerLabel.setWordWrap(False)
        self.spacerLabel.setObjectName(_fromUtf8("spacerLabel"))
        self.hboxlayout1.addWidget(self.spacerLabel)
        self.replaceLabel = QtGui.QLabel(self.widget)
        self.replaceLabel.setWordWrap(False)
        self.replaceLabel.setObjectName(_fromUtf8("replaceLabel"))
        self.hboxlayout1.addWidget(self.replaceLabel)
        self.replaceNumberSpinBox = QtGui.QSpinBox(self.widget)
        self.replaceNumberSpinBox.setObjectName(_fromUtf8("replaceNumberSpinBox"))
        self.hboxlayout1.addWidget(self.replaceNumberSpinBox)
        spacerItem1 = QtGui.QSpacerItem(118, 21, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem1)
        self.gridlayout.addLayout(self.hboxlayout1, 3, 0, 1, 1)
        MainWindowBA.setCentralWidget(self.widget)
        self.toolBar = QtGui.QToolBar(MainWindowBA)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindowBA.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menubar = QtGui.QMenuBar(MainWindowBA)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 497, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.fileMenu = QtGui.QMenu(self.menubar)
        self.fileMenu.setObjectName(_fromUtf8("fileMenu"))
        self.editMenu = QtGui.QMenu(self.menubar)
        self.editMenu.setObjectName(_fromUtf8("editMenu"))
        self.helpMenu = QtGui.QMenu(self.menubar)
        self.helpMenu.setObjectName(_fromUtf8("helpMenu"))
        MainWindowBA.setMenuBar(self.menubar)
        self.fileNewAction = QtGui.QAction(MainWindowBA)
        self.fileNewAction.setProperty("name", _fromUtf8("fileNewAction"))
        self.fileNewAction.setObjectName(_fromUtf8("fileNewAction"))
        self.fileOpenAction = QtGui.QAction(MainWindowBA)
        self.fileOpenAction.setProperty("name", _fromUtf8("fileOpenAction"))
        self.fileOpenAction.setObjectName(_fromUtf8("fileOpenAction"))
        self.fileSaveAction = QtGui.QAction(MainWindowBA)
        self.fileSaveAction.setProperty("name", _fromUtf8("fileSaveAction"))
        self.fileSaveAction.setObjectName(_fromUtf8("fileSaveAction"))
        self.fileSaveAsAction = QtGui.QAction(MainWindowBA)
        self.fileSaveAsAction.setShortcut(_fromUtf8(""))
        self.fileSaveAsAction.setProperty("name", _fromUtf8("fileSaveAsAction"))
        self.fileSaveAsAction.setObjectName(_fromUtf8("fileSaveAsAction"))
        self.fileExitAction = QtGui.QAction(MainWindowBA)
        self.fileExitAction.setShortcut(_fromUtf8(""))
        self.fileExitAction.setProperty("name", _fromUtf8("fileExitAction"))
        self.fileExitAction.setObjectName(_fromUtf8("fileExitAction"))
        self.editUndoAction = QtGui.QAction(MainWindowBA)
        self.editUndoAction.setProperty("name", _fromUtf8("editUndoAction"))
        self.editUndoAction.setObjectName(_fromUtf8("editUndoAction"))
        self.editRedoAction = QtGui.QAction(MainWindowBA)
        self.editRedoAction.setProperty("name", _fromUtf8("editRedoAction"))
        self.editRedoAction.setObjectName(_fromUtf8("editRedoAction"))
        self.editCutAction = QtGui.QAction(MainWindowBA)
        self.editCutAction.setProperty("name", _fromUtf8("editCutAction"))
        self.editCutAction.setObjectName(_fromUtf8("editCutAction"))
        self.editCopyAction = QtGui.QAction(MainWindowBA)
        self.editCopyAction.setProperty("name", _fromUtf8("editCopyAction"))
        self.editCopyAction.setObjectName(_fromUtf8("editCopyAction"))
        self.editPasteAction = QtGui.QAction(MainWindowBA)
        self.editPasteAction.setProperty("name", _fromUtf8("editPasteAction"))
        self.editPasteAction.setObjectName(_fromUtf8("editPasteAction"))
        self.examineAction = QtGui.QAction(MainWindowBA)
        self.examineAction.setCheckable(True)
        self.examineAction.setProperty("name", _fromUtf8("examineAction"))
        self.examineAction.setObjectName(_fromUtf8("examineAction"))
        self.helpAboutAction = QtGui.QAction(MainWindowBA)
        self.helpAboutAction.setShortcut(_fromUtf8(""))
        self.helpAboutAction.setProperty("name", _fromUtf8("helpAboutAction"))
        self.helpAboutAction.setObjectName(_fromUtf8("helpAboutAction"))
        self.regexChangedAction = QtGui.QAction(MainWindowBA)
        self.regexChangedAction.setProperty("name", _fromUtf8("regexChangedAction"))
        self.regexChangedAction.setObjectName(_fromUtf8("regexChangedAction"))
        self.editPauseAction = QtGui.QAction(MainWindowBA)
        self.editPauseAction.setCheckable(True)
        self.editPauseAction.setProperty("name", _fromUtf8("editPauseAction"))
        self.editPauseAction.setObjectName(_fromUtf8("editPauseAction"))
        self.editPreferencesAction = QtGui.QAction(MainWindowBA)
        self.editPreferencesAction.setProperty("name", _fromUtf8("editPreferencesAction"))
        self.editPreferencesAction.setObjectName(_fromUtf8("editPreferencesAction"))
        self.helpHelpAction = QtGui.QAction(MainWindowBA)
        self.helpHelpAction.setProperty("name", _fromUtf8("helpHelpAction"))
        self.helpHelpAction.setObjectName(_fromUtf8("helpHelpAction"))
        self.helpPythonHelpAction = QtGui.QAction(MainWindowBA)
        self.helpPythonHelpAction.setProperty("name", _fromUtf8("helpPythonHelpAction"))
        self.helpPythonHelpAction.setObjectName(_fromUtf8("helpPythonHelpAction"))
        self.helpRegexReferenceAction = QtGui.QAction(MainWindowBA)
        self.helpRegexReferenceAction.setProperty("name", _fromUtf8("helpRegexReferenceAction"))
        self.helpRegexReferenceAction.setObjectName(_fromUtf8("helpRegexReferenceAction"))
        self.helpVisitWebsiteAction = QtGui.QAction(MainWindowBA)
        self.helpVisitWebsiteAction.setProperty("name", _fromUtf8("helpVisitWebsiteAction"))
        self.helpVisitWebsiteAction.setObjectName(_fromUtf8("helpVisitWebsiteAction"))
        self.helpCheckForUpdateAction = QtGui.QAction(MainWindowBA)
        self.helpCheckForUpdateAction.setProperty("name", _fromUtf8("helpCheckForUpdateAction"))
        self.helpCheckForUpdateAction.setObjectName(_fromUtf8("helpCheckForUpdateAction"))
        self.helpReportBugAction = QtGui.QAction(MainWindowBA)
        self.helpReportBugAction.setProperty("name", _fromUtf8("helpReportBugAction"))
        self.helpReportBugAction.setObjectName(_fromUtf8("helpReportBugAction"))
        self.fileImportFileAction = QtGui.QAction(MainWindowBA)
        self.fileImportFileAction.setProperty("name", _fromUtf8("fileImportFileAction"))
        self.fileImportFileAction.setObjectName(_fromUtf8("fileImportFileAction"))
        self.fileImportURLAction = QtGui.QAction(MainWindowBA)
        self.fileImportURLAction.setProperty("name", _fromUtf8("fileImportURLAction"))
        self.fileImportURLAction.setObjectName(_fromUtf8("fileImportURLAction"))
        self.helpRegexLibAction = QtGui.QAction(MainWindowBA)
        self.helpRegexLibAction.setProperty("name", _fromUtf8("helpRegexLibAction"))
        self.helpRegexLibAction.setObjectName(_fromUtf8("helpRegexLibAction"))
        self.fileRevertAction = QtGui.QAction(MainWindowBA)
        self.fileRevertAction.setProperty("name", _fromUtf8("FileRevertAction"))
        self.fileRevertAction.setObjectName(_fromUtf8("fileRevertAction"))
        self.toolBar.addAction(self.fileOpenAction)
        self.toolBar.addAction(self.fileSaveAction)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.editCutAction)
        self.toolBar.addAction(self.editCopyAction)
        self.toolBar.addAction(self.editPasteAction)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.editPauseAction)
        self.toolBar.addAction(self.examineAction)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.helpRegexReferenceAction)
        self.toolBar.addAction(self.helpRegexLibAction)
        self.fileMenu.addAction(self.fileNewAction)
        self.fileMenu.addAction(self.fileOpenAction)
        self.fileMenu.addAction(self.fileSaveAction)
        self.fileMenu.addAction(self.fileSaveAsAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.fileRevertAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.fileImportFileAction)
        self.fileMenu.addAction(self.fileImportURLAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.fileExitAction)
        self.fileMenu.addSeparator()
        self.editMenu.addAction(self.editUndoAction)
        self.editMenu.addAction(self.editRedoAction)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.editCutAction)
        self.editMenu.addAction(self.editCopyAction)
        self.editMenu.addAction(self.editPasteAction)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.examineAction)
        self.editMenu.addAction(self.editPauseAction)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.editPreferencesAction)
        self.helpMenu.addSeparator()
        self.helpMenu.addAction(self.helpHelpAction)
        self.helpMenu.addAction(self.helpPythonHelpAction)
        self.helpMenu.addSeparator()
        self.helpMenu.addAction(self.helpRegexReferenceAction)
        self.helpMenu.addAction(self.helpRegexLibAction)
        self.helpMenu.addSeparator()
        self.helpMenu.addAction(self.helpVisitWebsiteAction)
        self.helpMenu.addSeparator()
        self.helpMenu.addAction(self.helpAboutAction)
        self.menubar.addAction(self.fileMenu.menuAction())
        self.menubar.addAction(self.editMenu.menuAction())
        self.menubar.addAction(self.helpMenu.menuAction())

        self.retranslateUi(MainWindowBA)
        self.resultTabWidget.setCurrentIndex(0)
        self.tabWidget3.setCurrentIndex(0)
        QtCore.QObject.connect(self.dotallCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), MainWindowBA.checkboxSlot)
        QtCore.QObject.connect(self.editCopyAction, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindowBA.editCopy)
        QtCore.QObject.connect(self.editCutAction, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindowBA.editCut)
        QtCore.QObject.connect(self.editPasteAction, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindowBA.editPaste)
        QtCore.QObject.connect(self.editRedoAction, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindowBA.editRedo)
        QtCore.QObject.connect(self.editUndoAction, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindowBA.editUndo)
        QtCore.QObject.connect(self.examineAction, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindowBA.examine)
        QtCore.QObject.connect(self.fileExitAction, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindowBA.close)
        QtCore.QObject.connect(self.fileNewAction, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindowBA.fileNew)
        QtCore.QObject.connect(self.fileOpenAction, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindowBA.fileOpen)
        QtCore.QObject.connect(self.fileSaveAction, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindowBA.fileSave)
        QtCore.QObject.connect(self.fileSaveAsAction, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindowBA.fileSaveAs)
        QtCore.QObject.connect(self.helpAboutAction, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindowBA.helpAbout)
        QtCore.QObject.connect(self.helpHelpAction, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindowBA.helpHelp)
        QtCore.QObject.connect(self.ignorecaseCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), MainWindowBA.checkboxSlot)
        QtCore.QObject.connect(self.localeCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), MainWindowBA.checkboxSlot)
        QtCore.QObject.connect(self.matchNumberSpinBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindowBA.matchNumSlot)
        QtCore.QObject.connect(self.multilineCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), MainWindowBA.checkboxSlot)
        QtCore.QObject.connect(self.regexMultiLineEdit, QtCore.SIGNAL(_fromUtf8("textChanged()")), MainWindowBA.regexChangedSlot)
        QtCore.QObject.connect(self.stringMultiLineEdit, QtCore.SIGNAL(_fromUtf8("textChanged()")), MainWindowBA.stringChangedSlot)
        QtCore.QObject.connect(self.unicodeCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), MainWindowBA.checkboxSlot)
        QtCore.QObject.connect(self.verboseCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), MainWindowBA.checkboxSlot)
        QtCore.QObject.connect(self.editPauseAction, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), MainWindowBA.pause)
        QtCore.QObject.connect(self.editPreferencesAction, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindowBA.editPreferences)
        QtCore.QObject.connect(self.helpPythonHelpAction, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindowBA.helpPythonRegex)
        QtCore.QObject.connect(self.helpRegexReferenceAction, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindowBA.referenceGuide)
        QtCore.QObject.connect(self.helpVisitWebsiteAction, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindowBA.helpVisitKangWebsite)
        QtCore.QObject.connect(self.replaceTextEdit, QtCore.SIGNAL(_fromUtf8("textChanged()")), MainWindowBA.replaceChangedSlot)
        QtCore.QObject.connect(self.replaceNumberSpinBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindowBA.replaceNumSlot)
        QtCore.QObject.connect(self.fileImportFileAction, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindowBA.importFile)
        QtCore.QObject.connect(self.fileImportURLAction, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindowBA.importURL)
        QtCore.QObject.connect(self.helpRegexLibAction, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindowBA.helpRegexLib)
        QtCore.QObject.connect(self.regexMultiLineEdit, QtCore.SIGNAL(_fromUtf8("textChanged()")), MainWindowBA.edited)
        QtCore.QObject.connect(self.stringMultiLineEdit, QtCore.SIGNAL(_fromUtf8("textChanged()")), MainWindowBA.edited)
        QtCore.QObject.connect(self.ignorecaseCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), MainWindowBA.edited)
        QtCore.QObject.connect(self.replaceTextEdit, QtCore.SIGNAL(_fromUtf8("textChanged()")), MainWindowBA.edited)
        QtCore.QObject.connect(self.multilineCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), MainWindowBA.edited)
        QtCore.QObject.connect(self.dotallCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), MainWindowBA.edited)
        QtCore.QObject.connect(self.verboseCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), MainWindowBA.edited)
        QtCore.QObject.connect(self.localeCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), MainWindowBA.edited)
        QtCore.QObject.connect(self.unicodeCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), MainWindowBA.edited)
        QtCore.QObject.connect(self.fileRevertAction, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindowBA.fileRevert)
        QtCore.QMetaObject.connectSlotsByName(MainWindowBA)
        MainWindowBA.setTabOrder(self.regexMultiLineEdit, self.stringMultiLineEdit)
        MainWindowBA.setTabOrder(self.stringMultiLineEdit, self.resultTabWidget)
        MainWindowBA.setTabOrder(self.resultTabWidget, self.ignorecaseCheckBox)
        MainWindowBA.setTabOrder(self.ignorecaseCheckBox, self.multilineCheckBox)
        MainWindowBA.setTabOrder(self.multilineCheckBox, self.dotallCheckBox)
        MainWindowBA.setTabOrder(self.dotallCheckBox, self.verboseCheckBox)
        MainWindowBA.setTabOrder(self.verboseCheckBox, self.localeCheckBox)
        MainWindowBA.setTabOrder(self.localeCheckBox, self.unicodeCheckBox)
        MainWindowBA.setTabOrder(self.unicodeCheckBox, self.matchNumberSpinBox)
        MainWindowBA.setTabOrder(self.matchNumberSpinBox, self.matchTextBrowser)
        MainWindowBA.setTabOrder(self.matchTextBrowser, self.codeTextBrowser)

    def retranslateUi(self, MainWindowBA):
        MainWindowBA.setWindowTitle(_translate("MainWindowBA", "Kang - The Python Regular Expression Editor", None))
        MainWindowBA.setWindowIconText(_translate("MainWindowBA", "Kang", None))
        self.groupBox2.setTitle(_translate("MainWindowBA", "Flags", None))
        self.ignorecaseCheckBox.setToolTip(_translate("MainWindowBA", "Perform case-insensitive matching; expressions like [A-Z] will match\n"
"lowercase letters, too. This is not affected by the current locale.", None))
        self.ignorecaseCheckBox.setText(_translate("MainWindowBA", "Ignore Case", None))
        self.multilineCheckBox.setToolTip(_translate("MainWindowBA", "When specified, the pattern character \"^\" matches at the beginning of the \n"
"string and at the beginning of each line (immediately following each newline); \n"
"and the pattern character \"$\" matches at the end of the string and at the end \n"
"of each line (immediately preceding each newline). By default, \"^\" matches \n"
"only at the beginning of the string, and \"$\" only at the end of the string and \n"
"immediately before the newline (if any) at the end of the string.", None))
        self.multilineCheckBox.setText(_translate("MainWindowBA", "Multi Line", None))
        self.dotallCheckBox.setToolTip(_translate("MainWindowBA", "Make the \".\" special character match any character at all, including a \n"
"newline; without this flag, \".\" will match anything except a newline.", None))
        self.dotallCheckBox.setText(_translate("MainWindowBA", "Dot All", None))
        self.verboseCheckBox.setToolTip(_translate("MainWindowBA", "This flag allows you to write regular expressions that look nicer. Whitespace \n"
"within the pattern is ignored, except when in a character class or preceded by \n"
"an unescaped backslash, and, when a line contains a \"#\" neither in a character\n"
"class or preceded by an unescaped backslash, all characters from the leftmost \n"
"such \"#\" through the end of the line are ignored.", None))
        self.verboseCheckBox.setText(_translate("MainWindowBA", "Verbose", None))
        self.localeCheckBox.setToolTip(_translate("MainWindowBA", "Make \\w, \\W, \\b, and \\B dependent on the current locale.", None))
        self.localeCheckBox.setText(_translate("MainWindowBA", "Locale", None))
        self.unicodeCheckBox.setToolTip(_translate("MainWindowBA", "\"Make \\w, \\W, \\b, and \\B dependent on the Unicode character properties \n"
"database. New in Python version 2.0.", None))
        self.unicodeCheckBox.setText(_translate("MainWindowBA", "Unicode", None))
        self.groupBox1.setTitle(_translate("MainWindowBA", "Regular Expression Pattern", None))
        item = self.groupTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindowBA", "Group Name", None))
        item = self.groupTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindowBA", "Match", None))
        self.resultTabWidget.setTabText(self.resultTabWidget.indexOf(self.tab), _translate("MainWindowBA", "Group", None))
        self.resultTabWidget.setTabText(self.resultTabWidget.indexOf(self.tab1), _translate("MainWindowBA", "Match", None))
        self.resultTabWidget.setTabText(self.resultTabWidget.indexOf(self.TabPage), _translate("MainWindowBA", "Match All", None))
        self.resultTabWidget.setTabText(self.resultTabWidget.indexOf(self.TabPage1), _translate("MainWindowBA", "Replace", None))
        self.resultTabWidget.setTabText(self.resultTabWidget.indexOf(self.TabPage2), _translate("MainWindowBA", "Sample Code", None))
        self.tabWidget3.setTabText(self.tabWidget3.indexOf(self.tab2), _translate("MainWindowBA", "Search String", None))
        self.tabWidget3.setTabText(self.tabWidget3.indexOf(self.tab3), _translate("MainWindowBA", "Replace String", None))
        self.textLabel1.setText(_translate("MainWindowBA", "Match Number", None))
        self.replaceLabel.setText(_translate("MainWindowBA", "Replace Number", None))
        self.toolBar.setProperty("label", _translate("MainWindowBA", "Tools", None))
        self.fileMenu.setTitle(_translate("MainWindowBA", "&File", None))
        self.editMenu.setTitle(_translate("MainWindowBA", "&Edit", None))
        self.helpMenu.setTitle(_translate("MainWindowBA", "&Help", None))
        self.fileNewAction.setText(_translate("MainWindowBA", "&New", None))
        self.fileNewAction.setIconText(_translate("MainWindowBA", "New", None))
        self.fileNewAction.setShortcut(_translate("MainWindowBA", "Ctrl+N", None))
        self.fileOpenAction.setText(_translate("MainWindowBA", "&Open...", None))
        self.fileOpenAction.setIconText(_translate("MainWindowBA", "Open", None))
        self.fileOpenAction.setShortcut(_translate("MainWindowBA", "Ctrl+O", None))
        self.fileSaveAction.setText(_translate("MainWindowBA", "&Save", None))
        self.fileSaveAction.setIconText(_translate("MainWindowBA", "Save", None))
        self.fileSaveAction.setShortcut(_translate("MainWindowBA", "Ctrl+S", None))
        self.fileSaveAsAction.setText(_translate("MainWindowBA", "Save &As...", None))
        self.fileSaveAsAction.setIconText(_translate("MainWindowBA", "Save As", None))
        self.fileExitAction.setText(_translate("MainWindowBA", "E&xit", None))
        self.fileExitAction.setIconText(_translate("MainWindowBA", "Exit", None))
        self.editUndoAction.setText(_translate("MainWindowBA", "&Undo", None))
        self.editUndoAction.setIconText(_translate("MainWindowBA", "Undo", None))
        self.editUndoAction.setShortcut(_translate("MainWindowBA", "Ctrl+Z", None))
        self.editRedoAction.setText(_translate("MainWindowBA", "&Redo", None))
        self.editRedoAction.setIconText(_translate("MainWindowBA", "Redo", None))
        self.editRedoAction.setShortcut(_translate("MainWindowBA", "Ctrl+Y", None))
        self.editCutAction.setText(_translate("MainWindowBA", "&Cut", None))
        self.editCutAction.setIconText(_translate("MainWindowBA", "Cut", None))
        self.editCutAction.setShortcut(_translate("MainWindowBA", "Ctrl+X", None))
        self.editCopyAction.setText(_translate("MainWindowBA", "C&opy", None))
        self.editCopyAction.setIconText(_translate("MainWindowBA", "Copy", None))
        self.editCopyAction.setShortcut(_translate("MainWindowBA", "Ctrl+C", None))
        self.editPasteAction.setText(_translate("MainWindowBA", "&Paste", None))
        self.editPasteAction.setIconText(_translate("MainWindowBA", "Paste", None))
        self.editPasteAction.setShortcut(_translate("MainWindowBA", "Ctrl+V", None))
        self.examineAction.setText(_translate("MainWindowBA", "E&xamine Regex", None))
        self.examineAction.setIconText(_translate("MainWindowBA", "Examine Regex for Match", None))
        self.examineAction.setShortcut(_translate("MainWindowBA", "Ctrl+X", None))
        self.helpAboutAction.setText(_translate("MainWindowBA", "&About", None))
        self.helpAboutAction.setIconText(_translate("MainWindowBA", "About", None))
        self.regexChangedAction.setText(_translate("MainWindowBA", "Action", None))
        self.regexChangedAction.setIconText(_translate("MainWindowBA", "Action", None))
        self.editPauseAction.setText(_translate("MainWindowBA", "Pause Processing", None))
        self.editPauseAction.setIconText(_translate("MainWindowBA", "Pause Processing", None))
        self.editPauseAction.setShortcut(_translate("MainWindowBA", "Ctrl+P", None))
        self.editPreferencesAction.setText(_translate("MainWindowBA", "Preferences", None))
        self.editPreferencesAction.setIconText(_translate("MainWindowBA", "Preferences", None))
        self.helpHelpAction.setText(_translate("MainWindowBA", "Help", None))
        self.helpHelpAction.setIconText(_translate("MainWindowBA", "Help", None))
        self.helpHelpAction.setShortcut(_translate("MainWindowBA", "Ctrl+/", None))
        self.helpPythonHelpAction.setText(_translate("MainWindowBA", "&Python Regex Help", None))
        self.helpPythonHelpAction.setIconText(_translate("MainWindowBA", "Python Regex Help", None))
        self.helpRegexReferenceAction.setText(_translate("MainWindowBA", "&Regex Reference Guide", None))
        self.helpRegexReferenceAction.setIconText(_translate("MainWindowBA", "Regex Reference Guide", None))
        self.helpRegexReferenceAction.setShortcut(_translate("MainWindowBA", "Ctrl+R", None))
        self.helpVisitWebsiteAction.setText(_translate("MainWindowBA", "&Visit Kang Website", None))
        self.helpVisitWebsiteAction.setIconText(_translate("MainWindowBA", "&Visit Kang Website", None))
        self.helpCheckForUpdateAction.setText(_translate("MainWindowBA", "&Check for Kang Update", None))
        self.helpCheckForUpdateAction.setIconText(_translate("MainWindowBA", "Check for Kang Update", None))
        self.helpReportBugAction.setText(_translate("MainWindowBA", "Report a &Bug", None))
        self.helpReportBugAction.setIconText(_translate("MainWindowBA", "Report a Bug", None))
        self.fileImportFileAction.setText(_translate("MainWindowBA", "Import &File", None))
        self.fileImportFileAction.setIconText(_translate("MainWindowBA", "Import File", None))
        self.fileImportURLAction.setText(_translate("MainWindowBA", "Import &URL", None))
        self.fileImportURLAction.setIconText(_translate("MainWindowBA", "Import URL", None))
        self.helpRegexLibAction.setText(_translate("MainWindowBA", "Regex &Library", None))
        self.helpRegexLibAction.setIconText(_translate("MainWindowBA", "Regex Library", None))
        self.helpRegexLibAction.setToolTip(_translate("MainWindowBA", "Open the Regex Library", None))
        self.helpRegexLibAction.setShortcut(_translate("MainWindowBA", "Ctrl+L", None))
        self.fileRevertAction.setText(_translate("MainWindowBA", "&Revert Kang File", None))
        self.fileRevertAction.setIconText(_translate("MainWindowBA", "Revert Kang File", None))


class MainWindowBA(QtGui.QMainWindow, Ui_MainWindowBA):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)

        self.setupUi(self)

