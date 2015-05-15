import sys
import unittest

from kang.modules import exceptionHandler


class TestExceptionHandler(unittest.TestCase):

    def test_excepthook(self):
        mainWindow = FakeMainWindow()
        exceptionHandler.init(mainWindow, debug=True)

        try:
            raise ValueError('A very specific bad thing happened')
        except ValueError:
            _stderr = sys.stderr
            sys.stderr = mainWindow
            exc_type, exc_value, exc_traceback = sys.exc_info()
            exceptionHandler._excepthook(exc_type, exc_value, exc_traceback)
            sys.stderr = _stderr

        self.assertTrue(mainWindow.wok, 'Exception not printed to stderr')
        self.assertTrue(mainWindow.ok, 'Something wrong in the message\n%s' % mainWindow.message)


class FakeMainWindow:

    def __init__(self):
        self.ok = False
        self.message = ''
        self.wmessage = ''
        self.regexMultiLineEdit = FakeLineEdit('regexMultiLineEdit')
        self.stringMultiLineEdit = FakeLineEdit('stringMultiLineEdit')
        self.replaceTextEdit = FakeLineEdit('replaceTextEdit')

    def write(self, message):
        self.wmessage = message
        self.wok = message.find('ValueError: A very specific bad thing happened') > 0

    def signalException(self, message):
        self.message = message
        self.ok = (message.find('ValueError: A very specific bad thing happened') > 0)
        self.ok = self.ok and (message.find('regexMultiLineEdit') > 0)
        self.ok = self.ok and (message.find('stringMultiLineEdit') > 0)
        self.ok = self.ok and (message.find('replaceTextEdit') > 0)


class FakeLineEdit():

    def __init__(self, text):
        self._text = text

    def toPlainText(self):
        return self._text
