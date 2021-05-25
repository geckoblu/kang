from PySide2.QtCore import Qt, Signal
from PySide2.QtWidgets import QWidget, QTreeWidget, QAbstractItemView, QVBoxLayout, \
                              QTreeWidgetItem, QTabWidget, QSplitter, QTextEdit, QLabel

from kang.modules.regexlibrary import REGEXLIBRARY

tr = lambda msg: msg


class RegexLibraryWidget(QWidget):

    emitEntry = Signal(dict)

    def __init__(self):
        QWidget.__init__(self)

        self._refTable = QTreeWidget()
        self._refTable.setHeaderLabels([tr("Description")])
        self._refTable.setSelectionMode(QAbstractItemView.SingleSelection)

        tabWidget = QTabWidget()

        self._regexEdit = QTextEdit()
        self._regexEdit.setReadOnly(True)
        tabWidget.addTab(self._regexEdit, tr("Regex"))

        notesWidget = QWidget()
        vLayout = QVBoxLayout(notesWidget)
        self._noteEdit = QTextEdit()
        self._noteEdit.setReadOnly(True)
        vLayout.addWidget(self._noteEdit)
        self._contribLabel = QLabel(tr("Contributed by:"))
        vLayout.addWidget(self._contribLabel)
        tabWidget.addTab(notesWidget, tr("Note"))

        splitter = QSplitter(Qt.Vertical)
        splitter.addWidget(self._refTable)
        splitter.addWidget(tabWidget)

        verticalLayout = QVBoxLayout(self)
        verticalLayout.addWidget(splitter)

        for entry in REGEXLIBRARY:
            desc = entry['desc']
            item = QTreeWidgetItem(self._refTable, [desc])
            item.setToolTip(0, desc)

        self._refTable.currentItemChanged.connect(self._currentItemChanged)
        self._refTable.doubleClicked.connect(self._emitEntry)

    def _currentItemChanged(self, current):
        index = self._refTable.indexOfTopLevelItem(current)
        entry = REGEXLIBRARY[index]
        self._regexEdit.setPlainText(entry['regex'])
        self._noteEdit.setPlainText(entry['note'])
        lbltxt = tr("Contributed by:") + " " + entry['contributor']
        self._contribLabel.setText(lbltxt)

    def _emitEntry(self, modelIndex):
        entry = REGEXLIBRARY[modelIndex.row()]
        self.emitEntry.emit(entry)
