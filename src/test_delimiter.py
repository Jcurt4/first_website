import unittest
from textnode import TextNode
from delimiter import split_nodes_delimiter



class TestDelimiter(unittest.TestCase):
    def test_basic_split(self):
        node = TextNode('This is a text node with a "code block" word', 'text')
        new_nodes = split_nodes_delimiter([node], '"', 'code')
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, 'This is a text node with a ')
        self.assertEqual(new_nodes[1].text, 'code block')
        self.assertEqual(new_nodes[1].text_type, 'code')
        self.assertEqual(new_nodes[2].text, ' word')

        print('All assertations have passed for basic split test!')

    def test_no_delimiter(self):
        node = TextNode('This is a text node with no delimiter and text as text type', 'text')
        new_nodes = split_nodes_delimiter([node], '', 'text')
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, 'This is a text node with no delimiter and text as text type')
        self.assertEqual(new_nodes[0].text_type, 'text')
        
    def test_no_text_type(self):
        node = TextNode('This is a text node with **no** text type', '')
        new_nodes = split_nodes_delimiter([node], '**', '')
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, 'This is a text node with ')
        self.assertEqual(new_nodes[1].text, 'no')
        self.assertEqual(new_nodes[2].text, 'text type')
        self.assertEqual(new_nodes[1].text_type, '')


if __name__ == "__main__":
    unittest.main()