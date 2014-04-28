# -*- coding: utf-8 -*-

"""Main module."""

from __future__ import unicode_literals, print_function, absolute_import, division


from xmllxml.xmlparser import XMLParser
from xmllxml.xslttransformer import XSLTransformer
from xmllxml.settings import XML_PATH, XSLT_PATH, OUTPUT_PATH, OUTPUT_METHOD

if __name__ == '__main__':
    transformer = XSLTransformer(xml_parser=XMLParser(XML_PATH, from_file=True),
                                 xslt_parser=XMLParser(XSLT_PATH, from_file=True),
                                 output_path=OUTPUT_PATH)
    transformer.transform()
    transformer.write_output(OUTPUT_METHOD)
