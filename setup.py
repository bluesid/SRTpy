#!/usr/bin/env python

"""
    SRTpy -- SRT (https://etk.srail.co.kr) wrapper for Python.
    ==========================================================

    : copyright: (c) 2017 by Heena Kwag.
    : URL: <http://github.com/dotaitch/SRTpy>
    : license: BSD, see LICENSE for more details.
"""

import os
from distutils.core import setup

version = license = author = email = url = None
with open(os.path.join('SRTpy', '__init__.py'), encoding='utf-8') as f:
    for line in f:
        if line.strip().startswith('__version__'):
            version = line.split('=')[1].strip().replace('"', '').replace("'", '')
        elif line.strip().startswith('__license__'):
            license = line.split('=')[1].strip().replace('"', '').replace("'", '')
        elif line.strip().startswith('__author__'):
            author = line.split('=')[1].strip().replace('"', '').replace("'", '')
        elif line.strip().startswith('__author_email__'):
            email = line.split('=')[1].strip().replace('"', '').replace("'", '')
        elif line.strip().startswith('__url__'):
            url = line.split('=')[1].strip().replace('"', '').replace("'", '')
        elif None not in (version, license, author, email, url):
            break

setup(
    name='SRTpy',
    packages=['SRTpy'],
    version=version,
    description='SRT (https://etk.srail.co.kr) wrapper for Python',
    license=license,
    author=author,
    author_email=email,
    url=url,
    keywords=['SRT', 'srt', 'SRTpy', 'srtpy'],
    package_data={'assets': ['*.xml']},
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'requests',
    ],
)
