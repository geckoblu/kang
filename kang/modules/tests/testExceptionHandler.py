# pylint: disable=protected-access

import sys
import unittest

from kang.modules import exceptionHandler


class TestExceptionHandler(unittest.TestCase):

    def testExcepthook(self):
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

    def testExcepthookException(self):
        stderr = sys.stderr
        sys.stderr = None
        with self.assertRaises(AttributeError):
            exceptionHandler._excepthook(None, None, None)
        sys.stderr = stderr

    def testFormatMessageExmess(self):
        exceptionHandler._formatMessage('exmess')


class FakeMainWindow:

    def __init__(self):
        self.ok = False
        self.message = ''
        self.wok = False
        self.wmessage = ''
        self._regexMultiLineEdit = FakeLineEdit('_regexMultiLineEdit')
        self._stringMultiLineEdit = FakeLineEdit('_stringMultiLineEdit')
        self._replaceTextEdit = FakeLineEdit('_replaceTextEdit')

    def write(self, message):
        self.wmessage = message
        self.wok = message.find('ValueError: A very specific bad thing happened') > 0

    def _signalException(self, message):
        self.message = message
        self.ok = (message.find('ValueError: A very specific bad thing happened') > 0)
        self.ok = self.ok and (message.find('_regexMultiLineEdit') > 0)
        self.ok = self.ok and (message.find('_stringMultiLineEdit') > 0)
        self.ok = self.ok and (message.find('_replaceTextEdit') > 0)


class FakeLineEdit():

    def __init__(self, text):
        self._text = text

    def toPlainText(self):
        return self._text
