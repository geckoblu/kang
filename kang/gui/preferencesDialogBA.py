# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferencesDialogBA.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PreferencesDialogBA(object):
    def setupUi(self, PreferencesDialogBA):
        PreferencesDialogBA.setObjectName("PreferencesDialogBA")
        PreferencesDialogBA.resize(549, 214)
        PreferencesDialogBA.setSizeGripEnabled(True)
        PreferencesDialogBA.setModal(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(PreferencesDialogBA)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.recentFilesLabel = QtWidgets.QLabel(PreferencesDialogBA)
        self.recentFilesLabel.setObjectName("recentFilesLabel")
        self.gridLayout.addWidget(self.recentFilesLabel, 0, 0, 1, 1)
        self.recentFilesSpinBox = QtWidgets.QSpinBox(PreferencesDialogBA)
        self.recentFilesSpinBox.setObjectName("recentFilesSpinBox")
        self.gridLayout.addWidget(self.recentFilesSpinBox, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.foolLabel = QtWidgets.QLabel(PreferencesDialogBA)
        self.foolLabel.setObjectName("foolLabel")
        self.gridLayout.addWidget(self.foolLabel, 1, 0, 1, 1)
        self.askSaveLabel = QtWidgets.QLabel(PreferencesDialogBA)
        self.askSaveLabel.setObjectName("askSaveLabel")
        self.gridLayout.addWidget(self.askSaveLabel, 2, 0, 1, 1)
        self.askSaveCheckbox = QtWidgets.QCheckBox(PreferencesDialogBA)
        self.askSaveCheckbox.setText("")
        self.askSaveCheckbox.setObjectName("askSaveCheckbox")
        self.gridLayout.addWidget(self.askSaveCheckbox, 2, 1, 1, 1)
        self.askSaveCheckbox2 = QtWidgets.QCheckBox(PreferencesDialogBA)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.askSaveCheckbox2.sizePolicy().hasHeightForWidth())
        self.askSaveCheckbox2.setSizePolicy(sizePolicy)
        self.askSaveCheckbox2.setObjectName("askSaveCheckbox2")
        self.gridLayout.addWidget(self.askSaveCheckbox2, 3, 1, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(PreferencesDialogBA)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)

        self.retranslateUi(PreferencesDialogBA)
        self.buttonBox.accepted.connect(PreferencesDialogBA.accept)
        self.buttonBox.rejected.connect(PreferencesDialogBA.reject)
        self.askSaveCheckbox.toggled['bool'].connect(PreferencesDialogBA.askSaveCheckboxToogled)
        QtCore.QMetaObject.connectSlotsByName(PreferencesDialogBA)

    def retranslateUi(self, PreferencesDialogBA):
        _translate = QtCore.QCoreApplication.translate
        PreferencesDialogBA.setWindowTitle(_translate("PreferencesDialogBA", "Preferences"))
        self.recentFilesLabel.setText(_translate("PreferencesDialogBA", "Recent Files:"))
        self.foolLabel.setText(_translate("PreferencesDialogBA", " "))
        self.askSaveLabel.setText(_translate("PreferencesDialogBA", "Check for changes to save"))
        self.askSaveCheckbox2.setText(_translate("PreferencesDialogBA", "Only for named projects"))
