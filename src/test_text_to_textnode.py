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

    def test_with_italics_only(self):
        text = "This is going to have *italic* text"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is going to have ", TEXT_TYPE_TEXT),
            TextNode("italic", TEXT_TYPE_ITALIC),
            TextNode(" text", TEXT_TYPE_TEXT),
        ]
        self.assertEqual(nodes, expected)

    def test_with_code_only(self):
        text = "This is going to have `code` text"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is going to have ", TEXT_TYPE_TEXT),
            TextNode("code", TEXT_TYPE_CODE),
            TextNode(" text", TEXT_TYPE_TEXT),
        ]
        self.assertEqual(nodes, expected)

    def test_with_image_only(self):
        text = "This is going to have ![image](https://www.google.com)"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is going to have ", TEXT_TYPE_TEXT),
            TextNode("image", TEXT_TYPE_IMAGE, "https://www.google.com"),
        ]
        self.assertEqual(nodes, expected)

    def test_with_link_only(self):
        text = "This is going to have [link](https://www.google.com)"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is going to have ", TEXT_TYPE_TEXT),
            TextNode("link", TEXT_TYPE_LINK, "https://www.google.com"),
        ]
        self.assertEqual(nodes, expected)

    def test_with_bold_and_italics(self):
        text = "This is going to have **bold** and *italic* text"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is going to have ", TEXT_TYPE_TEXT),
            TextNode("bold", TEXT_TYPE_BOLD),
            TextNode(" and ", TEXT_TYPE_TEXT),
            TextNode("italic", TEXT_TYPE_ITALIC),
            TextNode(" text", TEXT_TYPE_TEXT),
        ]
        self.assertEqual(nodes, expected)

    def test_with_bold_italics_code(self):
        text = "This is going to have **bold**, *italic*, and `code` text"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is going to have ", TEXT_TYPE_TEXT),
            TextNode("bold", TEXT_TYPE_BOLD),
            TextNode(", ", TEXT_TYPE_TEXT),
            TextNode("italic", TEXT_TYPE_ITALIC),
            TextNode(", and ", TEXT_TYPE_TEXT),
            TextNode("code", TEXT_TYPE_CODE),
            TextNode(" text", TEXT_TYPE_TEXT),
        ]
        self.assertEqual(nodes, expected)

    def test_with_4_types(self):
        text = "This is going to have **bold**, *italic*, `code`, and ![image](https://www.google.com)"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is going to have ", TEXT_TYPE_TEXT),
            TextNode("bold", TEXT_TYPE_BOLD),
            TextNode(", ", TEXT_TYPE_TEXT),
            TextNode("italic", TEXT_TYPE_ITALIC),
            TextNode(", ", TEXT_TYPE_TEXT),
            TextNode("code", TEXT_TYPE_CODE),
            TextNode(", and ", TEXT_TYPE_TEXT),
            TextNode("image", TEXT_TYPE_IMAGE, "https://www.google.com"),
        ]
        self.assertEqual(nodes, expected)

    def test_with_5_types(self):
        text = "This is going to have **bold**, *italic*, `code`, ![image](https://www.google.com), and [link](https://www.google.com)"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is going to have ", TEXT_TYPE_TEXT),
            TextNode("bold", TEXT_TYPE_BOLD),
            TextNode(", ", TEXT_TYPE_TEXT),
            TextNode("italic", TEXT_TYPE_ITALIC),
            TextNode(", ", TEXT_TYPE_TEXT),
            TextNode("code", TEXT_TYPE_CODE),
            TextNode(", ", TEXT_TYPE_TEXT),
            TextNode("image", TEXT_TYPE_IMAGE, "https://www.google.com"),
            TextNode(", and ", TEXT_TYPE_TEXT),
            TextNode("link", TEXT_TYPE_LINK, "https://www.google.com"),
        ]
        self.assertEqual(nodes, expected)

    def test_with_5_types_and_text(self):
        text = "This is going to have **bold**, *italic*, `code`, ![image](https://www.google.com), and [link](https://www.google.com) text"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is going to have ", TEXT_TYPE_TEXT),
            TextNode("bold", TEXT_TYPE_BOLD),
            TextNode(", ", TEXT_TYPE_TEXT),
            TextNode("italic", TEXT_TYPE_ITALIC),
            TextNode(", ", TEXT_TYPE_TEXT),
            TextNode("code", TEXT_TYPE_CODE),
            TextNode(", ", TEXT_TYPE_TEXT),
            TextNode("image", TEXT_TYPE_IMAGE, "https://www.google.com"),
            TextNode(", and ", TEXT_TYPE_TEXT),
            TextNode("link", TEXT_TYPE_LINK, "https://www.google.com"),
            TextNode(" text", TEXT_TYPE_TEXT),
        ]
        self.assertEqual(nodes, expected)

    def test_with_unmatched_asterisk(self):
        text = "This is going to have an unmatched * asterisk"
        with self.assertRaises(ValueError):
            text_to_textnodes(text)

    def test_with_multiple_bolds_and_italics(self):
        text = "This is **bold** and *italic* and **another bold** and *another italic* text"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TEXT_TYPE_TEXT),
            TextNode("bold", TEXT_TYPE_BOLD),
            TextNode(" and ", TEXT_TYPE_TEXT),
            TextNode("italic", TEXT_TYPE_ITALIC),
            TextNode(" and ", TEXT_TYPE_TEXT),
            TextNode("another bold", TEXT_TYPE_BOLD),
            TextNode(" and ", TEXT_TYPE_TEXT),
            TextNode("another italic", TEXT_TYPE_ITALIC),
            TextNode(" text", TEXT_TYPE_TEXT),
        ]
        self.assertEqual(nodes, expected)

    def test_with_multiple_bolds_and_italics_and_code(self):
        text = "This is **bold** and *italic* and `code` and **another bold** and *another italic* and `another code` text"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TEXT_TYPE_TEXT),
            TextNode("bold", TEXT_TYPE_BOLD),
            TextNode(" and ", TEXT_TYPE_TEXT),
            TextNode("italic", TEXT_TYPE_ITALIC),
            TextNode(" and ", TEXT_TYPE_TEXT),
            TextNode("code", TEXT_TYPE_CODE),
            TextNode(" and ", TEXT_TYPE_TEXT),
            TextNode("another bold", TEXT_TYPE_BOLD),
            TextNode(" and ", TEXT_TYPE_TEXT),
            TextNode("another italic", TEXT_TYPE_ITALIC),
            TextNode(" and ", TEXT_TYPE_TEXT),
            TextNode("another code", TEXT_TYPE_CODE),
            TextNode(" text", TEXT_TYPE_TEXT),
        ]
        self.assertEqual(nodes, expected)

    def test_with_empty_string(self):
        text = ''
        nodes = text_to_textnodes(text)
        expected = [TextNode([], TEXT_TYPE_TEXT)]
        self.assertEqual(nodes, expected)

    def test_with_only_delimiters(self):
        text = '****'
        nodes = text_to_textnodes(text)
        expected = [TextNode('', TEXT_TYPE_BOLD)]
        self.assertEqual(nodes, expected)

if __name__ == "__main__":
    unittest.main()