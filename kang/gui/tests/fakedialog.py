from kang.gui.importURLDialog import ImportURLDialogMode
from kang.modules.preferences import Preferences


class FakeDialog():

    def __init__(self, parent, *args, **kargs):
        pass

    def show(self):
        pass

    def exec_(self):
        pass

    """Used when replace ImportURLDialog"""
    def getURL(self):
        return (1, 'Some text', 'https://example.com/', ImportURLDialogMode.TEXT)

    """Used when replace preferencesDialo"""
    def getPreferences(self):
        return(1, Preferences())
