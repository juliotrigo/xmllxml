# -*- coding: utf-8 -*-

"""Main module."""

from __future__ import unicode_literals, print_function, absolute_import, division

from xmllxml.xslttransformer import XSLTransformer
from xmllxml.settings import XML_PATH, XSLT_PATH, OUTPUT_PATH

if __name__ == '__main__':
    transformer = XSLTransformer(xml_path=XML_PATH,
                                 xslt_path=XSLT_PATH,
                                 output_path=OUTPUT_PATH)
    transformer.transform()
    transformer.write_output()
