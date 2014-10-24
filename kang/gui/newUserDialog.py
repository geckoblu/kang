from kang.gui.newUserDialogBA import NewUserDialogBA
from kang.modules.util import getPixmap, getIcon


class NewUserDialog(NewUserDialogBA):
    
    def __init__(self, parent=None):
        NewUserDialogBA.__init__(self, parent)
        self.parent = parent
        
        self.setWindowIcon(getIcon('kang-icon'))
                
        image1 = getPixmap("library.svg")
        self.pixmapLabel1.setPixmap(image1)
        
        image2 = getPixmap("book.svg")
        self.pixmapLabel2.setPixmap(image2)