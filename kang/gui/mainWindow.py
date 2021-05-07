from kang.gui.mainWindowUI import MainWindowUI
from kang.modules.regexprocessor import RegexProcessor


class MainWindow(MainWindowUI):

    def __init__(self):
        MainWindowUI.__init__(self)

    def _regexStatusChanged(self):
        statusValue, statusMessage = self._regexProcessor.getStatus()
        self.updateStatus(statusMessage, statusValue)

        allmatches = self._regexProcessor.getAllSpans()
        if allmatches and len(allmatches):
            self.matchNumberSpinBox.setMaximum(len(allmatches))
            self.matchNumberSpinBox.setEnabled(True)
            self.replaceNumberSpinBox.setMaximum(len(allmatches))
            self.replaceNumberSpinBox.setEnabled(True)
        else:
            self.matchNumberSpinBox.setEnabled(False)
            self.replaceNumberSpinBox.setEnabled(False)

        self._populateGroupTable()
        self._populateMatchTextbrowser()
        self._populateMatchAllTextbrowser()
        self._populateReplaceTextbrowser()
        self._populateCodeTextBrowser()
        self._populateEmbeddedFlags()

    def fileOpen(self):
        # TODO: Implement this fileOpen
        raise Exception("To be implemented")

    def fileSave(self):
        # TODO: Implement this fileSave
        raise Exception("To be implemented")

    def fileExit(self):
        # TODO: Implement this fileExit
        self.close()
        raise Exception("To be implemented")
