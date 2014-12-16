#!/usr/bin/env python
# -*- encoding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = {
    "description": "My Project",
    "author": "Ranieri Rodrigues",
    "url": "https://github.com/rnrodrigues/myproject",
    "download_url": "",
    "author_email": "rnrodrigs@gmail.com",
    "version": "0.0.1",
    "install_requires": ["nose"],
    "packages": ["myapp"],
    "scripts": [],
    "name": "myproject"
}


setup(**config)
