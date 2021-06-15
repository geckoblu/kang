# pylint: disable=missing-function-docstring

from PySide2.QtWidgets import QMessageBox

_ANSWER = QMessageBox.No

# pylint: disable=unused-argument
class FakeMessageBox():

    Ok = QMessageBox.Ok
    Yes = QMessageBox.Yes
    No = QMessageBox.No

    @staticmethod
    def information(parent, title, text, *args, **kargs):
        return _ANSWER

    @staticmethod
    def critical(parent, title, text, *args, **kargs):
        return _ANSWER

    @staticmethod
    def warning(parent, title, text, *args, **kargs):
        return _ANSWER
