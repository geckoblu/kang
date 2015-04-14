from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QDialog

from kang.gui.preferencesDialogBA import PreferencesDialogBA
from kang.images import getIcon


class PreferencesDialog(PreferencesDialogBA):

    def __init__(self, parent, preferences):
        PreferencesDialogBA.__init__(self, parent)
        self.parent = parent
        self.preferences = preferences

        self.setWindowIcon(getIcon('kang-icon'))

    def showPrefsDialog(self):
        self.recentFilesSpinBox.setValue(self.preferences.recentFilesNum)

        self.show()

    def apply(self):
        self.preferences.recentFilesNum = self.recentFilesSpinBox.value()

        self.preferences.save()
        self.parent.emit(SIGNAL('preferencesChanged()'))

    def accept(self):
        self.apply()
        QDialog.accept(self)
