import sys

from PySide2.QtCore import Qt
from PySide2.QtGui import QBrush, QColor
from PySide2.QtWidgets import *

QCOLOR_EVIDENCE = QColor('#DDFFFF')

class MyQStyledItemDelegate(QStyledItemDelegate):

    def paint(self, painter, option, index):
        QStyledItemDelegate.paint(self, painter, option, index)

        if index.column() > 0: # and  not index.model().hasChildren(index):
            painter.save()
            painter.setPen(Qt.lightGray)
            painter.drawRect(option.rect)
            painter.restore();


class MyGui(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle("QTreeWidget Example")
        self.setGeometry(50, 50, 700, 400)

        treeWidget = QTreeWidget()
        treeWidget.setHeaderLabels(["Make", "Model", "Price"])

        treeWidget.setItemsExpandable(False)

        self.loadData(treeWidget)

        treeWidget.expandAll()
        treeWidget.setRootIsDecorated(False)

        # treeWidget.clear()

        treeWidget.setItemDelegate(MyQStyledItemDelegate())

        self.setCentralWidget(treeWidget)

        self.show()

    def loadData(self, treeWidget):
        item = QTreeWidgetItem(treeWidget)
        item.setText(0, 'A')
        item.setText(1, 'A.1')
        item.setText(2, 'A.2')

        child = QTreeWidgetItem()
        child.setText(1, 'A Child 1')
        child.setText(2, '333')
        item.addChild(child)

        child = QTreeWidgetItem()
        child.setText(1, 'A Child 2')
        child.setText(2, '333')
        item.addChild(child)

        b = QBrush(QCOLOR_EVIDENCE);

        item = QTreeWidgetItem(treeWidget)
        item.setText(0, 'B')
        item.setText(1, 'B.1')
        item.setText(2, 'B.2')

        child = QTreeWidgetItem()
        child.setText(1, 'B Child 1')
        child.setText(2, '333')
        child.setBackground(0 , b);
        child.setBackground(1 , b);
        child.setBackground(2 , b);
        item.addChild(child)

        child = QTreeWidgetItem()
        child.setText(1, 'B Child 2')
        child.setText(2, '333')
        child.setBackground(0 , b);
        child.setBackground(1 , b);
        child.setBackground(2 , b);
        item.addChild(child)

        item.setBackground(0 , b);
        item.setBackground(1 , b);
        item.setBackground(2 , b);

        item = QTreeWidgetItem(treeWidget)
        item.setText(0, 'C')
        item.setText(1, 'C.1')
        item.setText(2, 'C.2')

        child = QTreeWidgetItem()
        child.setText(1, 'C Child 1')
        child.setText(2, '333')
        item.addChild(child)

        child = QTreeWidgetItem()
        child.setText(1, 'C Child 2')
        child.setText(2, '333')
        item.addChild(child)


DATA = [
('Toyota', 'Camry', 25999),
('Honda', 'Accord', 25599),
('Chevrolet', 'Camaro', 35999)]

app = QApplication(sys.argv)
mygui = MyGui()
sys.exit(app.exec_())

# class MyQTreeWidget(QTreeWidget):
#
#    def drawRow(self, painter, option, index):
#        QTreeView.drawRow(self, painter, option, index)
#        painter.setPen(Qt.lightGray)
#        y = option.rect.y()
#        #saving is mandatory to keep alignment through out the row painting
#        painter.save()
#        painter.translate(self.visualRect(self.model().index(0, 0)).x() - self.indentation() - .5, -.5)
#        for sectionId in range(self.header().count() - 1):
#            painter.translate(self.header().sectionSize(sectionId), 0)
#            painter.drawLine(0, y, 0, y + option.rect.height())
#        painter.restore()
#        #don't draw the line before the root index
#        if index == self.model().index(0, 0):
#            return
#        painter.drawLine(0, y, option.rect.width(), y)
