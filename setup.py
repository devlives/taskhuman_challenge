#!/usr/bin/env python
import os
from setuptools import setup


def read(fname):
    """ Reads a file; Used everywhere.

    :param fname: The name of a file relative to the root path
    :return: The string contents of the file
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='TaskHuman Challenge',
    version='1.0',
    description='Data Challenge',
    long_description=read('README.md'),
    author='Kartik P',
    author_email='kartik@taskhuman.com',
    url='https://www.taskhuman.com/',
    packages=['dags'],
    install_requires=read('requirements.txt'),
)
