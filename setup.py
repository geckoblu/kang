#!/usr/bin/env python

import sys
try:
    from PyQt4 import QtCore
except:
    sys.stderr.write("""Could not locate the PyQt module.  Please make sure that
you have installed PyQt for the version of Python that you are running.\n""")
    sys.exit(1)

QT_VERS = int(QtCore.QT_VERSION_STR[0])

if QT_VERS < 4:
    sys.stderr.write("Qt versions prior to 4.0 are no longer supported\n")
    sys.exit(0)

from setuptools import setup, find_packages

from kang import VERSION

setup(
    name='kang',
    version=VERSION,
    scripts=['bin/kang'],
    packages=find_packages(exclude=['test', 'tests']),
    package_data={'': ['*.svg', '*.xml'],
                    'kang': ['doc/*.*', 'doc/_images/*.*', 'doc/_static/*.*']
                  },
    data_files=[
        ('share/pixmaps', ['kang/images/kang-icon.svg']),
        ('share/applications', ['data/kang.desktop'])
    ],
    zip_safe=False,
)
