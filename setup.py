# -*- coding: utf-8 -*-
"""Installer for Searx package."""

import os
import sys

from setuptools import find_packages, setup


version_ns = {}
with open(os.path.join('searx', 'version.py')) as f:
    exec(f.read(), version_ns)
VERSION_STRING = version_ns.get('VERSION_STRING', '')

brand = {}
with open(os.path.join('utils', 'brand.env')) as f:
    for line in f:
        line = line.strip()

        if not line or line.startswith('#'):
            continue

        if line.startswith('export '):
            line = line[len('export '):]

        if '=' in line:
            key, val = line.split('=', 1)
            key = key.strip()
            val = val.strip().strip("'").strip('"')
            brand[key] = val

with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = [ l.strip() for l in f.readlines()]

with open('requirements-dev.txt') as f:
    dev_requirements = [ l.strip() for l in f.readlines()]

setup(
    name='searx',
    version=VERSION_STRING,
    description="A privacy-respecting, hackable metasearch engine",
    long_description=long_description,
    url=brand.get("DOCS_URL", ""),
    project_urls={
        "Code": brand.get("GIT_URL", ""),
        "Issue tracker": brand.get("ISSUE_URL", ""),
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        'License :: OSI Approved :: GNU Affero General Public License v3'
    ],
    keywords='metasearch searchengine search web http',
    author='Adam Tauber',
    author_email='asciimoo@gmail.com',
    license='GNU Affero General Public License',
    packages=find_packages(exclude=["tests*", "searx_extra"]),
    zip_safe=False,
    install_requires=requirements,
    extras_require={
        'test': dev_requirements
    },
    entry_points={
        'console_scripts': [
            'searx-run = searx.webapp:run',
            'searx-checker = searx.search.checker.__main__:main'
        ]
    },
    package_data={
        'searx': [
            'settings.yml',
            '../README.rst',
            '../requirements.txt',
            '../requirements-dev.txt',
            'data/*',
            'plugins/*/*',
            'static/*.*',
            'static/*/*.*',
            'static/*/*/*.*',
            'static/*/*/*/*.*',
            'static/*/*/*/*/*.*',
            'templates/*/*.*',
            'templates/*/*/*.*',
            'tests/*',
            'tests/*/*',
            'tests/*/*/*',
            'translations/*/*/*'
        ],
    },

)
