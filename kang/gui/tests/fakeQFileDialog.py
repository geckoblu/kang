class FakeQFileDialog:

    def __init__(self, empty=False, filename=''):
        self._empty = empty
        self._filename = filename

    def getOpenFileName(self, *args):
        return self

    def getSaveFileName(self, *args):
        return self

    def isEmpty(self):
        return self._empty

    def __str__(self):
        return self._filename
