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
        d, _ = os.path.split(__file__)
        d = os.path.join(d, 'data')

        log.info('installing mime type')
        mimetype_filename = os.path.join(d, 'kang-mimetype.xml')
        subprocess.call(['xdg-mime', 'install', mimetype_filename])

        log.info('installing file icon')
        mimeicon_filename = os.path.join(d, 'application-x-kang.png')
        subprocess.call(['xdg-icon-resource', 'install', '--size', '48', mimeicon_filename])


if __name__ == '__main__':
    import setup
    setup.setup()
