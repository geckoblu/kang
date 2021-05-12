from PySide2 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent=parent)

        layout = QtWidgets.QVBoxLayout()

        self.treewidget = QtWidgets.QTreeWidget()

        layout.addWidget(self.treewidget)

        self.setLayout(layout)

        self.treewidget.setColumnCount(4)
        self.build_tree()

    def build_tree(self):
        for _index in range(10):
            item = QtWidgets.QTreeWidgetItem(self.treewidget)
            item.setText(0, 'icon 1')
            item.setText(1, 'icon 2')

            line_edit = QtWidgets.QLineEdit(self.treewidget)

            push_button = QtWidgets.QPushButton(self.treewidget)
            push_button.setText('TEST')

            self.treewidget.setItemWidget(item, 2, line_edit)
            self.treewidget.setItemWidget(item, 3, push_button)

    def build_tree2(self):
        for _index in range(10):
            item = QtWidgets.QTreeWidgetItem(self.treewidget)

            widget = QtWidgets.QWidget()
            layout = QtWidgets.QHBoxLayout()

            label_1 = QtWidgets.QLabel('icon 1')
            label_2 = QtWidgets.QLabel('icon 2')
            line_edit = QtWidgets.QLineEdit()
            push_button = QtWidgets.QPushButton('TEST')

            layout.addWidget(label_1)
            layout.addWidget(label_2)
            layout.addWidget(line_edit)
            layout.addWidget(push_button)

            widget.setLayout(layout)

            self.treewidget.setItemWidget(item, 0, widget)


app = QtWidgets.QApplication([])
window = Window()
window.setGeometry(50, 50, 700, 400)
window.show()
app.exec_()
