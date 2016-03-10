#!/usr/bin/env python

from setuptools import setup, find_packages
from codecs import open
from os import path
import sys

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()
with open(path.join(here, 'csgo/__init__.py'), encoding='utf-8') as f:
    __version__ = f.readline().split('"')[1]

install_requires = [
    'steam>=0.6.5',
    'gevent-eventemitter>=1.2',
    'gevent>=1.1rc3',
    'protobuf>=2.6.1',
]

if sys.version_info < (3, 4):
    install_requires.append('enum34>=1.0.4')

setup(
    name='csgo',
    version=__version__,
    description='Module for interacting CSGO\'s Game Coordinator',
    long_description=long_description,
    url='https://github.com/ValvePython/csgo',
    author="Rossen Georgiev",
    author_email='rossen@rgp.io',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: English',
        'Operating System :: OS Independent',
    ],
    keywords='valve steam steamid api webapi csgo global offensive',
    packages=['csgo'] + ['csgo.'+x for x in find_packages(where='csgo')],
    install_requires=install_requires,
    zip_safe=True,
)
