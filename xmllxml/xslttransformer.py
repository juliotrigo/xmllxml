# -*- coding: utf-8 -*-

"""XSLT transformation."""

from __future__ import unicode_literals, print_function, absolute_import, division
import codecs

from lxml import etree

from .xmlparser import XMLParser


class XSLTransformer(object):

    """XSLT transformation."""

    def __init__(self, xml_path, xslt_path, output_path):
        """Initialization of the instance.
        """
        xml_parser = XMLParser(xml_path, from_file=True)
        xslt_parser = XMLParser(xslt_path, from_file=True)

        self.xml_doc = xml_parser.xml_doc
        self.xslt_doc = xslt_parser.xml_doc
        self.output_path = output_path
        self.result_tree = None

    def transform(self):
        """Transforms the document."""
        transform = etree.XSLT(self.xslt_doc)
        self.result_tree = transform(self.xml_doc)

    def write_output(self):
        """Writes the result tree to a file."""
        try:
            f = codecs.open(self.output_path, "w", "utf-8")
            f.write(etree.tostring(self.result_tree))
        finally:
            f.close()
