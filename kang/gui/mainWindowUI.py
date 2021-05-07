from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from kang.images import getIcon
from kang.modules.regexprocessor import RegexProcessor


class MainWindowUI(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle("Kang")
        self.setWindowIcon(getIcon('kang-icon'))

        self.resize(497, 718)

        self._regexProcessor = RegexProcessor()

        self._createActions()
        self._setupMenuBar()
        self._setupToolBar()
        self.statusBar()
        self._setupCentralWidget()

        self._regexProcessor.statusChanged.connect(self._regexStatusChanged)

    def _createActions(self):

        self.fileOpenAction = QAction(getIcon('document-open'), "Open", self)
        self.fileOpenAction.setShortcut("Ctrl+O")
        self.fileOpenAction.triggered.connect(self.fileOpen)

        self.fileSaveAction = QAction(getIcon('document-save'), "Save", self)
        self.fileSaveAction.setShortcut("Ctrl+S")
        self.fileSaveAction.triggered.connect(self.fileSave)

        self._exitAction = QAction("Exit", self)
        self._exitAction.triggered.connect(self.fileExit)

    def _setupMenuBar(self):
        menubar = self.menuBar()

        fileMenu = menubar.addMenu("&File")
        editMenu = menubar.addMenu("&Edit")
        helpMenu = menubar.addMenu("&Help")

        fileMenu.addAction(self.fileOpenAction)
        fileMenu.addAction(self.fileSaveAction)
        fileMenu.addAction(self._exitAction)

    def _setupToolBar(self):
        toolBar = QToolBar(self)
        self.addToolBar(Qt.TopToolBarArea, toolBar)

        toolBar.addAction(self.fileOpenAction)

    def _setupCentralWidget(self):
        self.widget = QWidget(self)

        gridLayout = QGridLayout(self.widget)
        gridLayout.setSpacing(6)
        gridLayout.setContentsMargins(11, 11, 11, 11)

        tabWidget = QTabWidget(self.widget)
        self.stringMultiLineEdit = QTextEdit()
        tabWidget.addTab(self.stringMultiLineEdit, "Match String")
        gridLayout.addWidget(tabWidget, 0, 0, 1, 1)
        self.stringMultiLineEdit.textChanged.connect(lambda: self._regexProcessor.setMatchString(self.stringMultiLineEdit.toPlainText()))

        groupBox = QWidget(self)
        hboxLayout = QHBoxLayout(groupBox)
        hboxLayout.setSpacing(6)
        checkBox = QCheckBox("Ignore Case")
        hboxLayout.addWidget(checkBox)
        checkBox = QCheckBox("Multi Line")
        hboxLayout.addWidget(checkBox)
        checkBox = QCheckBox("Dot All")
        hboxLayout.addWidget(checkBox)
        checkBox = QCheckBox("Verbose")
        hboxLayout.addWidget(checkBox)
        checkBox = QCheckBox("Locale")
        hboxLayout.addWidget(checkBox)
        checkBox = QCheckBox("Unicode")
        hboxLayout.addWidget(checkBox)
        gridLayout.addWidget(groupBox, 1, 0, 1, 1)

        tabWidget = QTabWidget(self.widget)
        textEdit = QTextEdit()
        tabWidget.addTab(textEdit, "Regular Expression")
        textEdit = QTextEdit()
        tabWidget.addTab(textEdit, "Replace String")
        gridLayout.addWidget(tabWidget, 2, 0, 1, 1)

        groupBox = QWidget(self)
        hboxLayout = QHBoxLayout(groupBox)
        hboxLayout.setSpacing(6)

        textLabel1 = QLabel("Match Number", groupBox)
        hboxLayout.addWidget(textLabel1)
        self.matchNumberSpinBox = QSpinBox(groupBox)
        self.matchNumberSpinBox.setMinimum(1)
        self.matchNumberSpinBox.setMaximum(9999)
        hboxLayout.addWidget(self.matchNumberSpinBox)

        self.replaceLabel = QLabel("Replace Number", groupBox)
        hboxLayout.addWidget(self.replaceLabel)
        self.replaceNumberSpinBox = QSpinBox(groupBox)
        self.replaceNumberSpinBox.setMinimum(1)
        self.replaceNumberSpinBox.setMaximum(9999)
        hboxLayout.addWidget(self.replaceNumberSpinBox)

        gridLayout.addWidget(groupBox, 3, 0, Qt.AlignLeft)

        tabWidget = QTabWidget(self.widget)

        self.matchAllTextBrowser = QTextEdit()
        tabWidget.addTab(self.matchAllTextBrowser, "Match All")

        self.matchTextBrowser = QTextEdit()
        tabWidget.addTab(self.matchTextBrowser, "Match")

        tab = QWidget()
        self.groupTable = QTableWidget(tab)
        self.groupTable.setColumnCount(2)
        tabWidget.addTab(tab, "Group")

        self.replaceTextBrowser = QTextEdit()
        tabWidget.addTab(self.replaceTextBrowser, "Replace")

        self.codeTextBrowser = QTextEdit()
        tabWidget.addTab(self.codeTextBrowser, "Sample Code")

        gridLayout.addWidget(tabWidget, 4, 0, 1, 1)

        self.setCentralWidget(self.widget)
