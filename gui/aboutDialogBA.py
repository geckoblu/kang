# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/aboutDialogBA4.ui'
#
# Created: Tue Aug 26 15:14:55 2014
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

class Ui_AboutDialogBA(object):
    def setupUi(self, AboutDialogBA):
        AboutDialogBA.setObjectName(_fromUtf8("AboutDialogBA"))
        AboutDialogBA.resize(556, 384)
        AboutDialogBA.setSizeGripEnabled(True)
        AboutDialogBA.setModal(True)
        self.gridLayout = QtGui.QGridLayout(AboutDialogBA)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout1 = QtGui.QGridLayout()
        self.gridLayout1.setObjectName(_fromUtf8("gridLayout1"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelIcon = QtGui.QLabel(AboutDialogBA)
        self.labelIcon.setText(_fromUtf8(""))
        self.labelIcon.setObjectName(_fromUtf8("labelIcon"))
        self.horizontalLayout.addWidget(self.labelIcon)
        self.verticalLayout1 = QtGui.QVBoxLayout()
        self.verticalLayout1.setObjectName(_fromUtf8("verticalLayout1"))
        self.label_kang = QtGui.QLabel(AboutDialogBA)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 133, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_kang.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(24)
        self.label_kang.setFont(font)
        self.label_kang.setObjectName(_fromUtf8("label_kang"))
        self.verticalLayout1.addWidget(self.label_kang)
        self.label_outline = QtGui.QLabel(AboutDialogBA)
        self.label_outline.setObjectName(_fromUtf8("label_outline"))
        self.verticalLayout1.addWidget(self.label_outline)
        self.horizontalLayout.addLayout(self.verticalLayout1)
        self.label_fool1 = QtGui.QLabel(AboutDialogBA)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_fool1.sizePolicy().hasHeightForWidth())
        self.label_fool1.setSizePolicy(sizePolicy)
        self.label_fool1.setText(_fromUtf8(""))
        self.label_fool1.setObjectName(_fromUtf8("label_fool1"))
        self.horizontalLayout.addWidget(self.label_fool1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget = QtGui.QTabWidget(AboutDialogBA)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.gridLayout2 = QtGui.QGridLayout(self.tab_1)
        self.gridLayout2.setObjectName(_fromUtf8("gridLayout2"))
        self.label_fool4 = QtGui.QLabel(self.tab_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_fool4.sizePolicy().hasHeightForWidth())
        self.label_fool4.setSizePolicy(sizePolicy)
        self.label_fool4.setText(_fromUtf8(""))
        self.label_fool4.setObjectName(_fromUtf8("label_fool4"))
        self.gridLayout2.addWidget(self.label_fool4, 8, 2, 1, 1)
        self.label_fool5 = QtGui.QLabel(self.tab_1)
        self.label_fool5.setText(_fromUtf8(""))
        self.label_fool5.setObjectName(_fromUtf8("label_fool5"))
        self.gridLayout2.addWidget(self.label_fool5, 2, 0, 1, 1)
        self.label_licensetxt = QtGui.QLabel(self.tab_1)
        self.label_licensetxt.setObjectName(_fromUtf8("label_licensetxt"))
        self.gridLayout2.addWidget(self.label_licensetxt, 4, 1, 1, 1)
        self.label_license = QtGui.QLabel(self.tab_1)
        self.label_license.setObjectName(_fromUtf8("label_license"))
        self.gridLayout2.addWidget(self.label_license, 4, 0, 1, 1)
        self.label_homepage = QtGui.QLabel(self.tab_1)
        self.label_homepage.setObjectName(_fromUtf8("label_homepage"))
        self.gridLayout2.addWidget(self.label_homepage, 3, 0, 1, 1)
        self.label_version = QtGui.QLabel(self.tab_1)
        self.label_version.setObjectName(_fromUtf8("label_version"))
        self.gridLayout2.addWidget(self.label_version, 1, 0, 1, 1)
        self.label_versiontxt = QtGui.QLabel(self.tab_1)
        self.label_versiontxt.setObjectName(_fromUtf8("label_versiontxt"))
        self.gridLayout2.addWidget(self.label_versiontxt, 1, 1, 1, 1)
        self.label_fool3 = QtGui.QLabel(self.tab_1)
        self.label_fool3.setText(_fromUtf8(""))
        self.label_fool3.setObjectName(_fromUtf8("label_fool3"))
        self.gridLayout2.addWidget(self.label_fool3, 8, 1, 1, 1)
        self.label_homepagetxt = QtGui.QLabel(self.tab_1)
        self.label_homepagetxt.setObjectName(_fromUtf8("label_homepagetxt"))
        self.gridLayout2.addWidget(self.label_homepagetxt, 3, 1, 1, 1)
        self.label_fool6 = QtGui.QLabel(self.tab_1)
        self.label_fool6.setText(_fromUtf8(""))
        self.label_fool6.setObjectName(_fromUtf8("label_fool6"))
        self.gridLayout2.addWidget(self.label_fool6, 2, 1, 1, 1)
        self.label_fool2 = QtGui.QLabel(self.tab_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_fool2.sizePolicy().hasHeightForWidth())
        self.label_fool2.setSizePolicy(sizePolicy)
        self.label_fool2.setText(_fromUtf8(""))
        self.label_fool2.setObjectName(_fromUtf8("label_fool2"))
        self.gridLayout2.addWidget(self.label_fool2, 8, 0, 1, 1)
        self.label_fool7 = QtGui.QLabel(self.tab_1)
        self.label_fool7.setText(_fromUtf8(""))
        self.label_fool7.setObjectName(_fromUtf8("label_fool7"))
        self.gridLayout2.addWidget(self.label_fool7, 0, 0, 1, 1)
        self.label_fool8 = QtGui.QLabel(self.tab_1)
        self.label_fool8.setText(_fromUtf8(""))
        self.label_fool8.setObjectName(_fromUtf8("label_fool8"))
        self.gridLayout2.addWidget(self.label_fool8, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout3 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout3.setObjectName(_fromUtf8("gridLayout3"))
        self.textAuthors = QtGui.QTextBrowser(self.tab_2)
        self.textAuthors.setReadOnly(True)
        self.textAuthors.setOpenExternalLinks(True)
        self.textAuthors.setOpenLinks(True)
        self.textAuthors.setObjectName(_fromUtf8("textAuthors"))
        self.gridLayout3.addWidget(self.textAuthors, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.gridLayout1.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout1, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(AboutDialogBA)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(AboutDialogBA)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AboutDialogBA.close)
        QtCore.QMetaObject.connectSlotsByName(AboutDialogBA)

    def retranslateUi(self, AboutDialogBA):
        AboutDialogBA.setWindowTitle(_translate("AboutDialogBA", "About", None))
        self.label_kang.setText(_translate("AboutDialogBA", "KANG", None))
        self.label_outline.setText(_translate("AboutDialogBA", "The Python Regex Tester", None))
        self.label_licensetxt.setText(_translate("AboutDialogBA", "TextLabel", None))
        self.label_license.setText(_translate("AboutDialogBA", "License:", None))
        self.label_homepage.setText(_translate("AboutDialogBA", "Homepage:", None))
        self.label_version.setText(_translate("AboutDialogBA", "Version:", None))
        self.label_versiontxt.setText(_translate("AboutDialogBA", "TextLabel", None))
        self.label_homepagetxt.setText(_translate("AboutDialogBA", "TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("AboutDialogBA", "General", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("AboutDialogBA", "Authors", None))


class AboutDialogBA(QtGui.QDialog, Ui_AboutDialogBA):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QDialog.__init__(self, parent, f)

        self.setupUi(self)
