# -*- coding: utf-8 -*-

"""Unit tests. XML Parser."""

import unittest

from xmllxml.xmlparser import XMLParser


class XMLParserTestCase(unittest.TestCase):

    """Tests general xml functionality."""

    def setUp(self):
        """Set up method."""
        pass

    def tearDown(self):
        """Tear down method."""
        pass

    def test_parse_bad_xml_from_string(self):
        xml_string = """<?xml version="1.0" encoding="UTF-8"?>
            <CML version="1.0">
            <dd>
            </CML>"""
        self.assertRaises(Exception, XMLParser, xml_string, from_file=False)

#    def test_parse_ok_xml_from_string(self):
#        xml_string = """<?xml version="1.0" encoding="UTF-8"?>
#<CML version="1.0">Hi</CML>"""
#        parser = XMLParser(xml_string, from_file=False)
#        doc = parser.print_document()

#        xml_unicode = xml_string.decode('utf-8')
#        doc_strip = doc.rstrip(' \n\t')

#        print(type(xml_unicode))
#        print(type(doc_strip))
#        print('*' + xml_unicode + '*')
#        print('*' + doc_strip + '*')
#        print(xml_unicode.encode('utf-8'))
#        print(doc_strip.encode('utf-8'))
#        self.assertEqual(xml_unicode, doc_strip, 'We get the xml same.')

if __name__ == '__main__':
    unittest.main()
