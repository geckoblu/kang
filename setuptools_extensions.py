from distutils import log
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
        d, __ = os.path.split(__file__)
        d = os.path.join(d, 'data')

        # sudo xdg-mime install --mode system data/kang-mimetype.xml
        log.info('installing mime type')
        mimetype_filename = os.path.join(d, 'kang-mimetype.xml')
        subprocess.call(['xdg-mime', 'install', mimetype_filename])

        # sudo xdg-icon-resource install --mode system --size 48 application-x-kang.png
        log.info('installing file icon')
        mimeicon_filename = os.path.join(d, 'application-x-kang.png')
        subprocess.call(['xdg-icon-resource', 'install', '--size', '48', mimeicon_filename])
        
        # sudo xdg-mime default kang.desktop application/x-kang
        log.info('link mime type to kang')
        subprocess.call(['xdg-mime', 'default', 'kang.desktop', 'application/x-kang'])


if __name__ == '__main__':
    import setup
    setup.setup()
