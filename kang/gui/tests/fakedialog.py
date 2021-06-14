from kang.gui.importURLDialog import ImportURLDialogMode
from kang.modules.preferences import Preferences


class FakeDialog():

    def __init__(self, parent, *args, **kargs):
        pass

    def show(self):
        pass

    # pylint: disable=invalid-name
    def exec_(self):
        pass

    def getURL(self):
        """Used when replace ImportURLDialog"""
        return (1, 'Some text', 'https://example.com/', ImportURLDialogMode.TEXT)

    def getPreferences(self):
        """Used when replace preferencesDialo"""
        return(1, Preferences())
