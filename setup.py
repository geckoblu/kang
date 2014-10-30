#!/usr/bin/env python

from setuptools import setup, find_packages

from kang import VERSION

setup(
    name = 'kang',
    version = VERSION,
    scripts = ['bin/kang'],
    packages = find_packages(exclude=['test', 'tests']),
    package_data = {'': ['*.svg']},
    #data_files = [
    #    ('images', glob('images/kang-icon.svg'))
    #],
    zip_safe = False
)