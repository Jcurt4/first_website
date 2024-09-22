import unittest 
from htmlnode import ParentNode, LeafNode, HTMLNode


class TestParentNode(unittest.TestCase):
    def test_parent_node(self):
        node = ParentNode(
            children=[
                LeafNode(value='Hello', tag='p'),
                LeafNode(value='World', tag='p')
            ], tag='a', props={'href': 'http://www.google.com'}
        )

        expected_output = '<a href="http://www.google.com"><p>Hello</p><p>World</p></a>'

        self.assertEqual(node.to_html(), expected_output)

    def test_parent_node_no_tag(self):
        with self.assertRaises(ValueError) as context:
            node = ParentNode(
                children=[
                    LeafNode('Hello', 'p'),
                    LeafNode('World', 'p')
                ], props={'href': 'http://www.google.com'}
            )
            node.to_html()

        self.assertEqual(str(context.exception), 'Must have a tag')

    def test_parent_node_no_children(self):
        with self.assertRaises(ValueError) as context:
            node = ParentNode(
                tag='a', props={'href': 'http://www.google.com'}
            )
            node.to_html()

        self.assertEqual(str(context.exception), 'Must have children')

    def test_parent_node_no_props(self):
        node = ParentNode(
            children=[
                LeafNode(value='Hello', tag='p'),
                LeafNode(value='World', tag='p')
            ], tag='a'
        )

        expected_output = '<a><p>Hello</p><p>World</p></a>'

        self.assertEqual(node.to_html(), expected_output)

    def test_parent_node_no_props_no_tag(self):
        with self.assertRaises(ValueError) as context:
            node = ParentNode(
                children=[
                    LeafNode(value='Hello', tag='p'),
                    LeafNode(value='World', tag='p')
                ],
                tag=None,
                props=None
            )
            node.to_html()

        self.assertEqual(str(context.exception), 'Must have a tag')

    def test_parent_node_no_props_no_children(self):
        with self.assertRaises(ValueError) as context:
            node = ParentNode(
                tag='a',
                children=None,
                props=None
            )
            node.to_html()

        self.assertEqual(str(context.exception), 'Must have children')

    def test_no_props(self):
        node = ParentNode(
            children=[
                LeafNode(value='Hello', tag='p'),
                LeafNode(value='World', tag='p')
            ], tag='a'
        )

        expected_output = '<a><p>Hello</p><p>World</p></a>'

        self.assertEqual(node.to_html(), expected_output)


if __name__ == '__main__':
    unittest.main()