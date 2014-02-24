#  about.py: -*- Python -*-  DESCRIPTIVE TEXT.

from aboutBA import AboutBA
from util import getPixmap
import version

class About(AboutBA):
    def __init__(self):
        AboutBA.__init__(self)
        self.versionLabel.setText(version.VERSION)
        self.image0 = getPixmap("kodos.png")
        self.PixmapLabel1.setPixmap(self.image0)

