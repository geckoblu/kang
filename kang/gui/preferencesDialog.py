from PySide2.QtWidgets import QDialog, QDialogButtonBox, QGridLayout, \
                              QVBoxLayout, QLabel, QSpinBox, QCheckBox, QHBoxLayout

from kang.images import getIcon
from kang.modules.preferences import Preferences

tr = lambda msg: msg


class PreferencesDialog(QDialog):

    def __init__(self, parent, preferences):
        QDialog.__init__(self, parent)

        self.setWindowIcon(getIcon('kang-icon'))
        self.setWindowTitle(tr("Preferences"))
        self.resize(440, 0)  # Height will be recalculated
        self.setModal(True)

        gridLayout = QGridLayout()

        label = QLabel(tr("Recent Files:"))
        gridLayout.addWidget(label, 0, 0, 1, 1)

        self.recentFilesSpinBox = QSpinBox()
        self.recentFilesSpinBox.setMinimum(0)
        self.recentFilesSpinBox.setMaximum(10)
        gridLayout.addWidget(self.recentFilesSpinBox, 0, 1, 1, 1)

        label = QLabel(tr("Check for changes to save:"))
        gridLayout.addWidget(label, 1, 0, 1, 1)

        self.askSaveCheckbox = QCheckBox()
        gridLayout.addWidget(self.askSaveCheckbox, 1, 1, 1, 1)

        self.askSaveOnlyForNamedProjectsCheckbox = QCheckBox(tr("Only for named projects"))
        gridLayout.addWidget(self.askSaveOnlyForNamedProjectsCheckbox, 2, 1, 1, 4)

        # Parent - child relationship
        self.askSaveCheckbox.toggled.connect(self.askSaveOnlyForNamedProjectsCheckbox.setEnabled)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        buttonBox.rejected.connect(self.close)
        buttonBox.accepted.connect(self.accept)

        hLayout = QHBoxLayout()
        hLayout.addLayout(gridLayout)
        hLayout.addStretch()

        vLayout = QVBoxLayout(self)
        vLayout.addLayout(hLayout)
        vLayout.addWidget(QLabel(' '))
        vLayout.addStretch()
        vLayout.addWidget(buttonBox)

        self.recentFilesSpinBox.setValue(preferences.recentFilesNum)
        self.askSaveCheckbox.setChecked(preferences.askSave)
        self.askSaveOnlyForNamedProjectsCheckbox.setChecked(preferences.askSaveOnlyForNamedProjects)
        self.askSaveOnlyForNamedProjectsCheckbox.setEnabled(preferences.askSave)

    def getPreferences(self):
        self.exec()

        preferences = Preferences()
        preferences.recentFilesNum = self.recentFilesSpinBox.value()
        preferences.askSave = self.askSaveCheckbox.isChecked()
        preferences.askSaveOnlyForNamedProjects = self.askSaveOnlyForNamedProjectsCheckbox.isChecked()

        return (self.result(), preferences)
