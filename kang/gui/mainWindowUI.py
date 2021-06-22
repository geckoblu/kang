from PySide2.QtCore import Qt
from PySide2.QtGui import QPalette
from PySide2.QtWidgets import QMainWindow, QAction, QToolBar, QWidget, QLabel, QGridLayout, \
                              QTabWidget, QTextEdit, QHBoxLayout, QCheckBox, QSpinBox, \
                              QTreeWidget, QStyledItemDelegate, QAbstractItemView, QSplitter

from kang.gui.regexLibraryWidget import RegexLibraryWidget
from kang.gui.regexReferenceWidget import RegexReferenceWidget
from kang.images import getIcon
from kang.modules.regexprocessor import RegexProcessor

tr = lambda msg: msg


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

        mainPanel = self._createMainPanel()
        self._setupCentralWidget(mainPanel)

        self._regexProcessor.statusChanged.connect(self._regexprocessorStatusChanged)

        palette = self._stringMultiLineEdit.palette()

        self._normalTextColor = palette.color(QPalette.ColorGroup.Active, QPalette.ColorRole.Text)
        self._normalForegroundColor = palette.color(QPalette.ColorGroup.Active, QPalette.ColorRole.Base)
        self._disabledTextColor = palette.color(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text)
        self._highlightTextColor = palette.color(QPalette.ColorGroup.Active, QPalette.ColorRole.HighlightedText)
        self._highlightForegroundColor = palette.color(QPalette.ColorGroup.Active, QPalette.ColorRole.Highlight)

    def _createActions(self):

        # File Actions

        self._fileNewAction = QAction(getIcon('document-new'), "&New", self)
        self._fileNewAction.setShortcut("Ctrl+N")
        self._fileNewAction.triggered.connect(self._fileNew)

        self._fileOpenAction = QAction(getIcon('document-open'), "&Open", self)
        self._fileOpenAction.setShortcut("Ctrl+O")
        self._fileOpenAction.triggered.connect(self._fileOpen)

        self._fileSaveAction = QAction(getIcon('document-save'), "&Save", self)
        self._fileSaveAction.setShortcut("Ctrl+S")
        self._fileSaveAction.triggered.connect(self._fileSave)

        self._fileSaveAsAction = QAction(getIcon('document-save-as'), "Save &As", self)
        self._fileSaveAsAction.triggered.connect(self._fileSaveAs)

        self._fileRevertAction = QAction(getIcon('document-revert'), "&Revert", self)
        self._fileRevertAction.triggered.connect(self._fileRevert)

        self._fileImportFileAction = QAction("Import &File", self)
        self._fileImportFileAction.triggered.connect(self._importFile)

        self._fileImportURLAction = QAction("Import &URL", self)
        self._fileImportURLAction.triggered.connect(self._importURL)

        self._exitAction = QAction("E&xit", self)
        self._exitAction.triggered.connect(self._fileExit)

        # Edit Actions

        self._editUndoAction = QAction(getIcon('edit-undo'), "&Undo", self)
        self._editUndoAction.setShortcut("Ctrl+Z")
        self._editUndoAction.triggered.connect(self._editUndo)

        self._editRedoAction = QAction(getIcon('edit-redo'), "&Redo", self)
        self._editRedoAction.setShortcut("Ctrl+Y")
        self._editRedoAction.triggered.connect(self._editRedo)

        self._editCutAction = QAction(getIcon('edit-cut'), "&Cut", self)
        self._editCutAction.setShortcut("Ctrl+X")
        self._editCutAction.triggered.connect(self._editCut)

        self._editCopyAction = QAction(getIcon('edit-copy'), "&Copy", self)
        self._editCopyAction.setShortcut("Ctrl+C")
        self._editCopyAction.triggered.connect(self._editCopy)

        self._editPasteAction = QAction(getIcon('edit-paste'), "&Paste", self)
        self._editPasteAction.setShortcut("Ctrl+V")
        self._editPasteAction.triggered.connect(self._editPaste)

        self._editPauseAction = QAction(getIcon('media-playback-pause'), "&Pause", self, checkable=True)
        self._editPauseAction.setShortcut("Ctrl+P")
        self._editPauseAction.triggered.connect(self._pause)

        self._editExamineAction = QAction(getIcon('edit-find'), "&Examine Regex", self, checkable=True)
        self._editExamineAction.setShortcut("Ctrl+E")
        self._editExamineAction.triggered.connect(self._examine)

        self._editPreferencesAction = QAction("Preferences", self)
        self._editPreferencesAction.setShortcut("Ctrl+P")
        self._editPreferencesAction.triggered.connect(self._editPreferences)

        # Help Actions

        self._helpRegexHelpAction = QAction(getIcon('help'), "&Python Regex Help", self)
        self._helpRegexHelpAction.setShortcut("F1")
        self._helpRegexHelpAction.triggered.connect(self._helpPythonRegex)

        self._helpRegexReferenceGuideAction = QAction(getIcon('book'), "&Regex Reference Guide", self, checkable=True)
        self._helpRegexReferenceGuideAction.setShortcut("Ctrl+R")
        self._helpRegexReferenceGuideAction.triggered.connect(self._helpRegexReferenceGuide)

        self._helpRegexLibraryAction = QAction(getIcon('library'), "Regex &Library", self, checkable=True)
        self._helpRegexLibraryAction.setShortcut("Ctrl+L")
        self._helpRegexLibraryAction.triggered.connect(self._helpRegexLibrary)

        self._helpAboutAction = QAction(getIcon('help-about'), "&About", self)
        self._helpAboutAction.triggered.connect(self._helpAbout)

    def _setupMenuBar(self):
        menubar = self.menuBar()

        fileMenu = menubar.addMenu("&File")
        editMenu = menubar.addMenu("&Edit")
        helpMenu = menubar.addMenu("&Help")

        fileMenu.addAction(self._fileNewAction)
        fileMenu.addAction(self._fileOpenAction)
        fileMenu.addAction(self._fileSaveAction)
        fileMenu.addAction(self._fileSaveAsAction)
        fileMenu.addAction(self._fileRevertAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self._fileImportFileAction)
        fileMenu.addAction(self._fileImportURLAction)
        fileMenu.addSeparator()
        self._placeholderAction = fileMenu.addSeparator()
        fileMenu.addAction(self._exitAction)

        self._fileMenu = fileMenu

        editMenu.addAction(self._editUndoAction)
        editMenu.addAction(self._editRedoAction)
        editMenu.addSeparator()
        editMenu.addAction(self._editCutAction)
        editMenu.addAction(self._editCopyAction)
        editMenu.addAction(self._editPasteAction)
        editMenu.addSeparator()
        editMenu.addAction(self._editPauseAction)
        editMenu.addAction(self._editExamineAction)
        editMenu.addSeparator()
        editMenu.addAction(self._editPreferencesAction)

        helpMenu.addAction(self._helpRegexHelpAction)
        helpMenu.addSeparator()
        helpMenu.addAction(self._helpRegexReferenceGuideAction)
        helpMenu.addAction(self._helpRegexLibraryAction)
        helpMenu.addSeparator()
        helpMenu.addAction(self._helpAboutAction)

    def _setupToolBar(self):
        toolBar = QToolBar(self)
        self.addToolBar(Qt.TopToolBarArea, toolBar)

        toolBar.addAction(self._fileOpenAction)
        toolBar.addAction(self._fileSaveAction)
        toolBar.addSeparator()
        toolBar.addAction(self._editCutAction)
        toolBar.addAction(self._editCopyAction)
        toolBar.addAction(self._editPasteAction)
        toolBar.addSeparator()
        toolBar.addAction(self._editPauseAction)
        toolBar.addAction(self._editExamineAction)
        toolBar.addSeparator()
        toolBar.addAction(self._helpRegexReferenceGuideAction)
        toolBar.addAction(self._helpRegexLibraryAction)

    def _setupStatusBar(self):
        permanentStatusLabel = QLabel()
        self.statusBar().addWidget(permanentStatusLabel, 1)
        self.statusBar().showPermanentMessage = permanentStatusLabel.setText

    def _setupCentralWidget(self, mainPanel):
        self._regexReferencePanel = RegexReferenceWidget()
        self._regexLibraryPanel = RegexLibraryWidget()

        self._splitterTabWidget = QTabWidget()
        self._splitterTabWidget.hide()
        # self._splitterTabWidget.addTab(self._regexReferencePanel, tr("Regex Reference Guide"))
        # self._splitterTabWidget.addTab(self._regexLibraryPanel, tr("Regex Library"))

        self._splitter = QSplitter()
        self._splitter.addWidget(mainPanel)
        self._splitter.addWidget(self._splitterTabWidget)

        self.setCentralWidget(self._splitter)

    def _createMainPanel(self):
        widget = QWidget(self)

        gridLayout = QGridLayout(widget)
        gridLayout.setSpacing(6)
        gridLayout.setContentsMargins(11, 11, 11, 11)

        tabWidget = QTabWidget(widget)

        self._stringMultiLineEdit = QTextEdit()
        self._stringMultiLineEdit.textChanged.connect(
            lambda: self._regexProcessor.setMatchString(self._stringMultiLineEdit.toPlainText()))
        self._stringMultiLineEdit.textChanged.connect(self._setModified)
        tabWidget.addTab(self._stringMultiLineEdit, "Match String")

        gridLayout.addWidget(tabWidget, 0, 0, 1, 1)

        groupBox = QWidget(self)
        hboxLayout = QHBoxLayout(groupBox)
        hboxLayout.setSpacing(6)

        self._ignorecaseCheckBox = QCheckBox("Ignore Case")
        self._ignorecaseCheckBox.toggled.connect(self._regexProcessor.setIgnorecaseFlag)
        self._ignorecaseCheckBox.toggled.connect(self._setModified)
        hboxLayout.addWidget(self._ignorecaseCheckBox)
        self._multilineCheckBox = QCheckBox("Multi Line")
        self._multilineCheckBox.toggled.connect(self._regexProcessor.setMultilineFlag)
        self._multilineCheckBox.toggled.connect(self._setModified)
        hboxLayout.addWidget(self._multilineCheckBox)
        self._dotallCheckBox = QCheckBox("Dot All")
        self._dotallCheckBox.toggled.connect(self._regexProcessor.setDotallFlag)
        self._dotallCheckBox.toggled.connect(self._setModified)
        hboxLayout.addWidget(self._dotallCheckBox)
        self._verboseCheckBox = QCheckBox("Verbose")
        self._verboseCheckBox.toggled.connect(self._regexProcessor.setVerboseFlag)
        self._verboseCheckBox.toggled.connect(self._setModified)
        hboxLayout.addWidget(self._verboseCheckBox)
        self._asciiCheckBox = QCheckBox("Ascii")
        self._asciiCheckBox.toggled.connect(self._regexProcessor.setAsciiFlag)
        self._asciiCheckBox.toggled.connect(self._setModified)
        hboxLayout.addWidget(self._asciiCheckBox)

        gridLayout.addWidget(groupBox, 1, 0, 1, 1)

        tabWidget = QTabWidget(widget)

        self._regexMultiLineEdit = QTextEdit()
        self._regexMultiLineEdit.textChanged.connect(
            lambda: self._regexProcessor.setRegexString(self._regexMultiLineEdit.toPlainText()))
        self._regexMultiLineEdit.textChanged.connect(self._setModified)
        tabWidget.addTab(self._regexMultiLineEdit, "Regular Expression")

        self._replaceTextEdit = QTextEdit()
        self._replaceTextEdit.textChanged.connect(
            lambda: self._regexProcessor.setReplaceString(self._replaceTextEdit.toPlainText()))
        self._replaceTextEdit.textChanged.connect(self._setModified)
        tabWidget.addTab(self._replaceTextEdit, "Replace String")

        gridLayout.addWidget(tabWidget, 2, 0, 1, 1)

        groupBox = QWidget(self)
        hboxLayout = QHBoxLayout(groupBox)
        hboxLayout.setSpacing(6)

        textLabel1 = QLabel("Match Number", groupBox)
        textLabel1.setToolTip("0 stands for 'all'")
        hboxLayout.addWidget(textLabel1)
        self._matchNumberSpinBox = QSpinBox(groupBox)
        self._matchNumberSpinBox.setMinimum(0)
        self._matchNumberSpinBox.setMaximum(9999)
        self._matchNumberSpinBox.setWrapping(True)
        self._matchNumberSpinBox.valueChanged.connect(self._matchNumberChanged)
        hboxLayout.addWidget(self._matchNumberSpinBox)

        replaceLabel = QLabel("Replace Number", groupBox)
        replaceLabel.setToolTip("0 stands for 'all'")
        hboxLayout.addWidget(replaceLabel)
        self._replaceNumberSpinBox = QSpinBox(groupBox)
        self._replaceNumberSpinBox.setMinimum(0)
        self._replaceNumberSpinBox.setMaximum(9999)
        self._replaceNumberSpinBox.setWrapping(True)
        self._replaceNumberSpinBox.valueChanged.connect(self._replaceNumberChanged)
        hboxLayout.addWidget(self._replaceNumberSpinBox)

        gridLayout.addWidget(groupBox, 3, 0, Qt.AlignLeft)

        self._resultTabWidget = QTabWidget(widget)

        self._matchTextBrowser = QTextEdit()
        self._matchTextBrowser.setReadOnly(True)
        self._resultTabWidget.addTab(self._matchTextBrowser, "Match")

        tab = QWidget()
        self._groupTable = QTreeWidget(tab)
        self._groupTable.setHeaderLabels(["Match Number", "Idx", "Group Name", "Match"])
        self._groupTable.setItemsExpandable(False)
        self._groupTable.setRootIsDecorated(False)
        self._groupTable.setItemDelegate(MyQStyledItemDelegate())
        self._groupTable.setSelectionMode(QAbstractItemView.NoSelection)
        gridlayout2 = QGridLayout(tab)
        gridlayout2.addWidget(self._groupTable, 0, 0, 1, 1)
        self._resultTabWidget.addTab(tab, "Group")

        self._replaceTextBrowser = QTextEdit()
        self._replaceTextBrowser.setReadOnly(True)
        self._resultTabWidget.addTab(self._replaceTextBrowser, "Replace")

        self._codeTextBrowser = QTextEdit()
        self._codeTextBrowser.setReadOnly(True)
        self._resultTabWidget.addTab(self._codeTextBrowser, "Sample Code")

        gridLayout.addWidget(self._resultTabWidget, 4, 0, 1, 1)

        return widget


class MyQStyledItemDelegate(QStyledItemDelegate):

    def paint(self, painter, option, index):  # pragma: no cover - No way to test
        """Reimplements: QStyledItemDelegate::paint, drawing a box around the item"""

        QStyledItemDelegate.paint(self, painter, option, index)

        if index.column() > 0:  # and  not index.model().hasChildren(index):
            painter.save()
            painter.setPen(Qt.lightGray)
            painter.drawRect(option.rect)
            painter.restore()
