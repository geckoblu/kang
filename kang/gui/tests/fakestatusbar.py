from PySide2.QtWidgets import QWidget


class FakeStatusBar(QWidget):

    def addWidget(self, widget, pos):
        pass
