#  prefs.py: -*- Python -*-  DESCRIPTIVE TEXT.

from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QDialog, QFileDialog, QFontDialog, QFont
import os
import string

from gui.preferencesDialogBA import PreferencesDialogBA
from modules.util import getConfigDirectory, getIcon


def get_font_value(s):
    if s in ('0', 'False'): return 0
    else:                   return 1

        
class PreferencesDialog(PreferencesDialogBA):
    def __init__(self, parent, autoload=0):
        PreferencesDialogBA.__init__(self, parent)
        self.parent = parent
        
        self.setWindowIcon(getIcon('kang-icon'))

        prefsFilename = "prefs"
        self.prefsPath = os.path.join(getConfigDirectory(), prefsFilename)
        if autoload: self.load()
        
    def load(self):
        try:
            fp = open(self.prefsPath, "r")
        except:
            return
        
        prefsList = fp.readlines()
        for pref in prefsList:
            preference, setting = string.split(pref, ":", 1)
            setting = string.strip(setting)
            if preference == 'Font' and setting:
                self.parseFontStr(setting, self.parent.setfont)
            if preference == 'Match Font' and setting:
                self.parseFontStr(setting, self.parent.setMatchFont)
            if preference == 'Web Browser' and setting:
                self.browserEdit.setText(setting)
            if preference == 'Email Server' and setting:
                self.emailServerEdit.setText(setting)
            if preference == 'Recent Files' and setting:
                self.recentFilesSpinBox.setValue(int(setting))
            

    def save(self):
        try:
            fp = open(self.prefsPath, "w")
        except:
            print("Could not save preferences:", self.prefsPath)
            return

        #print self.prefsPath
        f = self.parent.getfont()

        fp.write("Font: %s:%s:%s:%s:%s:%s\n" %
                 (f.family(), f.pointSize(),
                  f.bold(), f.italic(),
                  f.underline(), f.strikeOut()))

        f = self.parent.getMatchFont()
        fp.write("Match Font: %s:%s:%s:%s:%s:%s\n" %
                 (f.family(), f.pointSize(),
                  f.bold(), f.italic(),
                  f.underline(), f.strikeOut()))

        fp.write("Web Browser: %s\n" % str(self.browserEdit.text()))
        fp.write("Email Server: %s\n" % str(self.emailServerEdit.text()))
        fp.write("Recent Files: %s\n" % str(self.recentFilesSpinBox.cleanText()))
        fp.close()
        self.parent.emit(SIGNAL('prefsSaved()'))


    def parseFontStr(self, fontstr, meth):
        # parse a font in the form: family:pt size:bold:italic:underline:strikeout
        parts = string.split(fontstr, ":")
        if len(parts) != 6: return
        
        f = QFont()
        f.setFamily(parts[0])
        f.setPointSize(int(parts[1]))
        f.setBold(get_font_value(parts[2]))
        f.setItalic(get_font_value(parts[3]))
        f.setUnderline(get_font_value(parts[4]))
        f.setStrikeOut(get_font_value(parts[5]))
        meth(f)
        #self.parent.setfont(f)


    def setFontButtonText(self, button, font):
        #self.fontButton.setText("%s %s" % (str(font.family()),font.pointSize() ))
        button.setText("%s %s" % (str(font.family()),font.pointSize() ))

    def showPrefsDialog(self):
        f = self.parent.getfont()
        self.fontButton.setFont(f)
        self.setFontButtonText(self.fontButton, f)

        f = self.parent.getMatchFont()
        self.fontButtonMatch.setFont(f)
        self.setFontButtonText(self.fontButtonMatch, f)

        self.show()

    def font_slot(self):
        (font, ok) = QFontDialog.getFont(self.fontButton.font())
        if ok:
            self.fontButton.setFont(font)
            self.setFontButtonText(self.fontButton, font)

    def match_font_slot(self):
        (font, ok) = QFontDialog.getFont(self.fontButtonMatch.font())
        if ok:
            self.fontButtonMatch.setFont(font)
            self.setFontButtonText(self.fontButtonMatch, font)        

    def browser_slot(self):
        fn = QFileDialog.getOpenFileName(self, self.tr("Choose Web Browser"), self.browserEdit.text(), "All (*)")
        if not fn.isEmpty():
            self.browserEdit.setText(fn)


    def apply_slot(self):
        self.parent.setfont(self.fontButton.font())
        self.parent.setMatchFont(self.fontButtonMatch.font())
        self.save()


    def accept(self):
        self.apply_slot()
        QDialog.accept(self)


    def help_slot(self):
        self.helpWindow = help.Help(self, "prefs.html")

