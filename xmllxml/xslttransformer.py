# -*- coding: utf-8 -*-

"""XSLT transformation module."""

from __future__ import unicode_literals, print_function, absolute_import, division
import codecs

from lxml import etree

from .xmlparser import XMLParser


class XSLTransformer(object):

    """XSLT transformation class."""

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
        """Transforms the document using the template."""
        transform = etree.XSLT(self.xslt_doc)
        self.result_tree = transform(self.xml_doc)

    def write_output(self, output_method='xml'):
        """Writes the result tree to a file.

        The keyword argument 'output_method' selects the output method:
        'xml', 'html', 'text' or 'c14n'. Default is 'xml'."""
        with codecs.open(self.output_path, "w", "utf-8") as f:
            f.write(etree.tostring(self.result_tree,
                                   encoding='UTF-8',
                                   method=output_method,
                                   xml_declaration=True,
                                   pretty_print=True))
