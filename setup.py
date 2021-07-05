#!/usr/bin/env python3

from setuptools import setup, find_packages
import os.path
import sys

from distutils import log
import os
from setuptools import  Command
import subprocess

from kang import VERSION

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()


class integrate_desktop(Command):
    """Subcommand to integrate kang into a desktop environment"""

    description = "Integrate Kang into the desktop."

    user_options = []

    def initialize_options(self):
        """init options"""
        pass

    def finalize_options(self):
        """finalize options"""
        pass

    def run(self):
        """runner"""
        d, __ = os.path.split(__file__)
        d = os.path.join(d, 'data')
        
        # sudo xdg-desktop-menu install --novendor --mode system data/kang.desktop
        log.info('installing desktop menu')
        desktop_filename = os.path.join(d, 'kang.desktop')
        subprocess.call(['xdg-desktop-menu', 'install', '--novendor', desktop_filename])
        
        # sudo xdg-icon-resource install --mode system --size svg ./data/kang-icon.svg
        log.info('installing file icon')
        desktopicon_filename = os.path.join(d, 'kang-icon.svg')
        subprocess.call(['./xdg-icon-resource', 'install', '--size', 'scalable', desktopicon_filename])

        # sudo xdg-mime install --mode system data/kang-mimetype.xml
        log.info('installing mime type')
        mimetype_filename = os.path.join(d, 'kang-mimetype.xml')
        subprocess.call(['xdg-mime', 'install', mimetype_filename])

        # sudo xdg-icon-resource install --mode system --size 48 application-x-kang.png
        log.info('installing mime file icon')
        mimeicon_filename = os.path.join(d, 'application-x-kang.png')
        subprocess.call(['xdg-icon-resource', 'install', '--size', '48', mimeicon_filename])
        
        # sudo xdg-mime default kang.desktop application/x-kang
        log.info('link mime type to Kang')
        subprocess.call(['xdg-mime', 'default', 'kang.desktop', 'application/x-kang'])

cmdclass = {}
cmdclass['integrate_desktop'] = integrate_desktop
        
setup(
    name='kang',
    version=VERSION,
    url='https://github.com/geckoblu/kang',
    author='Alessio Piccoli',
    author_email='alepic@geckoblu.net',
    description="The Python Regular Expression Editor",
    long_description=README,
    long_description_content_type="text/markdown",
    license="GPL v2",
    
    scripts=['bin/kang'],
    packages=find_packages(exclude=['test', 'tests']),
    package_data={'': ['*.svg'] },
    data_files=[
        ('share/pixmaps', ['kang/images/kang-icon.svg']),
        ('share/applications', ['data/kang.desktop'])
    ],
    zip_safe=False,
    cmdclass=cmdclass,    
)
