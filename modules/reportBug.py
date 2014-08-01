#  reportBug.py: -*- Python -*-  DESCRIPTIVE TEXT.

from PyQt4.QtCore import QT_VERSION_STR
from PyQt4.QtGui import QMessageBox
import smtplib
import string
import sys

from reportBugBA import reportBugBA
from util import getIcon
from version import VERSION


AUTHOR_ADDR = 'phil_schwartz@users.sourceforge.net'

class reportBug(reportBugBA):
    def __init__(self, parent=None):
        reportBugBA.__init__(self, parent)
        self.parent = parent
        self.kodos_main = parent
        self.populate()
        
        closeicon = getIcon('window-close');
        self.closeAction.setIcon(closeicon)
        

    def populate(self):
        self.OSEdit.setText(sys.platform)
        pyvers = string.replace(sys.version, '\n', ' - ')
        self.pythonVersionEdit.setText(pyvers)
        self.pyQtVersionEdit.setText(QT_VERSION_STR)
        self.regexMultiLineEdit.setText(self.kodos_main.regexMultiLineEdit.toPlainText())
        self.stringMultiLineEdit.setText(self.kodos_main.stringMultiLineEdit.toPlainText())


#     def cancel_slot(self):
#         self.parent.close()

    def submit(self):
        addr = str(self.emailAddressEdit.text())
        if not addr:
            msg = self.tr(
                'An email address is necessary so that the author '
                'can contact you.  Your email address will not '
                'be used for any other purposes.')

            QMessageBox.information(None,
                                    self.tr('You must supply a valid email address'),
                                    msg)
            return 

        msg = 'Subject: Kodos bug report\n\n'
        msg += 'Kodos Version: %s\n' % VERSION
        msg += 'Operating System: %s\n' % unicode(self.OSEdit.text())
        msg += 'Python Version: %s\n' % unicode(self.pythonVersionEdit.text())
        msg += 'PyQt Version: %s\n' % unicode(self.pyQtVersionEdit.text())
        msg += '\n' + '=' * 70 + '\n'
        msg += 'Regex:\n%s\n' % unicode(self.regexMultiLineEdit.toPlainText())
        msg += '=' * 70 + '\n'
        msg += 'String:\n%s\n' % unicode(self.stringMultiLineEdit.toPlainText())
        msg += '=' * 70 + '\n'
        msg += 'Comments:\n%s\n' % unicode(self.commentsMultiLineEdit.toPlainText())
        email_server = unicode(self.kodos_main.prefs.emailServerEdit.text()) or 'localhost'
        try:
            server = smtplib.SMTP(email_server)
            server.sendmail(addr, AUTHOR_ADDR, msg)
            server.quit()
            QMessageBox.information(None,
                                    self.tr('Bug report sent'),
                                    self.tr('Your bug report has been sent.'))
            self.parent.close()
        except Exception, e:
            QMessageBox.information(None,
                                    self.tr('An exception occurred sending bug report'),
                                    str(e))
        

# class reportBugWindow(QMainWindow):
#     def __init__(self, kodos_main):
#         self.kodos_main = kodos_main
#         
#         QMainWindow.__init__(self, None, Qt.WindowFlags(Qt.Window | Qt.WA_DeleteOnClose))
#         
#         self.setGeometry(100, 50, 800, 600)
#         self.setWindowTitle(self.tr('Report a Bug'))
#         self.setWindowIcon(QIcon(QPixmap(xpm.kodosIcon)))
#         self.bug_report = reportBug(self)
#         self.setCentralWidget(self.bug_report)
# 
#         
#         self.createMenu()
#         self.createToolBar()
# 
#         self.show()
# 
# 
#     def createMenu(self):
#         pass
# #         self.filemenu = QPopupMenu()
# #         id = self.filemenu.insertItem(self.tr('&Close'), self, SLOT('close()'))
# # 
# #         self.menubar = QMenuBar(self)
# #         self.menubar.insertItem(self.tr('&File'), self.filemenu)
# 
# 
#     def createToolBar(self):
#         toolbar = QToolBar(self)
#         #toolbar.setStretchableWidget(self.menubar)
#         self.logolabel = kodos_toolbar_logo(toolbar)
 
