#!/usr/bin/env python3

from setuptools import setup, find_packages
import sys

from kang import VERSION

try:
    import PySide2
except ImportError:
    sys.stderr.write("""Could not locate the PySide2 module.  Please make sure that
you have installed PySide2 for the version of Python that you are running.\n""")
    sys.exit(1)

cmdclass = {}
try:
    from setuptools_extensions import integrate_desktop
    cmdclass['integrate_desktop'] = integrate_desktop
except ImportError:
    pass


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
    cmdclass=cmdclass,

    url='http://www.geckoblu.net/kang',
    author='Alessio Piccoli',
    author_email='alepic@geckoblu.net'
)
