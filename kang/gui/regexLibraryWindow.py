from PySide2.QtCore import SIGNAL

from kang.gui.regexLibraryWindowBA import RegexLibraryWindowBA
from kang.images import getIcon
from kang.modules.parseRegexLib import ParseRegexLib
from kang.modules.util import restoreWindowSettings, saveWindowSettings


GEO = "regex-lib_geometry"


class RegexLibraryWindow(RegexLibraryWindowBA):

    def __init__(self, parent):
        RegexLibraryWindowBA.__init__(self, None)
        self.parent = parent
        self.selected = None
        self.regexLibDicts = []

        restoreWindowSettings(self, GEO)
        self.setWindowIcon(getIcon('kang-icon'))

        self.parseXML()
        self.populateListBox()

    def closeEvent(self, event):
        saveWindowSettings(self, GEO)
        event.accept()

    def parseXML(self):
        parser = ParseRegexLib()
        self.regexLibDicts = parser.parse()

    def populateListBox(self):
        for d in self.regexLibDicts:
            self.descriptionListBox.addItem(d.get('desc', "<unknown>"))

    def descSelectedSlot(self, qlistboxitem):
        if qlistboxitem is None:
            return

        itemnum = self.descriptionListBox.currentRow()
        self.populateSelected(self.regexLibDicts[itemnum])

    def populateSelected(self, regexLibDict):
        self.regexTextBrowser.setPlainText(regexLibDict.get('regex', ""))
        self.contribEdit.setText(regexLibDict.get("contrib", ""))
        self.noteTextBrowser.setPlainText(regexLibDict.get('note', ""))
        self.selected = regexLibDict

    def editPaste(self):
        if self.selected:
            self.parent.emit(SIGNAL('pasteRegexLib(PyQt_PyObject)'), self.selected)
