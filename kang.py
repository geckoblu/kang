#!/usr/bin/env python
#  kang.py: -*- Python -*-  DESCRIPTIVE TEXT.

# pyuic4 -w mainWindowBA4.ui > mainWindowBA.py

# pyrcc4 resources.qrc > modules/resources.py

from distutils.sysconfig import get_python_lib
import getopt
import os
import sys

from gui.mainWindow import MainWindow
from modules import exceptionHandler
from modules.util import findFile


try:
    from PyQt4 import QtCore
    from PyQt4 import QtGui
except:
    print """Could not locate the PyQt module.  Please make sure that
you have installed PyQt for the version of Python that you are running."""
    sys.exit(1)
    
### make sure that this script can find kang specific modules ###
sys.path.insert(0, os.path.join(get_python_lib(), "kang")) 

###################################################################







##############################################################################
#
#
##############################################################################

def usage():
    print "kang.py [-f filename | --file=filename ] [ -k kang_dir ]"
    print
    print "  -f filename | --filename=filename  : Load filename on startup"
    print "  -k kang_dir                       : Path containing Kang images & help subdirs"
    print "  -l locale | --locale=locale        : 2-letter locale (eg. en)"
    print
    sys.exit(0)

def main():
    filename  = None
    kang_dir = os.path.join(sys.prefix, "kang")
    locale    = None

    args = sys.argv[1:]
    try:
        (opts, getopts) = getopt.getopt(args, 'd:f:k:l:?h',
                                        ["file=",
                                         "help", "locale="])
    except:
        print "\nInvalid command line option detected."
        usage()
 
    for opt, arg in opts:
        if opt in ('-h', '-?', '--help'):
            usage()
        if opt == '-k':
            kang_dir = arg          
        if opt in ('-f', '--file'):
            filename = arg
        if opt in ('-l', '--locale'):
            locale = arg

    os.environ['KANG_DIR'] = kang_dir

    qApp = QtGui.QApplication(sys.argv)

    if locale not in (None, 'en'):
        localefile = "kang_%s.qm" % (locale or QtCore.QTextCodec.locale())
        localepath = findFile("translations", localefile)
    
        translator = QtCore.QTranslator(qApp)
        translator.load(localepath)

        qApp.installTranslator(translator)

    kang = MainWindow(filename)
    
    exceptionHandler.init(kang)
    
    kang.show()

    sys.exit(qApp.exec_())   



if __name__ == '__main__':
    main()
