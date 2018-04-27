import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='porespy-examples',
    description='A set of tools for analyzing 3D images of porous materials',
    version=main_['__version__'],
    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python',
                 'Topic :: Scientific/Engineering',
                 'Topic :: Scientific/Engineering :: Physics'],
    author='Jeff Gostick',
    author_email='jgostick@gmail.com',
    url='http://porespy.org'
)
