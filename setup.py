#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

version = '0.0.1'

setup(
    name='pyscheduler',
    version=version,
    description='Create scheduled tasks at runtime easily',
    long_description=README,
    url='https://github.com/baranbartu/pyscheduler',
    download_url='https://github.com/baranbartu/pyscheduler/tarball/%s' % version,
    author='Baran Bartu Demirci',
    author_email='bbartu.demirci@gmail.com',
    license='MIT',
    keywords='scheduler scheduled tasks crontab cron cronjob celery',
    packages=find_packages(),
    install_requires=[
        'crontab==0.21.3',
    ]
)
