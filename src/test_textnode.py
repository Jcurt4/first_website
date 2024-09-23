import unittest

from textnode import *
from htmlnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(repr(node), repr(node2))

    def test_repr_format(self):
        node = TextNode("This is a text node", "bold")
        expected = "TextNode('This is a text node', 'bold', None)"
        self.assertEqual(repr(node), expected)

    def test_url_is_none(self):
        node = TextNode("This is a text node for url is none test", "bold", None)
        node2 = TextNode("This is a text node for url is none test", "bold", None)
        self.assertEqual(node, node2)

    def test_url_is_not_none(self):
        node = TextNode("This is a text node for url is not none test", "bold", "http://www.google.com")
        node2 = TextNode("This is a text node for url is not none test", "bold", "http://www.google.com")
        self.assertEqual(node, node2)

    def test_textnode_to_html_node_text(self):
        text_node = TextNode("This is a text node", "text")
        html_node = text_node_to_html_node(text_node)
        excpected = 'This is a text node'

        self.assertEqual(html_node.to_html(), excpected)

    def test_textnode_to_html_node_bold(self):
        text_node = TextNode("This is a text node", "bold")
        html_node = text_node_to_html_node(text_node)
        excpected = '<b>This is a text node</b>'

        self.assertEqual(html_node.to_html(), excpected)

    def test_textnode_to_html_node_italic(self):
        text_node = TextNode("This is a text node", "italic")
        html_node = text_node_to_html_node(text_node)
        excpected = '<i>This is a text node</i>'

        self.assertEqual(html_node.to_html(), excpected)

    def test_textnode_to_html_node_code(self):
        text_node = TextNode("This is a text node", "code")
        html_node = text_node_to_html_node(text_node)
        excpected = '<code>This is a text node</code>'

        self.assertEqual(html_node.to_html(), excpected)

    def test_textnode_to_html_node_link(self):
        text_node = TextNode("This is a text node", "link", "http://www.google.com")
        html_node = text_node_to_html_node(text_node)
        excpected = '<a href="http://www.google.com">This is a text node</a>'

        self.assertEqual(html_node.to_html(), excpected)

    def test_textnode_to_html_node_image(self):
        text_node = TextNode("This is a text node", "image", "http://www.google.com")
        html_node = text_node_to_html_node(text_node)
        excpected = '<img src="http://www.google.com" alt="This is a text node">'

        self.assertEqual(html_node.to_html(), excpected)

    def test_textnode_to_html_node_unsupported_text_type(self):
        with self.assertRaises(ValueError) as context:
            text_node = TextNode("This is a text node", "unsupported")
            text_node_to_html_node(text_node)

        self.assertEqual(str(context.exception), 'Unsupported text type: unsupported')

    def test_textnode_to_html_node_empty_string(self):
        text_node = TextNode("", "text")
        html_node = text_node_to_html_node(text_node)
        excpected = ''

        self.assertEqual(html_node.to_html(), excpected)

    def test_textnode_to_html_node_none_type(self):
        text_node = TextNode("This is a text node", None)
        html_node = text_node_to_html_node(text_node)
        expected = 'This is a text node'
        self.assertEqual(html_node.to_html(), expected)

if __name__ == "__main__":
    unittest.main()