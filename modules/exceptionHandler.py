from PyQt4.QtCore import QT_VERSION_STR
import string
import sys
import traceback

from modules import VERSION


_mainWindow = None
_showedexmess = set()

def init(mainWindow):
    """
    Initialize the module
    """
    global _mainWindow
    _mainWindow = mainWindow
    sys.excepthook = _excepthook


def _excepthook(excType, excValue, tracebackobj):
    """
    Global function to catch unhandled exceptions.
    
    @param excType exception type
    @param excValue exception value
    @param tracebackobj traceback object
    """
        
    global _showedexmess
        
    try:
        tb = traceback.format_exception(excType, excValue, tracebackobj)
        exmess = ''.join(tb)
        sys.stderr.write(exmess)
        if _mainWindow and not (exmess in _showedexmess):
            _showedexmess.add(exmess)
            msg = _formatMessage(exmess)
            _mainWindow.signalException(msg)
    except:
        pass

def _formatMessage(exmess):
    """
    Format the exception message
    """
    msg  = '==========================================================================\n'
    msg += 'Kang Version:\t %s\n' % VERSION
    msg += 'Python Version:\t %s\n' % unicode(string.replace(sys.version, '\n', ' - '))
    msg += 'PyQt Version:\t %s\n' % unicode(QT_VERSION_STR)
    msg += 'Operating System: %s\n' % unicode(sys.platform)
    
    regex = _mainWindow.regexMultiLineEdit.toPlainText()
    if regex:
        msg += '=== REGEX ============================================================\n'
        msg += unicode(regex)
        if not msg.endswith('\n'):
            msg += '\n'
        
    rstr = _mainWindow.stringMultiLineEdit.toPlainText()
    if rstr:
        msg += '=== STRING ===========================================================\n'
        msg += unicode(rstr)
        if not msg.endswith('\n'):
            msg += '\n'
        
    replace = _mainWindow.replaceTextEdit.toPlainText()
    if replace:
        msg += '=== REPLACE ==========================================================\n'
        msg += unicode(replace)
        if not msg.endswith('\n'):
            msg += '\n'
    
    if exmess:
        msg += '=== EXCEPTION ========================================================\n'
        msg += unicode(exmess)
        if not msg.endswith('\n'):
            msg += '\n'
        
    return msg  

    