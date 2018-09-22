#! /usr/bin/env python
"""vaultuploader install script."""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name="vaultuploader",
    version="0.0.1",
    description="A certificate uploader for Vault written in Python",
    long_description=open("README.md").read(),
    author="Stefan Caraiman",
    url="https://github.com/stefan-caraiman/vaultuploader",
    packages=["vaultuploader"],
    scripts=["scripts/vaultuploader"],
    requires=open("requirements.txt").readlines(),
)
