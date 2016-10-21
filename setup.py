#!/usr/bin/env python

from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='PythonInteractiveMath',
    version='0.1',
    description='Python package for writing interactive math documents.',
    long_description=readme(),
    author='Joshua Frye',
    author_email='josh.n.frye@gmail.com ',
    url='https://github.com/jnfrye/python_interactive_math',

    packages=[
        'py_interactive_math',
    ],
    install_requires=[],
)
