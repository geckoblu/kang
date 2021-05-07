from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

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
        self.askSaveCheckbox.setChecked(self.preferences.askSave)
        self.askSaveCheckbox2.setChecked(self.preferences.askSaveOnlyForNamedProjects)

        self.askSaveCheckbox2.setEnabled(self.askSaveCheckbox.isChecked())

        self.show()

    def apply(self):
        self.preferences.recentFilesNum = self.recentFilesSpinBox.value()
        self.preferences.askSave = self.askSaveCheckbox.isChecked()
        self.preferences.askSaveOnlyForNamedProjects = self.askSaveCheckbox2.isChecked()

        self.preferences.save()
        self.parent.emit(SIGNAL('preferencesChanged()'))

    def accept(self):
        self.apply()
        QDialog.accept(self)

    def askSaveCheckboxToogled(self):
        self.askSaveCheckbox2.setEnabled(self.askSaveCheckbox.isChecked())
