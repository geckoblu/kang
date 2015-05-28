from PyQt4.QtGui import QWidget


class FakeMessageBox(QWidget):

    def __init__(self, *args, **kwargs):
        super(FakeMessageBox, self).__init__(*args, **kwargs)
        self.parent = None
        self.title = ''
        self.text = ''
        self.informationCalled = False

    def information(self, parent, title, text):
        self.informationCalled = True
        self.parent = parent
        self.title = title
        self.text = text
