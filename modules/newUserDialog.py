from modules.newUserDialogBA import NewUserDialogBA
from util import getPixmap


class NewUserDialog(NewUserDialogBA):
    
    def __init__(self, parent=None):
        NewUserDialogBA.__init__(self, parent)
        self.parent = parent
                
        image1 = getPixmap("library.png")
        self.pixmapLabel1.setPixmap(image1)
        
        image2 = getPixmap("book.png")
        self.pixmapLabel2.setPixmap(image2)