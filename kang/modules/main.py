import argparse
import sys
try:
    from PySide2.QtWidgets import QApplication
except ImportError:
    sys.stderr.write("""Could not locate the PySide2 module.  Please make sure that
you have installed PySide2 for the version of Python that you are running.\n""")
    sys.exit(1)

from kang.gui.mainWindow import MainWindow
from kang.modules import exceptionHandler


def _parseCmdline():

    # def locale(locale):
    #    if len(locale) != 2:
    #        msg = "'%s' is not a valid locale" % locale
    #        raise argparse.ArgumentTypeError(msg)
    #    return locale

    parser = argparse.ArgumentParser(description='Kang is a visual regular expression editor.')
    parser.add_argument('filename', metavar='FILENAME', nargs='?', help='load _filename on startup')
    # parser.add_argument('-l', '--locale', type=locale, help='2-letter locale (eg. en)')

    return parser.parse_args()


def main():
    """Main function"""

    args = _parseCmdline()

    qApp = QApplication(sys.argv)

# TODO: Re-enable locale
#     if args.locale not in (None, 'en'):
#         localefile = "kang_%s.qm" % (args.locale or QTextCodec.locale())
#         localepath = findFile("translations", localefile)
#
#         if localepath:
#             translator = QTranslator(qApp)
#             translator.load(localepath)
#
#             qApp.installTranslator(translator)
#         else:
#             sys.stderr.write("Locale for '%s' not found. Fallback to default.\n" % args.locale)

    kang = MainWindow()

    exceptionHandler.init(kang)

    if args.filename:
        kang.loadFile(args.filename)

    kang.show()

    sys.exit(qApp.exec_())
