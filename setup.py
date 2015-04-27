#!/usr/bin/env python

from setuptools import setup, find_packages

from kang import VERSION

setup(
    name = 'kang',
    version = VERSION,
    scripts = ['bin/kang'],
    packages = find_packages(exclude=['test', 'tests']),
    package_data = {'': ['*.svg', '*.xml'],
                    'kang': ['doc/*.*', 'doc/_images/*.*', 'doc/_static/*.*']
                    },
    data_files = [
        ('share/pixmaps', ['kang/images/kang-icon.svg']),
        ('share/applications', ['data/kang.desktop'])
    ],
    zip_safe = False
)
