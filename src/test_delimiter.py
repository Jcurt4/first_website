import unittest
from textnode import TextNode
from delimiter import split_nodes_delimiter



class TestDelimiter(unittest.TestCase):
    def test_basic_split(self):
        node = TextNode('This is a text node with a "code block" word', 'text')
        new_nodes = split_nodes_delimiter([node], '"', 'code')
        print(f'Actual Nodes returned: {new_nodes}')
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, 'This is a text node with a ')
        self.assertEqual(new_nodes[1].text, 'code block')
        self.assertEqual(new_nodes[1].text_type, 'code')
        self.assertEqual(new_nodes[2].text, ' word')

    def test_no_delimiter(self):
        with self.assertRaises(ValueError):
            node = TextNode('This is a node with no delimiter', 'text')
            new_nodes = split_nodes_delimiter([node], delimiter=None)

    def test_mismatched_delimiters(self):
        with self.assertRaises(ValueError):
            node = TextNode("This is a test of *mismatched' delimiters", 'text')
            split_nodes_delimiter([node], "*")

    def test_more_than_one_split(self):
        node = TextNode('This is going to *have* more than *one* split', 'text')
        new_nodes = split_nodes_delimiter([node], '*')
        self.assertEqual(new_nodes[0].text, 'This is going to ')
        self.assertEqual(new_nodes[1].text, 'have')
        self.assertEqual(new_nodes[2].text, ' more than ')
        self.assertEqual(new_nodes[3].text, 'one')
        self.assertEqual(new_nodes[4].text, ' split')

    def test_for_bold(self):
        node = TextNode('This is going to be *bold* text', 'text')
        new_nodes = split_nodes_delimiter([node], '*', 'bold')
        self.assertEqual()


if __name__ == "__main__":
    unittest.main()