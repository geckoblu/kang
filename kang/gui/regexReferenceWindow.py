#  reference.py: -*- Python -*-  DESCRIPTIVE TEXT.

from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QTreeWidgetItem

from kang.gui.regexReferenceWindowBA import RegexReferenceWindowBA
from kang.modules.util import restoreWindowSettings, saveWindowSettings, getIcon


GEO = "regex-ref_geometry"

class RegexReferenceWindow(RegexReferenceWindowBA):
    
    def __init__(self, parent):
        RegexReferenceWindowBA.__init__(self, None)
        self.parent = parent

        restoreWindowSettings(self, GEO)
        self.setWindowIcon(getIcon('kang-icon'))
        
        self.populateTable()        


    def populateTable(self):
        
        items = []
        for r in references:
            items.append(QTreeWidgetItem(r))
            
        self.referenceTreeWidget.insertTopLevelItems(0, items)
        

    def closeEvent(self, ev):
        saveWindowSettings(self, GEO)
        ev.accept()


    def editPaste(self):
        list_view_item = self.referenceTreeWidget.selectedItems()
        if list_view_item :         
            symbol = str(list_view_item[0].text(0))
            self.parent.emit(SIGNAL('pasteSymbol(PyQt_PyObject)'), symbol)
            
        
references = []
references.append(('^', 'Matches start of string'))
references.append(('?', 'Matches 0 or 1 repetition of preceeding RE'))
references.append(('??', 'Non-greedy ?'))
references.append(('.', 'Matches any character'))
references.append(('(?<=...)', 'Matches if the current position in the string is preceded by a match for ... that ends at the current position. This is called a positive lookbehind assertion.'))
references.append(('(?<!...)', 'Matches if the current position in the string is not preceded by a match for .... This is called a negative lookbehind assertion.'))
references.append(('(?=...) ', "Matches if ... matches next, but doesn't consume any of the string. This is called a lookahead assertion."))
references.append(('(?:)', 'Non-capturing Parenthesis'))
references.append(('(?!...)', "Matches if ... doesn't match next. This is a negative lookahead assertion"))
references.append(('(?#...) ', 'A comment; the contents of the parentheses are simply ignored.  '))
references.append(('()', 'Capturing Parenthesis'))
references.append(('[]', 'Character class'))
references.append(('$', 'Matches the end of the string'))
references.append(('*', 'Matches 0 or more repetition of preceeding RE'))
references.append(('*?', 'Non-greedy *'))
references.append(('\\', 'Matches a literal backslash'))
references.append(('+', 'Matches 1 or more repetition of preceeding RE'))
references.append(('+?', 'Non-greedy +'))
references.append(('\\A', 'Matches only at the start of the string'))
references.append(('\\b', 'Matches the empty string, but only at the beginning or end of a word'))
references.append(('\\B', 'Matches the empty string, but only when it is not at the beginning or end of a  word'))
references.append(('\\d', 'Matches any decimal digit'))
references.append(('\\D', 'Matches any non-digit character'))
references.append(('{m,n}', 'match from m to n repetitions of the preceding RE, attempting to match as many repetitions as possible. '))
references.append(('{m,n}?', 'match from m to n repetitions of the preceding RE, attempting to match as few repetitions as possible. '))
references.append(('\\number ', 'Matches the contents of the group of the same number. Groups are numbered starting from 1.'))
references.append(('(?P<name>...)', 'Similar to regular parentheses, but the substring matched by the group is accessible via the symbolic group name name.'))
references.append(('(?P=name)', 'Matches whatever text was matched by the earlier group named name. '))
references.append(('\\s', 'Matches any whitespace character'))
references.append(('\\S', 'Matches any non-whitespace character'))
references.append(('\\w', 'Matches any word'))
references.append(('\\W', 'Matches any non-word'))
references.append(('\\z', 'Matches only at the end of the string'))


