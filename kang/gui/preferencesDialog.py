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

        self._recentFilesSpinBox = QSpinBox()
        self._recentFilesSpinBox.setMinimum(0)
        self._recentFilesSpinBox.setMaximum(10)
        gridLayout.addWidget(self._recentFilesSpinBox, 0, 1, 1, 1)

        label = QLabel(tr("Check for changes to save:"))
        gridLayout.addWidget(label, 1, 0, 1, 1)

        self._askSaveCheckbox = QCheckBox()
        gridLayout.addWidget(self._askSaveCheckbox, 1, 1, 1, 1)

        self._askSaveOnlyForNamedProjectsCheckbox = QCheckBox(tr("Only for named projects"))
        gridLayout.addWidget(self._askSaveOnlyForNamedProjectsCheckbox, 2, 1, 1, 4)

        # Parent - child relationship
        self._askSaveCheckbox.toggled.connect(self._askSaveOnlyForNamedProjectsCheckbox.setEnabled)

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

        self._recentFilesSpinBox.setValue(preferences.recentFilesNum)
        self._askSaveCheckbox.setChecked(preferences.askSave)
        self._askSaveOnlyForNamedProjectsCheckbox.setChecked(preferences.askSaveOnlyForNamedProjects)
        self._askSaveOnlyForNamedProjectsCheckbox.setEnabled(preferences.askSave)

    def getPreferences(self):
        self.exec()

        preferences = Preferences()
        preferences.recentFilesNum = self._recentFilesSpinBox.value()
        preferences.askSave = self._askSaveCheckbox.isChecked()
        preferences.askSaveOnlyForNamedProjects = self._askSaveOnlyForNamedProjectsCheckbox.isChecked()

        return (self.result(), preferences)
