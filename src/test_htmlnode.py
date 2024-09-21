import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            tag='a',
            value='',
            children=None,
            props={
                'href': 'https://www.google.com',
                'target': '_blank'
            }
        )
        
        expected_output = ' href="https://www.google.com" target="_blank"'
        
        self.assertEqual(node.props_to_html(), expected_output)


    def test_props_to_html(self):
        node = HTMLNode(
            tag='b',
            value='',
            children=None,
            props={
                'href': 'https://www.thisisanothertest.com',
                'target': 'praying I can get this one right'
            }
        )

        expected_output = ' href="https://www.thisisanothertest.com" target="praying I can get this one right"'

        self.assertEqual(node.props_to_html(), expected_output)

    def test_props_to_html(self):
        node = HTMLNode(
            tag=None, 
            value=None,
            children=None
        )

if __name__ == '__main__':
    unittest.main()