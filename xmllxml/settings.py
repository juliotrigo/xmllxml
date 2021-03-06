# -*- coding: utf-8 -*-

"""Settings."""

from __future__ import unicode_literals, print_function, absolute_import, division

import os

OUTPUT_METHOD = 'text'  # 'xml', 'html', 'text' or 'c14n'.

XML_FOLDER = '/XML/'
XSLT_FOLDER = '/XSLT/'
OUTPUT_FOLDER = '/OUTPUT/'

XML_FILE = "data.xml"
XSLT_FILE = "template.xslt"
OUTPUT_FILE = "output.csv"

#FILES_FOLDER = 'FILES'
#XML_PATH = os.path.abspath(os.path.join(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__).replace('\\', '/'), '..'), FILES_FOLDER), XML_FOLDER), XML_FILE))
#XSLT_PATH = os.path.abspath(os.path.join(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__).replace('\\', '/'), '..'), FILES_FOLDER), XSLT_FOLDER), XSLT_FILE))
#OUTPUT_PATH = os.path.abspath(os.path.join(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__).replace('\\', '/'), '..'), FILES_FOLDER), OUTPUT_FOLDER), OUTPUT_FILE))

XML_PATH = os.path.abspath(os.path.join(os.path.dirname(XML_FOLDER).replace('\\', '/'), XML_FILE))
XSLT_PATH = os.path.abspath(os.path.join(os.path.dirname(XSLT_FOLDER).replace('\\', '/'), XSLT_FILE))
OUTPUT_PATH = os.path.abspath(os.path.join(os.path.dirname(OUTPUT_FOLDER).replace('\\', '/'), OUTPUT_FILE))
