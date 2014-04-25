# -*- coding: utf-8 -*-

"""Settings."""

from __future__ import unicode_literals, print_function, absolute_import, division

import os

FILES_FOLDER = 'FILES'
XML_FOLDER = 'XML'
XSLT_FOLDER = 'XSLT'
OUTPUT_FOLDER = 'OUTPUT'

XML_FILE = "material_small.xml"
XSLT_FILE = "fabory.xslt"
OUTPUT_FILE = "fabory_output.xml"

XML_PATH = os.path.abspath(os.path.join(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__).replace('\\', '/'), '..'), FILES_FOLDER), XML_FOLDER), XML_FILE))
XSLT_PATH = os.path.abspath(os.path.join(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__).replace('\\', '/'), '..'), FILES_FOLDER), XSLT_FOLDER), XSLT_FILE))
OUTPUT_PATH = os.path.abspath(os.path.join(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__).replace('\\', '/'), '..'), FILES_FOLDER), OUTPUT_FOLDER), OUTPUT_FILE))
