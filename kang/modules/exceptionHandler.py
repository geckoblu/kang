# pylint: disable=global-statement,invalid-name,c-extension-no-member,superfluous-parens
import sys
import traceback

from PySide2 import QtCore

from kang import VERSION

__mainWindow = None
__showedexmess = set()
__debug = False


def init(mainWindow, debug=False):
    """
    Initialize the module
    """
    global __mainWindow
    global __debug
    __mainWindow = mainWindow
    __debug = debug
    sys.excepthook = _excepthook


# pylint: disable=protected-access
def _excepthook(excType, excValue, tracebackObj):
    """
    Global function to catch unhandled exceptions.

    @param excType exception type
    @param excValue exception value
    @param tracebackObj traceback object
    """

    try:
        tb = traceback.format_exception(excType, excValue, tracebackObj)
        exmess = ''.join(tb)
        sys.stderr.write(exmess)
        if __mainWindow and not (exmess in __showedexmess):
            __showedexmess.add(exmess)
            msg = _formatMessage(exmess)
            __mainWindow._signalException(msg)
    except:
        if __debug:
            raise


# pylint: disable=protected-access
def _formatMessage(exmess):
    """
    Format the exception message
    """
    msg = '======================================================================\n'
    msg += 'Kang Version:\t %s\n' % VERSION
    msg += 'Python Version:\t %s\n' % str.replace(sys.version, '\n', ' - ')
    msg += 'PyQt Version:\t %s\n' % QtCore.__version__
    msg += 'Operating System: %s\n' % sys.platform

    regex = __mainWindow._regexMultiLineEdit.toPlainText()
    if regex:
        msg += '=== REGEX ============================================================\n'
        msg += regex
        if not msg.endswith('\n'):
            msg += '\n'

    rstr = __mainWindow._stringMultiLineEdit.toPlainText()
    if rstr:
        msg += '=== STRING ===========================================================\n'
        msg += rstr
        if not msg.endswith('\n'):
            msg += '\n'

    replace = __mainWindow._replaceTextEdit.toPlainText()
    if replace:
        msg += '=== REPLACE ==========================================================\n'
        msg += replace
        if not msg.endswith('\n'):
            msg += '\n'

    if exmess:
        msg += '=== EXCEPTION ========================================================\n'
        msg += exmess
        if not msg.endswith('\n'):
            msg += '\n'

    return msg
