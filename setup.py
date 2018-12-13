#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(name='dkim-generator',
      version='0.0.1',
      url='https://github.com/Fourier1/dkim_generator.git',
      license='MIT',
      author='Fourier Saint',
      author_email='fouriersaint@gmail.com',
      install_requires=[
      ],
      classifiers=[

          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Topic :: Software Development :: Libraries',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',

      ],
      description='All librairies for Micro-service',
      packages=find_packages(exclude=['tests', '.git', 'env', '.gitignore']),
      zip_safe=False)