from PySide2.QtCore import Qt
from PySide2.QtGui import QPalette
from PySide2.QtWidgets import \
    QMainWindow, QAction, QToolBar, QWidget, QLabel, \
    QGridLayout, QTabWidget, QTextEdit, QHBoxLayout, QCheckBox, QSpinBox, \
    QTreeWidget, QStyledItemDelegate, QAbstractItemView

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
        self._setupStatusBar()
        self._setupCentralWidget()

        self._regexProcessor.statusChanged.connect(self._regexprocessorStatusChanged)

        palette = self.stringMultiLineEdit.palette()

        self.normalTextColor = palette.color(QPalette.ColorGroup.Active, QPalette.ColorRole.Text)
        self.normalForegroundColor = palette.color(QPalette.ColorGroup.Active, QPalette.ColorRole.Base)
        self.disabledTextColor = palette.color(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text)
        self.highlightTextColor = palette.color(QPalette.ColorGroup.Active, QPalette.ColorRole.HighlightedText)
        self.highlightForegroundColor = palette.color(QPalette.ColorGroup.Active, QPalette.ColorRole.Highlight)

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

        self.fileSaveAsAction = QAction(getIcon('document-save-as'), "Save &As", self)
        self.fileSaveAsAction.triggered.connect(self.fileSaveAs)

        self.fileRevertAction = QAction(getIcon('document-revert'), "&Revert", self)
        self.fileRevertAction.triggered.connect(self.fileRevert)

        self.fileImportFileAction = QAction("Import &File", self)
        self.fileImportFileAction.triggered.connect(self.importFile)

        self.fileImportURLAction = QAction("Import &URL", self)
        self.fileImportURLAction.triggered.connect(self._importURL)

        self._exitAction = QAction("E&xit", self)
        self._exitAction.triggered.connect(self.fileExit)

        # Edit Actions

        self.editUndoAction = QAction(getIcon('edit-undo'), "&Undo", self)
        self.editUndoAction.setShortcut("Ctrl+Z")
        self.editUndoAction.triggered.connect(self.editUndo)

        self.editRedoAction = QAction(getIcon('edit-redo'), "&Redo", self)
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

        self.editPauseAction = QAction(getIcon('media-playback-pause'), "&Pause", self, checkable=True)
        self.editPauseAction.setShortcut("Ctrl+P")
        self.editPauseAction.triggered.connect(self.pause)

        self.editExamineAction = QAction(getIcon('edit-find'), "&Examine Regex", self, checkable=True)
        self.editExamineAction.setShortcut("Ctrl+E")
        self.editExamineAction.triggered.connect(self.examine)

        self.editPreferencesAction = QAction("Preferences", self)
        self.editPreferencesAction.setShortcut("Ctrl+P")
        self.editPreferencesAction.triggered.connect(self.editPreferences)

        # Help Actions

        self.helpRegexHelpAction = QAction(getIcon('help'), "&Python Regex Help", self)
        self.helpRegexHelpAction.setShortcut("F1")
        self.helpRegexHelpAction.triggered.connect(self.helpPythonRegex)

        self.helpRegexReferenceGuideAction = QAction(getIcon('book'), "&Regex Reference Guide", self)
        self.helpRegexReferenceGuideAction.setShortcut("Ctrl+R")
        self.helpRegexReferenceGuideAction.triggered.connect(self.referenceGuide)

        self.helpRegexLibraryAction = QAction(getIcon('library'), "Regex &Library", self)
        self.helpRegexLibraryAction.setShortcut("Ctrl+L")
        self.helpRegexLibraryAction.triggered.connect(self.helpRegexLib)

        self.helpAboutAction = QAction(getIcon('help-about'), "&About", self)
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
        fileMenu.addAction(self.fileRevertAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.fileImportFileAction)
        fileMenu.addAction(self.fileImportURLAction)
        fileMenu.addSeparator()
        self.placeholderAction = fileMenu.addSeparator()
        fileMenu.addAction(self._exitAction)

        self.fileMenu = fileMenu

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

        helpMenu.addAction(self.helpRegexHelpAction)
        helpMenu.addSeparator()
        helpMenu.addAction(self.helpRegexReferenceGuideAction)
        helpMenu.addAction(self.helpRegexLibraryAction)
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

    def _setupStatusBar(self):
        permanentStatusLabel = QLabel()
        self.statusBar().addWidget(permanentStatusLabel, 1)
        self.statusBar().showPermanentMessage = permanentStatusLabel.setText

    def _setupCentralWidget(self):
        self.widget = QWidget(self)

        gridLayout = QGridLayout(self.widget)
        gridLayout.setSpacing(6)
        gridLayout.setContentsMargins(11, 11, 11, 11)

        tabWidget = QTabWidget(self.widget)

        self.stringMultiLineEdit = QTextEdit()
        self.stringMultiLineEdit.textChanged.connect(lambda: self._regexProcessor.setMatchString(self.stringMultiLineEdit.toPlainText()))
        self.stringMultiLineEdit.textChanged.connect(self._setModified)
        tabWidget.addTab(self.stringMultiLineEdit, "Match String")

        gridLayout.addWidget(tabWidget, 0, 0, 1, 1)

        groupBox = QWidget(self)
        hboxLayout = QHBoxLayout(groupBox)
        hboxLayout.setSpacing(6)

        self.ignorecaseCheckBox = QCheckBox("Ignore Case")
        self.ignorecaseCheckBox.toggled.connect(self._regexProcessor.setIgnorecaseFlag)
        self.ignorecaseCheckBox.toggled.connect(self._setModified)
        hboxLayout.addWidget(self.ignorecaseCheckBox)
        self.multilineCheckBox = QCheckBox("Multi Line")
        self.multilineCheckBox.toggled.connect(self._regexProcessor.setMultilineFlag)
        self.multilineCheckBox.toggled.connect(self._setModified)
        hboxLayout.addWidget(self.multilineCheckBox)
        self.dotallCheckBox = QCheckBox("Dot All")
        self.dotallCheckBox.toggled.connect(self._regexProcessor.setDotallFlag)
        self.dotallCheckBox.toggled.connect(self._setModified)
        hboxLayout.addWidget(self.dotallCheckBox)
        self.verboseCheckBox = QCheckBox("Verbose")
        self.verboseCheckBox.toggled.connect(self._regexProcessor.setVerboseFlag)
        self.verboseCheckBox.toggled.connect(self._setModified)
        hboxLayout.addWidget(self.verboseCheckBox)
        self.asciiCheckBox = QCheckBox("Ascii")
        self.asciiCheckBox.toggled.connect(self._regexProcessor.setAsciiFlag)
        self.asciiCheckBox.toggled.connect(self._setModified)
        hboxLayout.addWidget(self.asciiCheckBox)

        gridLayout.addWidget(groupBox, 1, 0, 1, 1)

        tabWidget = QTabWidget(self.widget)

        self.regexMultiLineEdit = QTextEdit()
        self.regexMultiLineEdit.textChanged.connect(lambda: self._regexProcessor.setRegexString(self.regexMultiLineEdit.toPlainText()))
        self.regexMultiLineEdit.textChanged.connect(self._setModified)
        tabWidget.addTab(self.regexMultiLineEdit, "Regular Expression")

        self.replaceTextEdit = QTextEdit()
        self.replaceTextEdit.textChanged.connect(lambda: self._regexProcessor.setReplaceString(self.replaceTextEdit.toPlainText()))
        self.replaceTextEdit.textChanged.connect(self._setModified)
        tabWidget.addTab(self.replaceTextEdit, "Replace String")

        gridLayout.addWidget(tabWidget, 2, 0, 1, 1)

        groupBox = QWidget(self)
        hboxLayout = QHBoxLayout(groupBox)
        hboxLayout.setSpacing(6)

        textLabel1 = QLabel("Match Number", groupBox)
        textLabel1.setToolTip("0 stands for 'all'")
        hboxLayout.addWidget(textLabel1)
        self.matchNumberSpinBox = QSpinBox(groupBox)
        self.matchNumberSpinBox.setMinimum(0)
        self.matchNumberSpinBox.setMaximum(9999)
        self.matchNumberSpinBox.setWrapping(True)
        self.matchNumberSpinBox.valueChanged.connect(self._matchNumberChanged)
        hboxLayout.addWidget(self.matchNumberSpinBox)

        self.replaceLabel = QLabel("Replace Number", groupBox)
        self.replaceLabel.setToolTip("0 stands for 'all'")
        hboxLayout.addWidget(self.replaceLabel)
        self.replaceNumberSpinBox = QSpinBox(groupBox)
        self.replaceNumberSpinBox.setMinimum(0)
        self.replaceNumberSpinBox.setMaximum(9999)
        self.replaceNumberSpinBox.setWrapping(True)
        self.replaceNumberSpinBox.valueChanged.connect(self._replaceNumberChanged)
        hboxLayout.addWidget(self.replaceNumberSpinBox)

        gridLayout.addWidget(groupBox, 3, 0, Qt.AlignLeft)

        tabWidget = QTabWidget(self.widget)

        self.matchTextBrowser = QTextEdit()
        self.matchTextBrowser.setReadOnly(True)
        tabWidget.addTab(self.matchTextBrowser, "Match")

        tab = QWidget()
        self.groupTable = QTreeWidget(tab)
        self.groupTable.setHeaderLabels(["Match Number", "Idx", "Group Name", "Match"])
        self.groupTable.setItemsExpandable(False)
        self.groupTable.setRootIsDecorated(False)
        self.groupTable.setItemDelegate(MyQStyledItemDelegate())
        self.groupTable.setSelectionMode(QAbstractItemView.NoSelection)
        gridlayout2 = QGridLayout(tab)
        gridlayout2.addWidget(self.groupTable, 0, 0, 1, 1)
        tabWidget.addTab(tab, "Group")

        self.replaceTextBrowser = QTextEdit()
        self.replaceTextBrowser.setReadOnly(True)
        tabWidget.addTab(self.replaceTextBrowser, "Replace")

        self.codeTextBrowser = QTextEdit()
        self.codeTextBrowser.setReadOnly(True)
        tabWidget.addTab(self.codeTextBrowser, "Sample Code")

        gridLayout.addWidget(tabWidget, 4, 0, 1, 1)

        self.setCentralWidget(self.widget)


class MyQStyledItemDelegate(QStyledItemDelegate):

    def paint(self, painter, option, index):
        QStyledItemDelegate.paint(self, painter, option, index)

        if index.column() > 0:  # and  not index.model().hasChildren(index):
            painter.save()
            painter.setPen(Qt.lightGray)
            painter.drawRect(option.rect)
            painter.restore()
