from PyQt4.QtGui import QPixmap, QIcon
import os


def getPixmap(fileStr):
    """Return a QPixmap instance for the file fileStr relative
    to the binary location and residing in it's 'images' subdirectory"""

    imagepath = os.path.join(os.path.dirname(__file__), fileStr)

    pixmap = QPixmap(imagepath)
    pixmap.setMask(pixmap.createHeuristicMask(1))

    return pixmap


def getIcon(iconName):
    """Returns the QIcon corresponding to name in the current icon theme.
    If no such icon is found in the current theme a fallback is return instead."""
    icon = QIcon.fromTheme(iconName)
    if icon.isNull():
        icon = QIcon(getPixmap('%s.svg' % iconName))
    return icon
