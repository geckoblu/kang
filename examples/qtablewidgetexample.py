import sys

from PySide2.QtWidgets import QMainWindow, QTableWidget, QAction, QFileDialog, QApplication, QTableWidgetItem


class MyGui(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle("My GUI Program")
        self.setGeometry(50, 50, 700, 400)

        self.table = QTableWidget(1, 3)
        self.columnLabels = ["Make", "Model", "Price"]
        self.table.setHorizontalHeaderLabels(self.columnLabels)
        self.setCentralWidget(self.table)

        self.loadData()

        self.show()

    def loadData(self):
        self.table.setRowCount(len(DATA))
        for i in range(0, len(DATA)):
            row = DATA[i]
            make = QTableWidgetItem(row[0])
            model = QTableWidgetItem(row[1])
            price = QTableWidgetItem(str(row[2]))
            print(row[2])
            self.table.setItem(i, 0, make)
            self.table.setItem(i, 1, model)
            self.table.setItem(i, 2, price)
        self.table.resizeColumnsToContents()


DATA = [
('Toyota', 'Camry', 25999),
('Honda', 'Accord', 25599),
('Chevrolet', 'Camaro', 35999)]

app = QApplication(sys.argv)
mygui = MyGui()
sys.exit(app.exec_())
