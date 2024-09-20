import unittest

from textnode import TextNode


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

    


if __name__ == "__main__":
    unittest.main()