# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in palfingercraft/__init__.py
from palfingercraft import __version__ as version

setup(
	name='palfingercraft',
	version=version,
	description='Craft Changes in Palfinger',
	author='Craft',
	author_email='info@craftinteractive.ae',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
