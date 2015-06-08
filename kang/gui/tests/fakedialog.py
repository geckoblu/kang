class FakeDialog():

    def __init__(self, parent, *args, **kargs):
        pass

    def setModal(self, modal):
        pass

    def show(self):
        pass

    def exec_(self):
        pass

    def showPrefsDialog(self):
        self.show()
