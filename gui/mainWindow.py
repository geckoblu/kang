from gui.mainWindowBA import MainWindowBA
from modules.util import getIcon


class MainWindow(MainWindowBA):
    
    def __init__(self, parent=None):
        MainWindowBA.__init__(self, parent)
        self.parent = parent
        
        self.setWindowIcon(getIcon('kang-icon'))