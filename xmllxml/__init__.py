# -*- coding: utf-8 -*-

"""Python xml manipulation interface.

This package uses the lxml package and is written in Python 2.7.

It reads an XML document and a XSLT template and transforms the XML
into xml, html or text.

Usage:
$ xmllxml/main.py

Folder layout:
[project folder]
    tests/
    xmllxml/              Package folder.
        ...
        main.py           Starting point of the application.
        settings.py       Configuration module.
        ...
    requirements_dev.py
    requirements.py

The input and output folder layout and the output method can be changed
in the settings.py file.
    OUTPUT/           Output files should be placed here.
    XML/              XML files should be placed here.
    XSLT/             XSLT templates should be placed here.
"""

__version__ = '1.0.0'
