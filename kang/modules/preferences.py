from PyQt4.Qt import QFont
import os
import string
import sys

from kang.modules.util import getConfigDirectory


def _get_font_value(s):
    if s in ('0', 'False'): return 0
    else:                   return 1

class Preferences:
    
    def __init__(self, defaultEditorFont, defaultMatchFont):
        prefsFilename = "prefs"
        self.prefsPath = os.path.join(getConfigDirectory(), prefsFilename)
        
        self.defaultRecentFilesNum = 5
        self.defaultEditorFont = defaultEditorFont
        self.defaultEditorFontStr = self.fontToString(self.defaultEditorFont)
        self.defaultMatchFont = defaultMatchFont
        self.defaultMatchFontStr = self.fontToString(self.defaultMatchFont)
        
        self.recentFilesNum = self.defaultRecentFilesNum
        self.editorFont = self.defaultEditorFont
        self.matchFont = self.defaultMatchFont
        
        self.load()
    
    
    def load(self):
        try:
            fp = open(self.prefsPath, "r")
        except:
            return
        
        prefsList = fp.readlines()
        for pref in prefsList:
            if ':' in pref:
                preference, setting = string.split(pref, ":", 1)
                setting = string.strip(setting)
                if preference == 'Editor Font' and setting:
                    self.editorFont = self.parseFontStr(setting)
                if preference == 'Match Font' and setting:
                    self.matchFont = self.parseFontStr(setting)
                if preference == 'Recent Files' and setting:
                    self.recentFilesNum = int(setting)
                
                
    def save(self):
        try:
            fp = open(self.prefsPath, "w")
        except:
            sys.stderr.write("Could not save preferences: %s\n" & self.prefsPath)
            return

        # Recent Files
        if self.recentFilesNum != self.defaultRecentFilesNum:
            fp.write("Recent Files: %s\n" % str(self.recentFilesNum))
        
        # Editor Font
        if self.editorFont:
            fstr = self.fontToString(self.editorFont)
            if fstr != self.defaultEditorFontStr:
                fp.write("Editor Font: %s\n" % fstr)
            
        # March Font
        if self.matchFont:
            fstr = self.fontToString(self.matchFont)
            if fstr != self.defaultMatchFontStr:
                fp.write("Match Font: %s\n" % fstr)

        fp.close()
        
        
    def parseFontStr(self, fontstr):
        # parse a font in the form: family:pt size:bold:italic:underline:strikeout
        parts = string.split(fontstr, ":")
        if len(parts) != 6: return
        
        f = QFont()
        f.setFamily(parts[0])
        f.setPointSize(int(parts[1]))
        f.setBold(_get_font_value(parts[2]))
        f.setItalic(_get_font_value(parts[3]))
        f.setUnderline(_get_font_value(parts[4]))
        f.setStrikeOut(_get_font_value(parts[5]))
        
        return f
    
    def fontToString(self, f):
        return ("%s:%s:%s:%s:%s:%s" % \
                     (f.family(), f.pointSize(),
                      f.bold(), f.italic(),
                      f.underline(), f.strikeOut()))
