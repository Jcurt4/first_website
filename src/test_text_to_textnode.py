import unittest
from textnode import *
from delimiter import *
from text_to_textnode import *

class TestTextToTextNode(unittest.TestCase):
    def test_basic_no_format(self):
        text = "Hello World!"
        nodes = text_to_textnodes(text)
        expected = [TextNode(text, TEXT_TYPE_TEXT)]
        self.assertEqual(nodes, expected)

    def test_with_bold_only(self):
        text = "This is going to have **bold** text"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is going to have ", TEXT_TYPE_TEXT),
            TextNode("bold", TEXT_TYPE_BOLD),
            TextNode(" text", TEXT_TYPE_TEXT),
        ]
        self.assertEqual(nodes, expected)

    def text_with_italics_only(self):
        text = "This is going to have *italic* text"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is going to have ", TEXT_TYPE_TEXT),
            TextNode("italic", TEXT_TYPE_ITALIC),
            TextNode(" text", TEXT_TYPE_TEXT),
        ]
        self.assertEqual(nodes, expected)


if __name__ == "__main__":
    unittest.main()