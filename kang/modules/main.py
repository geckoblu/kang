# pyuic5 mainWindowBA.ui > mainWindowBA.py

# pyrcc4 resources.qrc > modules/resources.py


import argparse
import sys
try:
    from PyQt5 import Qt, QtCore, QtWidgets
except:
    sys.stderr.write("""Could not locate the PyQt module.  Please make sure that
you have installed PyQt for the version of Python that you are running.\n""")
    sys.exit(1)

from kang.gui.mainWindow import MainWindow
from kang.modules import exceptionHandler

QT_VERS = int(QtCore.QT_VERSION_STR[0])

if QT_VERS < 5:
    sys.stderr.write("Qt versions prior to 5.0 are no longer supported\n")
    sys.exit(0)


def parseCmdline():

    #def locale(locale):
    #    if len(locale) != 2:
    #        msg = "'%s' is not a valid locale" % locale
    #        raise argparse.ArgumentTypeError(msg)
    #    return locale

    parser = argparse.ArgumentParser(description='Kang is a visual regular expression editor.')
    parser.add_argument('filename', metavar='FILENAME', nargs='?', help='load filename on startup')
    #parser.add_argument('-l', '--locale', type=locale, help='2-letter locale (eg. en)')

    return parser.parse_args()


def main():

    args = parseCmdline()

    qApp = Qt.QApplication(sys.argv)

# TODO: Re-enable locale
#     if args.locale not in (None, 'en'):
#         localefile = "kang_%s.qm" % (args.locale or QtCore.QTextCodec.locale())
#         localepath = findFile("translations", localefile)
#
#         if localepath:
#             translator = QtCore.QTranslator(qApp)
#             translator.load(localepath)
#
#             qApp.installTranslator(translator)
#         else:
#             sys.stderr.write("Locale for '%s' not found. Fallback to default.\n" % args.locale)

    # FIXME kang = MainWindow(args.filename)
    kang = MainWindow()
    exceptionHandler.init(kang)

    # kang.show()
    
    MainWindowBA = QtWidgets.QMainWindow()
    kang.setupUi(MainWindowBA)
    MainWindowBA.show()

    sys.exit(qApp.exec_())
