import os
from setuptools import  Command
import subprocess


class integrate_desktop(Command):
    """Subcommand to integrate kang into a desktop environment"""

    description = "Integrate kang into the desktop."

    user_options = []

    def initialize_options(self):
        """init options"""
        pass

    def finalize_options(self):
        """finalize options"""
        pass

    def run(self):
        """runner"""
        print('installing mime type')
        subprocess.call(['xdg-mime', 'install', './data/kang-mimetype.xml'])

        print('installing file icon')
        subprocess.call(['xdg-icon-resource', 'install', '--size', '48', './data/application-x-kang.png'])
