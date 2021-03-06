from PyQt4.QtCore import QTimer, SIGNAL
from PyQt4.QtGui import QLabel, QPixmap


class StatusBar:

    def __init__(self, parent):
        self._parent = parent

        self._statusTimer = QTimer(self._parent)
        self._parent.connect(self._statusTimer, SIGNAL("timeout()"), self._resetMessage)

        self._replaceStatusMessage = False
        self._lastStatusMessage = ''
        self._lastStatusPixmap = QPixmap()

        self._statusBar = parent.statusBar()
        self._statusLabel = QLabel(self._statusBar)

        self._pixmapLabel = QLabel(self._statusBar)
        self._pixmapLabel.setPixmap(self._lastStatusPixmap)

        self._statusBar.addWidget(self._pixmapLabel, 0)
        self._statusBar.addWidget(self._statusLabel, 1)

    def setMessage(self, message='', duration=0, pixmap=''):
        """Sets the status bar message label to message.

        if duration is > 0 than the message is displayed for duration seconds.

        if duration is > 0 then after duration seconds
        have elapsed, the previous message is displayed.
        """

        replace = (duration > 0)

        self._statusTimer.stop()

        self._replaceStatusMessage = replace
        self._lastStatusMessage = self._statusLabel.text()
        self._lastStatusPixmap = self._pixmapLabel.pixmap().copy()

        self._statusLabel.setText(message)

        if duration > 0:
            self._statusTimer.start(1000 * duration)

        if pixmap:
            self._pixmapLabel.setPixmap(pixmap)

    def _resetMessage(self):
        self._statusTimer.stop()
        if self._replaceStatusMessage:
            self._statusLabel.setText(self._lastStatusMessage)
            self._pixmapLabel.setPixmap(self._lastStatusPixmap)
        else:
            self._statusLabel.setText('')
            self._pixmapLabel.setPixmap(QPixmap())
