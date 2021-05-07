from PySide2.QtGui import QWidget

from kang.gui.tests.fakestatusbar import FakeStatusBar


class FakeParent(QWidget):

#     def __init__(self, *args, **kwargs):
#         super(FakeParent, self).__init__(*args, **kwargs)
#         self.statusBar = FakeStatusBar()

    def statusBar(self):
        return FakeStatusBar()
