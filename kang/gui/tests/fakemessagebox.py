from PySide2.QtWidgets import QMessageBox


class FakeMessageBox():

    Ok = QMessageBox.Ok
    Yes = QMessageBox.Yes
    No = QMessageBox.No

    def __init__(self, *args, **kwargs):
        super(FakeMessageBox, self).__init__(*args, **kwargs)

    @staticmethod
    def information(parent, title, text, *args, **kargs):
        pass

    @staticmethod
    def critical(parent, title, text, *args, **kargs):
        pass

    @staticmethod
    def warning(parent, title, text, *args, **kargs):
        pass
