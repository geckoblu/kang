from PySide2.QtGui import QWidget


class FakeStatusBar(QWidget):

    def addWidget(self, widget, pos):
        pass
