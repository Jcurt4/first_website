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
        self.assertEqual(new_nodes[0].text, 'This is going to be ')
        self.assertEqual(new_nodes[1].text, 'bold')
        self.assertEqual(new_nodes[1].text_type, 'bold')
        self.assertEqual(new_nodes[2].text, ' text')

    def test_for_italics(self):
        node = TextNode('This is going to be _italic_ text', 'text')
        new_nodes = split_nodes_delimiter([node], '_', 'italic')
        self.assertEqual(new_nodes[0].text, 'This is going to be ')
        self.assertEqual(new_nodes[1].text, 'italic')
        self.assertEqual(new_nodes[1].text_type, 'italic')
        self.assertEqual(new_nodes[2].text, ' text')

    def test_for_code(self):
        node = TextNode('This is going to be `code` text', 'text')
        new_nodes = split_nodes_delimiter([node], '`', 'code')
        self.assertEqual(new_nodes[0].text, 'This is going to be ')
        self.assertEqual(new_nodes[1].text, 'code')
        self.assertEqual(new_nodes[1].text_type, 'code')
        self.assertEqual(new_nodes[2].text, ' text')

    def test_empty_string(self):
        node = TextNode("", "text")
        new_nodes = split_nodes_delimiter([node], "*", "bold")
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "")
        self.assertEqual(new_nodes[0].text_type, "text")

    def test_no_delimiter_in_text(self):
        node = TextNode("This is a test without a delimiter", "text")
        new_nodes = split_nodes_delimiter([node], "*")
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "This is a test without a delimiter")
        self.assertEqual(new_nodes[0].text_type, "text")
    
    def test_with_multiple_nodes(self):
        node1 = TextNode("This is a test with a ", "text")
        node2 = TextNode("*code* block", "text")
        node3 = TextNode(" and more text", "text")
        new_nodes = split_nodes_delimiter([node1, node2, node3], "*", "code")
        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0].text, "This is a test with a ")
        self.assertEqual(new_nodes[1].text, "code")
        self.assertEqual(new_nodes[1].text_type, "code")
        self.assertEqual(new_nodes[2].text, " block")
        self.assertEqual(new_nodes[3].text, " and more text")

    def test_delimiter_at_start(self):
        node = TextNode("*This* is a test where the first word is bold", "text")
        new_nodes = split_nodes_delimiter([node], "*", "bold")
        self.assertEqual(len(new_nodes), 2)
        self.assertEqual(new_nodes[0].text, "This")
        self.assertEqual(new_nodes[0].text_type, "bold")
        self.assertEqual(new_nodes[1].text, " is a test where the first word is bold")

    def test_delimiter_at_end(self):
        node = TextNode("This is a test where the last word is *bold*", "text")
        new_nodes = split_nodes_delimiter([node], "*", "bold")
        self.assertEqual(len(new_nodes), 2)
        self.assertEqual(new_nodes[0].text, "This is a test where the last word is ")
        self.assertEqual(new_nodes[1].text, "bold")
        self.assertEqual(new_nodes[1].text_type, "bold")

    def test_multiple_delimiters_in_one_line(self):
        node = TextNode("This is a test with *multiple* delimiters *in* one line", "text")
        new_nodes = split_nodes_delimiter([node], "*", "bold")
        self.assertEqual(len(new_nodes), 5)
        self.assertEqual(new_nodes[0].text, "This is a test with ")
        self.assertEqual(new_nodes[1].text, "multiple")
        self.assertEqual(new_nodes[1].text_type, "bold")
        self.assertEqual(new_nodes[2].text, " delimiters ")
        self.assertEqual(new_nodes[3].text, "in")
        self.assertEqual(new_nodes[3].text_type, "bold")
        self.assertEqual(new_nodes[4].text, " one line")

    def test_for_unpaired_delimiter(self):
        with self.assertRaises(ValueError):
            node = TextNode("This is a test with an unpaired * delimiter", "text")
            split_nodes_delimiter([node], "*")

    def test_with_nothing_between_delimiters(self):
        node = TextNode("This is a test with ** between delimiters", "text")
        new_nodes = split_nodes_delimiter([node], "*", "bold")
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is a test with ")
        self.assertEqual(new_nodes[1].text, "")
        self.assertEqual(new_nodes[1].text_type, "bold")
        self.assertEqual(new_nodes[2].text, " between delimiters")

if __name__ == "__main__":
    unittest.main()