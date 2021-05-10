from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMainWindow, QAction, QToolBar, QWidget, \
    QGridLayout, QTabWidget, QTextEdit, QHBoxLayout, QCheckBox, QLabel, QSpinBox, \
    QTableWidget

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

        # File Actions

        self.fileNewAction = QAction(getIcon('document-new'), "&New", self)
        self.fileNewAction.setShortcut("Ctrl+N")
        self.fileNewAction.triggered.connect(self.fileNew)

        self.fileOpenAction = QAction(getIcon('document-open'), "&Open", self)
        self.fileOpenAction.setShortcut("Ctrl+O")
        self.fileOpenAction.triggered.connect(self.fileOpen)

        self.fileSaveAction = QAction(getIcon('document-save'), "&Save", self)
        self.fileSaveAction.setShortcut("Ctrl+S")
        self.fileSaveAction.triggered.connect(self.fileSave)

        self.fileSaveAsAction = QAction("Save &As", self)
        self.fileSaveAsAction.triggered.connect(self.fileSaveAs)

        self.fileRevertFileAction = QAction("&Revert Kang File", self)
        self.fileRevertFileAction.triggered.connect(self.fileRevert)

        self.fileImportFileAction = QAction("Import &File", self)
        self.fileImportFileAction.triggered.connect(self.importFile)

        self.fileImportURLAction = QAction("Import &URL", self)
        self.fileImportURLAction.triggered.connect(self.importURL)

        self._exitAction = QAction("E&xit", self)
        self._exitAction.triggered.connect(self.fileExit)

        # Edit Actions

        self.editUndoAction = QAction("&Undo", self)
        self.editUndoAction.setShortcut("Ctrl+Z")
        self.editUndoAction.triggered.connect(self.editUndo)

        self.editRedoAction = QAction("&Redo", self)
        self.editRedoAction.setShortcut("Ctrl+Y")
        self.editRedoAction.triggered.connect(self.editRedo)

        self.editCutAction = QAction(getIcon('edit-cut'), "&Cut", self)
        self.editCutAction.setShortcut("Ctrl+X")
        self.editCutAction.triggered.connect(self.editCut)

        self.editCopyAction = QAction(getIcon('edit-copy'), "&Copy", self)
        self.editCopyAction.setShortcut("Ctrl+C")
        self.editCopyAction.triggered.connect(self.editCopy)

        self.editPasteAction = QAction(getIcon('edit-paste'), "&Paste", self)
        self.editPasteAction.setShortcut("Ctrl+V")
        self.editPasteAction.triggered.connect(self.editPaste)

        self.editPauseAction = QAction(getIcon('media-playback-pause'), "&Pause", self)
        self.editPauseAction.setShortcut("Ctrl+P")
        self.editPauseAction.triggered.connect(self.pause)

        self.editExamineAction = QAction(getIcon('edit-find'), "&Examine Regex", self)
        self.editExamineAction.setShortcut("Ctrl+E")
        self.editExamineAction.triggered.connect(self.examine)

        self.editPreferencesAction = QAction(getIcon('edit-preferences'), "Preferences", self)
        self.editPreferencesAction.setShortcut("Ctrl+P")
        self.editPreferencesAction.triggered.connect(self.editPreferences)

        # Help Actions

        self.helpHelpAction = QAction("&Help", self)
        self.helpHelpAction.setShortcut("F1")
        self.helpHelpAction.triggered.connect(self.helpHelp)

        self.helpRegexHelpAction = QAction("&Python Regex Help", self)
        self.helpRegexHelpAction.triggered.connect(self.helpPythonRegex)

        self.helpRegexReferenceGuideAction = QAction(getIcon('book'), "&Regex Reference Guide", self)
        self.helpRegexReferenceGuideAction.setShortcut("Ctrl+R")
        self.helpRegexReferenceGuideAction.triggered.connect(self.referenceGuide)

        self.helpRegexLibraryAction = QAction(getIcon('library'), "Regex &Library", self)
        self.helpRegexReferenceGuideAction.setShortcut("Ctrl+L")
        self.helpRegexLibraryAction.triggered.connect(self.helpRegexLib)

        self.helpVisitKangWebsiteAction = QAction("&Visit Kang Website", self)
        self.helpVisitKangWebsiteAction.triggered.connect(self.helpVisitKangWebsite)

        self.helpAboutAction = QAction("&About", self)
        self.helpAboutAction.triggered.connect(self.helpAbout)

    def _setupMenuBar(self):
        menubar = self.menuBar()

        fileMenu = menubar.addMenu("&File")
        editMenu = menubar.addMenu("&Edit")
        helpMenu = menubar.addMenu("&Help")

        fileMenu.addAction(self.fileNewAction)
        fileMenu.addAction(self.fileOpenAction)
        fileMenu.addAction(self.fileSaveAction)
        fileMenu.addAction(self.fileSaveAsAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.fileRevertFileAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.fileImportFileAction)
        fileMenu.addAction(self.fileImportURLAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self._exitAction)

        editMenu.addAction(self.editUndoAction)
        editMenu.addAction(self.editRedoAction)
        editMenu.addSeparator()
        editMenu.addAction(self.editCutAction)
        editMenu.addAction(self.editCopyAction)
        editMenu.addAction(self.editPasteAction)
        editMenu.addSeparator()
        editMenu.addAction(self.editPauseAction)
        editMenu.addAction(self.editExamineAction)
        editMenu.addSeparator()
        editMenu.addAction(self.editPreferencesAction)

        helpMenu.addAction(self.helpHelpAction)
        helpMenu.addAction(self.helpRegexHelpAction)
        helpMenu.addSeparator()
        helpMenu.addAction(self.helpRegexReferenceGuideAction)
        helpMenu.addAction(self.helpRegexLibraryAction)
        helpMenu.addSeparator()
        helpMenu.addAction(self.helpVisitKangWebsiteAction)
        helpMenu.addSeparator()
        helpMenu.addAction(self.helpAboutAction)

    def _setupToolBar(self):
        toolBar = QToolBar(self)
        self.addToolBar(Qt.TopToolBarArea, toolBar)

        toolBar.addAction(self.fileOpenAction)
        toolBar.addAction(self.fileSaveAction)
        toolBar.addSeparator()
        toolBar.addAction(self.editCutAction)
        toolBar.addAction(self.editCopyAction)
        toolBar.addAction(self.editPasteAction)
        toolBar.addSeparator()
        toolBar.addAction(self.editPauseAction)
        toolBar.addAction(self.editExamineAction)
        toolBar.addSeparator()
        toolBar.addAction(self.helpRegexReferenceGuideAction)
        toolBar.addAction(self.helpRegexLibraryAction)

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
