from kang.gui.newUserDialogBA import Ui_NewUserDialogBA
from kang.images import getPixmap, getIcon


class NewUserDialog(Ui_NewUserDialogBA):

    def __init__(self, parent=None):
        Ui_NewUserDialogBA.__init__(self, parent)
        self.parent = parent

        self.setWindowIcon(getIcon('kang-icon'))

        image1 = getPixmap("library.svg")
        self.pixmapLabel1.setPixmap(image1)

        image2 = getPixmap("book.svg")
        self.pixmapLabel2.setPixmap(image2)
