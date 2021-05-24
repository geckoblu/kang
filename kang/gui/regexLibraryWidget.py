from PySide2.QtWidgets import QWidget, QTreeWidget, QAbstractItemView, QVBoxLayout, QTreeWidgetItem

from kang.modules.parseRegexLib import ParseRegexLib

tr = lambda msg: msg


class RegexLibraryWidget(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        refTable = QTreeWidget()
        refTable.setHeaderLabels([tr("Description")])
        refTable.setSelectionMode(QAbstractItemView.SingleSelection)

        parser = ParseRegexLib()
        regexLibDicts = parser.parse()
        # TODO: cmplete the widget
        # print(regexLibDicts)

        for entry in regexLibDicts:
            # print(entry)
            QTreeWidgetItem(refTable, [entry['desc']])

        verticalLayout = QVBoxLayout(self)
        verticalLayout.addWidget(refTable)
