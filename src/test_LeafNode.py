import unittest
from htmlnode import LeafNode


class TestlLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode(
            value='this is an initial test',
            tag='a'
        )
        expected_output = '<a>this is an initial test</a>'

        self.assertEqual(node.to_html(), expected_output)

    def test_to_html_no_tag(self):
        node = LeafNode(
            value='this is an initial test',
            tag=None
        )
        expected_output = 'this is an initial test'

        self.assertEqual(node.to_html(), expected_output)

    def test_to_html_no_value(self):
        with self.assertRaises(ValueError) as context:
            node = LeafNode(
                value=None,
                tag='a'
            )
            node.to_html()

        self.assertEqual(str(context.exception), 'Must provide a value')

    def test_to_html_with_props(self):
        node = LeafNode(
            value='this is an initial test',
            tag='a',
            props={'href': 'http://www.google.com'}
        )
        expected_output = '<a href="http://www.google.com">this is an initial test</a>'

        self.assertEqual(node.to_html(), expected_output)


if __name__ == '__main__':
    unittest.main()