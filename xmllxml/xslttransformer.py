# -*- coding: utf-8 -*-

"""XSLT transformation module."""

from __future__ import unicode_literals, print_function, absolute_import, division
import codecs

from lxml import etree


class XSLTransformer(object):

    """XSLT transformation class."""

    def __init__(self, xml_parser, xslt_parser, output_path):
        """Initialization of the instance.
        """
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
        with codecs.open(self.output_path, "w", encoding="utf-8") as f:
            if output_method == 'text':
                #http://lxml.de/FAQ.html#what-is-the-difference-between-lxml-etree-and-lxml-objectify
                output_string = str(self.result_tree)
            else:
                output_string = etree.tostring(self.result_tree,
                                               encoding='UTF-8',
                                               method=output_method,
                                               xml_declaration=True,
                                               pretty_print=True)
            f.write(output_string.decode('utf-8'))
