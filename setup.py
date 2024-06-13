#!/usr/bin/env python

PROJ_NAME = 'romkan'
PACKAGE_NAME = 'romkan'

PROJ_METADATA = '%s.json' % PROJ_NAME

import os
import json
import importlib.util

here = os.path.abspath(os.path.dirname(__file__))
proj_info = json.loads(open(os.path.join(here, PROJ_METADATA)).read())
README = open(os.path.join(here, 'README.rst')).read()
CHANGELOG = open(os.path.join(here, 'CHANGELOG.rst')).read()

version_path = os.path.join(here, 'src', PACKAGE_NAME, 'version.py')
spec = importlib.util.spec_from_file_location('version', version_path)
version = importlib.util.module_from_spec(spec)
spec.loader.exec_module(version)
VERSION = version.__version__

from setuptools import setup, find_packages
setup(
    name=proj_info['name'],
    version=VERSION,
    
    author=proj_info['author'],
    author_email=proj_info['author_email'],
    url=proj_info['url'],
    license=proj_info['license'],
    
    description=proj_info['description'],
    keywords=proj_info['keywords'],
    
    long_description=README + '\n\n' + CHANGELOG,
    
    packages=find_packages('src'),
    package_dir={'': 'src'},
    
    test_suite='tests',
    
    platforms='any',
    zip_safe=False,
    include_package_data=True,
    
    classifiers=proj_info['classifiers'],
)
