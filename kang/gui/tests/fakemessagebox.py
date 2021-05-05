from PyQt5.Qt import QMessageBox


class FakeMessageBox(QMessageBox):

    def __init__(self, *args, **kwargs):
        super(FakeMessageBox, self).__init__(*args, **kwargs)
        self.parent = None
        self.title = ''
        self.text = ''
        self.informationCalled = False
        self.criticalCalled = False
        self.warningCalled = False

    def information(self, parent, title, text, *args, **kargs):
        self.informationCalled = True
        self.parent = parent
        self.title = title
        self.text = text

    def critical(self, parent, title, text, *args, **kargs):
        self.criticalCalled = True
        self.parent = parent
        self.title = title
        self.text = text

    def warning(self, parent, title, text, *args, **kargs):
        self.warningCalled = True
        self.parent = parent
        self.title = title
        self.text = text
        return 0
