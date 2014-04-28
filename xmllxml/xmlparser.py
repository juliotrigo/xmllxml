# -*- coding: utf-8 -*-

"""XML parser module."""

from __future__ import unicode_literals, print_function, absolute_import, division

from lxml import etree


class XMLParser(object):

    """XML parser class."""

    def __init__(self, xml_doc, from_file=True):
        """Initialization of the instance."""
        if xml_doc == '' or xml_doc is None:
            raise Exception("XML document not valid.")
        else:
            if from_file:
                self.xml_doc = self.read_xml_from_file(xml_doc)
            else:
                self.xml_doc = self.read_xml_from_string(xml_doc)

    def read_xml_from_string(self, string):
        """Parses a XML document from a string."""
        doc = etree.fromstring(string)
        return doc

    def read_xml_from_file(self, file_name):
        """Parses a XML document from a file."""
        doc = etree.parse(file_name)
        return doc

    def print_document(self):
        """Returns a Unicode string representation of the document."""
        output_string = etree.tostring(self.xml_doc,
                                       encoding='UTF-8',
                                       method='xml',
                                       xml_declaration=True,
                                       pretty_print=True)
        return output_string.decode('utf-8')
