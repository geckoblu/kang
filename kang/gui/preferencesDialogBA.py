# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferencesDialogBA4.ui'
#
# Created: Fri Sep 19 16:06:43 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PreferencesDialogBA(object):
    def setupUi(self, PreferencesDialogBA):
        PreferencesDialogBA.setObjectName(_fromUtf8("PreferencesDialogBA"))
        PreferencesDialogBA.resize(549, 194)
        PreferencesDialogBA.setSizeGripEnabled(True)
        PreferencesDialogBA.setModal(True)
        self.gridLayout_2 = QtGui.QGridLayout(PreferencesDialogBA)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.editorFontLabel = QtGui.QLabel(PreferencesDialogBA)
        self.editorFontLabel.setObjectName(_fromUtf8("editorFontLabel"))
        self.gridLayout.addWidget(self.editorFontLabel, 0, 0, 1, 1)
        self.matchFontLabel = QtGui.QLabel(PreferencesDialogBA)
        self.matchFontLabel.setObjectName(_fromUtf8("matchFontLabel"))
        self.gridLayout.addWidget(self.matchFontLabel, 1, 0, 1, 1)
        self.recentFilesLabel = QtGui.QLabel(PreferencesDialogBA)
        self.recentFilesLabel.setObjectName(_fromUtf8("recentFilesLabel"))
        self.gridLayout.addWidget(self.recentFilesLabel, 2, 0, 1, 1)
        self.recentFilesSpinBox = QtGui.QSpinBox(PreferencesDialogBA)
        self.recentFilesSpinBox.setObjectName(_fromUtf8("recentFilesSpinBox"))
        self.gridLayout.addWidget(self.recentFilesSpinBox, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        self.editorFontButton = QtGui.QPushButton(PreferencesDialogBA)
        self.editorFontButton.setText(_fromUtf8(""))
        self.editorFontButton.setObjectName(_fromUtf8("editorFontButton"))
        self.gridLayout.addWidget(self.editorFontButton, 0, 1, 1, 2)
        self.matchFontButton = QtGui.QPushButton(PreferencesDialogBA)
        self.matchFontButton.setText(_fromUtf8(""))
        self.matchFontButton.setObjectName(_fromUtf8("matchFontButton"))
        self.gridLayout.addWidget(self.matchFontButton, 1, 1, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(PreferencesDialogBA)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 2, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)

        self.retranslateUi(PreferencesDialogBA)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), PreferencesDialogBA.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), PreferencesDialogBA.reject)
        QtCore.QObject.connect(self.editorFontButton, QtCore.SIGNAL(_fromUtf8("pressed()")), PreferencesDialogBA.chooseEditorFont)
        QtCore.QObject.connect(self.matchFontButton, QtCore.SIGNAL(_fromUtf8("pressed()")), PreferencesDialogBA.chooseMatchFont)
        QtCore.QMetaObject.connectSlotsByName(PreferencesDialogBA)

    def retranslateUi(self, PreferencesDialogBA):
        PreferencesDialogBA.setWindowTitle(_translate("PreferencesDialogBA", "Dialog", None))
        self.editorFontLabel.setText(_translate("PreferencesDialogBA", "Editor Font:", None))
        self.matchFontLabel.setText(_translate("PreferencesDialogBA", "Match Font:", None))
        self.recentFilesLabel.setText(_translate("PreferencesDialogBA", "Recent Files:", None))


class PreferencesDialogBA(QtGui.QDialog, Ui_PreferencesDialogBA):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QDialog.__init__(self, parent, f)

        self.setupUi(self)

