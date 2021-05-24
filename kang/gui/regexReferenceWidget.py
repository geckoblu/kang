from PySide2.QtCore import Signal
from PySide2.QtWidgets import QWidget, QTreeWidget, QAbstractItemView, QTreeWidgetItem, QVBoxLayout

tr = lambda msg: msg


class RegexReferenceWidget(QWidget):

    pasteSymbol = Signal(str)

    def __init__(self):
        QWidget.__init__(self)

        referencesTable = QTreeWidget()
        referencesTable.setHeaderLabels([tr("Symbol"), tr("Definition")])
        referencesTable.setSelectionMode(QAbstractItemView.SingleSelection)

        for reference in _REFERENCES:
            item = QTreeWidgetItem(referencesTable, reference)
            item.setToolTip(0, reference[1])
            item.setToolTip(1, reference[1])

        referencesTable.doubleClicked.connect(self._emitSymbol)

        verticalLayout = QVBoxLayout(self)
        verticalLayout.addWidget(referencesTable)

    def _emitSymbol(self, modelIndex):
        self.pasteSymbol.emit(_REFERENCES[modelIndex.row()][0])


_REFERENCES = [
    ('^', 'Matches start of string'),
    ('?', 'Matches 0 or 1 repetition of preceeding RE'),
    ('??', 'Non-greedy ?'),
    ('.', 'Matches any character'),
    ('(?<=...)', 'Matches if the current position in the string is preceded by a match for ... ' \
                 'that ends at the current position. This is called a positive lookbehind assertion.'),
    ('(?<!...)', 'Matches if the current position in the string is not preceded by a match for .... ' \
                 'This is called a negative lookbehind assertion.'),
    ('(?=...) ', "Matches if ... matches next, but doesn't consume any of the string." \
                 "This is called a lookahead assertion."),
    ('(?:)', 'Non-capturing Parenthesis'),
    ('(?!...)', "Matches if ... doesn't match next. This is a negative lookahead assertion"),
    ('(?#...) ', 'A comment; the contents of the parentheses are simply ignored.  '),
    ('()', 'Capturing Parenthesis'),
    ('[]', 'Character class'),
    ('$', 'Matches the end of the string'),
    ('*', 'Matches 0 or more repetition of preceeding RE'),
    ('*?', 'Non-greedy *'),
    ('\\', 'Matches a literal backslash'),
    ('+', 'Matches 1 or more repetition of preceeding RE'),
    ('+?', 'Non-greedy +'),
    ('\\A', 'Matches only at the start of the string'),
    ('\\b', 'Matches the empty string, but only at the beginning or end of a word'),
    ('\\B', 'Matches the empty string, but only when it is not at the beginning or end of a  word'),
    ('\\d', 'Matches any decimal digit'),
    ('\\D', 'Matches any non-digit character'),
    ('{m,n}', 'match from m to n repetitions of the preceding RE, attempting to match '\
              'as many repetitions as possible. '),
    ('{m,n}?', 'match from m to n repetitions of the preceding RE, attempting to match ' \
               'as few repetitions as possible. '),
    ('\\number ', 'Matches the contents of the group of the same number. Groups are numbered starting from 1.'),
    ('(?P<name>...)', 'Similar to regular parentheses, but the substring matched by the group ' \
                      'is accessible via the symbolic group name name.'),
    ('(?P=name)', 'Matches whatever text was matched by the earlier group named name. '),
    ('\\s', 'Matches any whitespace character'),
    ('\\S', 'Matches any non-whitespace character'),
    ('\\w', 'Matches any word'),
    ('\\W', 'Matches any non-word'),
    ('\\z', 'Matches only at the end of the string')]
