from PySide2.QtWidgets import QSplitter, QListView, QTreeView, QTextEdit, \
    QApplication, QMainWindow
import sys


def load(window):
    splitter = QSplitter(window)
    
    listview = QTextEdit() # QListView()
    # treeview = QTreeView()
    textedit = QTextEdit()
    
    splitter.addWidget(listview)
    # splitter.addWidget(treeview)
    splitter.addWidget(textedit)
    
if __name__ == '__main__':    
    qApp = QApplication(sys.argv)
     
    window = QMainWindow()
    window.setGeometry(50, 50, 700, 400)
    
    load(window)
    
    window.show()
    
    qApp.exec_()