from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QDialog, QFontDialog

from kang.gui.preferencesDialogBA import PreferencesDialogBA
from kang.images import getIcon


class PreferencesDialog(PreferencesDialogBA):
    
    
    def __init__(self, parent, preferences):
        PreferencesDialogBA.__init__(self, parent)
        self.parent = parent
        self.preferences = preferences
        
        self.setWindowIcon(getIcon('kang-icon'))


    def setFontButtonText(self, button, font):
        button.setText("%s %s" % (str(font.family()),font.pointSize() ))


    def showPrefsDialog(self):
        f = self.preferences.editorFont
        self.editorFontButton.setFont(f)
        self.setFontButtonText(self.editorFontButton, f)

        f = self.preferences.matchFont
        self.matchFontButton.setFont(f)
        self.setFontButtonText(self.matchFontButton, f)
        
        self.recentFilesSpinBox.setValue(self.preferences.recentFilesNum)

        self.show()


    def chooseEditorFont(self):
        (font, ok) = QFontDialog.getFont(self.editorFontButton.font())
        if ok:
            self.editorFontButton.setFont(font)
            self.setFontButtonText(self.editorFontButton, font)


    def chooseMatchFont(self):
        (font, ok) = QFontDialog.getFont(self.matchFontButton.font())
        if ok:            
            self.matchFontButton.setFont(font)
            self.setFontButtonText(self.matchFontButton, font)        


    def apply(self):
        self.preferences.editorFont = self.editorFontButton.font()
        self.preferences.matchFont = self.matchFontButton.font()
        self.preferences.recentFilesNum = self.recentFilesSpinBox.value()
        
        self.preferences.save()
        self.parent.emit(SIGNAL('preferencesChanged()'))


    def accept(self):
        self.apply()
        QDialog.accept(self)

