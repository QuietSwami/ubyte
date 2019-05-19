#!/usr/bin/env python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ubyte',  
    version='0.1',
    scripts=['ubyte'] ,
    author="Francisco Mendonça",
    author_email="fran.abm94@gmail.com  ",
    description="A UByte file creator and reader.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/QuietSwami/ubyte",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)