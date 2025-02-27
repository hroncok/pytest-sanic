#!/usr/bin/env python
import os
from setuptools import setup, find_packages

base = os.path.dirname(os.path.abspath(__file__))

README_PATH = os.path.join(base, "README.rst")

install_requires = [
    'pytest>=5.2',
    'httpx>=0.15.4',
    'async_generator>=1.10',
    'websockets>=9.1,<10.0',
]

tests_require = []

setup(name='pytest-sanic',
      version='1.8.1',
      description='a pytest plugin for Sanic',
      long_description=open(README_PATH).read(),
      author='Yun Xu',
      author_email='yunxu1992@gmail.com',
      license='ASL 2.0',
      url='https://github.com/yunstanford/pytest-sanic/',
      packages=find_packages(exclude=["tests.*", "tests"]),
      install_requires=install_requires,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Operating System :: MacOS',
          'Operating System :: POSIX :: Linux',
          'Topic :: System :: Software Distribution',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
      ],
      entry_points={
        'pytest11': ['sanic = pytest_sanic.plugin'],
      },
)
