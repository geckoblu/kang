# pyuic4 -w mainWindowBA4.ui > mainWindowBA.py

# pyrcc4 resources.qrc > modules/resources.py


from PyQt4 import QtGui
import argparse
import sys

from kang.gui.mainWindow import MainWindow
from kang.modules import exceptionHandler


def parse_cmdline():

    def locale(locale):
        if len(locale) != 2:
            msg = "'%s' is not a valid locale" % locale
            raise argparse.ArgumentTypeError(msg)
        return locale

    parser = argparse.ArgumentParser(description='Kang is a graphical regular expression tester.')
    parser.add_argument('filename', metavar='FILENAME', nargs='?', help='load filename on startup')
    #parser.add_argument('-l', '--locale', type=locale, help='2-letter locale (eg. en)')

    return parser.parse_args()


def main():

    args = parse_cmdline()

    qApp = QtGui.QApplication(sys.argv)

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

    kang = MainWindow(args.filename)

    exceptionHandler.init(kang)

    kang.show()

    sys.exit(qApp.exec_())
