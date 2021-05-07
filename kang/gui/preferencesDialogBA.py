# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kang/gui/preferencesDialogBA.ui'
#
# Created: Fri May  8 11:44:47 2015
#      by: PySide2 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# try:
    # _fromUtf8 = QString.fromUtf8
# except AttributeError:


def _fromUtf8(s):
    return s


try:
    _encoding = QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)

except AttributeError:

    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)


class Ui_PreferencesDialogBA(object):

    def setupUi(self, PreferencesDialogBA):
        PreferencesDialogBA.setObjectName(_fromUtf8("PreferencesDialogBA"))
        PreferencesDialogBA.resize(549, 214)
        PreferencesDialogBA.setSizeGripEnabled(True)
        PreferencesDialogBA.setModal(True)
        self.gridLayout_2 = QGridLayout(PreferencesDialogBA)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.recentFilesLabel = QLabel(PreferencesDialogBA)
        self.recentFilesLabel.setObjectName(_fromUtf8("recentFilesLabel"))
        self.gridLayout.addWidget(self.recentFilesLabel, 0, 0, 1, 1)
        self.recentFilesSpinBox = QSpinBox(PreferencesDialogBA)
        self.recentFilesSpinBox.setObjectName(_fromUtf8("recentFilesSpinBox"))
        self.gridLayout.addWidget(self.recentFilesSpinBox, 0, 1, 1, 1)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.foolLabel = QLabel(PreferencesDialogBA)
        self.foolLabel.setObjectName(_fromUtf8("foolLabel"))
        self.gridLayout.addWidget(self.foolLabel, 1, 0, 1, 1)
        self.askSaveLabel = QLabel(PreferencesDialogBA)
        self.askSaveLabel.setObjectName(_fromUtf8("askSaveLabel"))
        self.gridLayout.addWidget(self.askSaveLabel, 2, 0, 1, 1)
        self.askSaveCheckbox = QCheckBox(PreferencesDialogBA)
        self.askSaveCheckbox.setText(_fromUtf8(""))
        self.askSaveCheckbox.setObjectName(_fromUtf8("askSaveCheckbox"))
        self.gridLayout.addWidget(self.askSaveCheckbox, 2, 1, 1, 1)
        self.askSaveCheckbox2 = QCheckBox(PreferencesDialogBA)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.askSaveCheckbox2.sizePolicy().hasHeightForWidth())
        self.askSaveCheckbox2.setSizePolicy(sizePolicy)
        self.askSaveCheckbox2.setObjectName(_fromUtf8("askSaveCheckbox2"))
        self.gridLayout.addWidget(self.askSaveCheckbox2, 3, 1, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.buttonBox = QDialogButtonBox(PreferencesDialogBA)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 2, 0, 1, 1)
        spacerItem1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)

        self.retranslateUi(PreferencesDialogBA)
        QObject.connect(self.buttonBox, SIGNAL(_fromUtf8("accepted()")), PreferencesDialogBA.accept)
        QObject.connect(self.buttonBox, SIGNAL(_fromUtf8("rejected()")), PreferencesDialogBA.reject)
        QObject.connect(self.askSaveCheckbox, SIGNAL(_fromUtf8("toggled(bool)")), PreferencesDialogBA.askSaveCheckboxToogled)
        QMetaObject.connectSlotsByName(PreferencesDialogBA)

    def retranslateUi(self, PreferencesDialogBA):
        PreferencesDialogBA.setWindowTitle(_translate("PreferencesDialogBA", "Preferences", None))
        self.recentFilesLabel.setText(_translate("PreferencesDialogBA", "Recent Files:", None))
        self.foolLabel.setText(_translate("PreferencesDialogBA", " ", None))
        self.askSaveLabel.setText(_translate("PreferencesDialogBA", "Check for changes to save", None))
        self.askSaveCheckbox2.setText(_translate("PreferencesDialogBA", "Only for named projects", None))


class PreferencesDialogBA(QDialog, Ui_PreferencesDialogBA):

    def __init__(self, parent=None, f=Qt.WindowFlags()):
        QDialog.__init__(self, parent, f)

        self.setupUi(self)

