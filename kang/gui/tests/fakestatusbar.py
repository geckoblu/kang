from PyQt4.QtGui import QWidget


class FakeStatusBar(QWidget):

    def addWidget(self, widget, pos):
        pass
