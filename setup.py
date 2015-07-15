from __future__ import print_function
from setuptools import setup, find_packages
import io
import codecs
import os
import sys

import task

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

setup(
    name='task',
    version=task.__version__,
    long_description = read('README.md'),
    url='http://github.com/foundling/task/',
    author='Alex Ramsdell',
    author_email='alexramsdell@gmail.com',
    license='MIT',
    description='A really simple command-line task manager.',
    packages=find_packages(),
    scripts=['task.py'],
    package_data = {
      '':['*.md']
    }
    include_package_data=True,
    platforms='any',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Environment :: Console',
        'Intended Audience :: Developers',
				'Intended Audience :: System Administrators',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Productivity'
        ],
    keywords='productivity command-line task-management',

    entry_points={
      'console_scripts': [
          'task=task:main',
      ],
},
),
