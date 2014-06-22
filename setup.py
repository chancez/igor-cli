#!/usr/bin/env python

try:
    from setuptools import setup
except:
    from distutils.core import setup

dependencies = ['docopt', 'termcolor']

setup(
        name='igor',
        version='0.0.1',
        description='The Igor CLI',
        url='https://github.com/emaadmanzoor/igor-cli',
        author='Emaad Ahmed Manzoor',
        author_email='emaadmanzoor@gmail.com',
        install_requires=dependencies,
        packages=['cli'],
        entry_points={
            'console_scripts': [
                'igor=cli.main:start'
            ]
        }
)
