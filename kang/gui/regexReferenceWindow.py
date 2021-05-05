from PyQt5.QtCore import SIGNAL
from PyQt5.QtGui import QTreeWidgetItem

from kang.gui.regexReferenceWindowBA import Ui_RegexReferenceWindowBA
from kang.images import getIcon
from kang.modules.util import restoreWindowSettings, saveWindowSettings


GEO = "regex-ref_geometry"


class RegexReferenceWindow(Ui_RegexReferenceWindowBA):

    def __init__(self, parent):
        Ui_RegexReferenceWindowBA.__init__(self, None)
        self.parent = parent

        restoreWindowSettings(self, GEO)
        self.setWindowIcon(getIcon('kang-icon'))

        self.populateTable()

    def populateTable(self):

        items = []
        for r in REFERENCES:
            items.append(QTreeWidgetItem(r))

        self.referenceTreeWidget.insertTopLevelItems(0, items)

    def closeEvent(self, event):
        saveWindowSettings(self, GEO)
        event.accept()

    def editPaste(self):
        items = self.referenceTreeWidget.selectedItems()
        if items:
            symbol = str(items[0].text(0))
            self.parent.emit(SIGNAL('pasteSymbol(PyQt_PyObject)'), symbol)

REFERENCES = []
REFERENCES.append(('^', 'Matches start of string'))
REFERENCES.append(('?', 'Matches 0 or 1 repetition of preceeding RE'))
REFERENCES.append(('??', 'Non-greedy ?'))
REFERENCES.append(('.', 'Matches any character'))
REFERENCES.append(('(?<=...)',
                   'Matches if the current position in the string is preceded by a match for ... ' \
                   'that ends at the current position. This is called a positive lookbehind assertion.'))
REFERENCES.append(('(?<!...)',
                   'Matches if the current position in the string is not preceded by a match for .... ' \
                   'This is called a negative lookbehind assertion.'))
REFERENCES.append(('(?=...) ', "Matches if ... matches next, but doesn't consume any of the string. This is called a lookahead assertion."))
REFERENCES.append(('(?:)', 'Non-capturing Parenthesis'))
REFERENCES.append(('(?!...)', "Matches if ... doesn't match next. This is a negative lookahead assertion"))
REFERENCES.append(('(?#...) ', 'A comment; the contents of the parentheses are simply ignored.  '))
REFERENCES.append(('()', 'Capturing Parenthesis'))
REFERENCES.append(('[]', 'Character class'))
REFERENCES.append(('$', 'Matches the end of the string'))
REFERENCES.append(('*', 'Matches 0 or more repetition of preceeding RE'))
REFERENCES.append(('*?', 'Non-greedy *'))
REFERENCES.append(('\\', 'Matches a literal backslash'))
REFERENCES.append(('+', 'Matches 1 or more repetition of preceeding RE'))
REFERENCES.append(('+?', 'Non-greedy +'))
REFERENCES.append(('\\A', 'Matches only at the start of the string'))
REFERENCES.append(('\\b', 'Matches the empty string, but only at the beginning or end of a word'))
REFERENCES.append(('\\B', 'Matches the empty string, but only when it is not at the beginning or end of a  word'))
REFERENCES.append(('\\d', 'Matches any decimal digit'))
REFERENCES.append(('\\D', 'Matches any non-digit character'))
REFERENCES.append(('{m,n}', 'match from m to n repetitions of the preceding RE, attempting to match as many repetitions as possible. '))
REFERENCES.append(('{m,n}?', 'match from m to n repetitions of the preceding RE, attempting to match as few repetitions as possible. '))
REFERENCES.append(('\\number ', 'Matches the contents of the group of the same number. Groups are numbered starting from 1.'))
REFERENCES.append(('(?P<name>...)', 'Similar to regular parentheses, but the substring matched by the group is accessible via the symbolic group name name.'))
REFERENCES.append(('(?P=name)', 'Matches whatever text was matched by the earlier group named name. '))
REFERENCES.append(('\\s', 'Matches any whitespace character'))
REFERENCES.append(('\\S', 'Matches any non-whitespace character'))
REFERENCES.append(('\\w', 'Matches any word'))
REFERENCES.append(('\\W', 'Matches any non-word'))
REFERENCES.append(('\\z', 'Matches only at the end of the string'))
