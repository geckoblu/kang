# pylint: disable=missing-function-docstring

import os

# pylint: disable=unused-argument
class FakeQFileDialog:

    def __init__(self, filename):
        self._filename = filename

    def getOpenFileName(self, *args):
        if self._filename:
            (__, ext) = os.path.splitext(self._filename)
            return (self._filename, '*' + ext)
        else:
            return ('', '')

    def getSaveFileName(self, *args):
        return self.getOpenFileName(self, *args)
