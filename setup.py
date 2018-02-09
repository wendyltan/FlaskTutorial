#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/9 14:57
# @Author  : Wendyltanpcy
# @File    : setup.py
# @Software: PyCharm


from setuptools import setup

setup(
    name='flaskr',
    packages=['flaskr'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)