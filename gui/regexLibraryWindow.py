from gui.regexLibraryWindowBA import RegexLibraryWindowBA
from modules.parseRegexLib import ParseRegexLib
from modules.util import restoreWindowSettings, saveWindowSettings, getIcon

from PyQt4.QtCore import SIGNAL

GEO = "regex-lib_geometry"

class RegexLibraryWindow(RegexLibraryWindowBA):
    
    def __init__(self, parent):
        RegexLibraryWindowBA.__init__(self, None)
        self.parent = parent
        self.selected = None

        restoreWindowSettings(self, GEO) 
        self.setWindowIcon(getIcon('kang-icon'))

        self.parseXML()
        self.populateListBox()       


    def closeEvent(self, ev):
        saveWindowSettings(self, GEO)
        ev.accept()


    def parseXML(self):
        parser = ParseRegexLib()
        self.xml_dicts = parser.parse()

        
    def populateListBox(self):
        for d in self.xml_dicts:
            self.descriptionListBox.addItem(d.get('desc', "<unknown>"))

        
    def descSelectedSlot(self, qlistboxitem):
        if qlistboxitem == None: return

        itemnum = self.descriptionListBox.currentRow()
        self.populateSelected(self.xml_dicts[itemnum])


    def populateSelected(self, xml_dict):
        self.regexTextBrowser.setPlainText(xml_dict.get('regex', ""))
        self.contribEdit.setText(xml_dict.get("contrib", ""))
        self.noteTextBrowser.setPlainText(xml_dict.get('note', ""))
        self.selected = xml_dict

        
    def editPaste(self):
        if self.selected:
            self.parent.emit(SIGNAL('pasteRegexLib(PyQt_PyObject)'), self.selected)
