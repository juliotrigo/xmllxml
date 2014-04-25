# -*- coding: utf-8 -*-

"""Python lxml package examples.

This submodule must is in Python 2.7 temporary.
"""

from __future__ import unicode_literals, print_function, absolute_import, division

from lxml import etree


class XMLParser(object):

    """XML parser."""

    def __init__(self, xml_doc, from_file=True):
        """Initialization of the instance."""
        if xml_doc == '' or xml_doc == None:
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
