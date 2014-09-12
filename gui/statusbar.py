#  status_bar.py: -*- Python -*-  DESCRIPTIVE TEXT.

from PyQt4.QtCore import QTimer, SIGNAL
from PyQt4.QtGui import QLabel

from modules.util import getPixmap


class StatusBar:
    def __init__(self, parent, message=''):
        self.parent = parent

        self.statusBar = parent.statusBar()
        self.__statusTimer = QTimer(self.parent)

        self.parent.connect(self.__statusTimer, SIGNAL("timeout()"), self._resetMessage)
        
        self.__statusLabel = QLabel(self.statusBar)
        
        self.replaceStatusMessage = False
        self.lastStatusMessage = ''

        pixmap = getPixmap("yellow.png")

        self.pixmapLabel = QLabel("image", self.statusBar)
        self.pixmapLabel.setPixmap(pixmap)
        
        self.statusBar.addWidget(self.pixmapLabel, 0)
        self.statusBar.addWidget(self.__statusLabel, 1)
        #if progress_bar:
        #    self.progressBar = QProgressBar(self.statusBar)
        #    self.statusBar.addWidget(self.progressBar, 1)

        if message:
            self.set_message(message)
    

    def setMessage(self, message='', duration=0, pixmap=''):
        """sets the status bar message label to message.

        if duration is > 0 than the message is displayed for duration seconds.

        if duration is > 0 and replace is true then after duration seconds
        have elapsed, the previous message is displayed. 
        """
        
        replace = (duration > 0)

        self.__statusTimer.stop()
        self.lastStatusMessage = unicode(self.__statusLabel.text())
        self.replaceStatusMessage = replace

        self.__statusLabel.setText(message)

        if duration > 0:
            self.__statusTimer.start(1000 * duration)

        if pixmap:
            self.pixmapLabel.setPixmap(pixmap)
        

    
    def _resetMessage(self):
        self.__statusTimer.stop()
        if self.replaceStatusMessage:
            self.__statusLabel.setText(self.lastStatusMessage)
        else:
            self.__statusLabel.setText('')
