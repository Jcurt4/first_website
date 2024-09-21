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


if __name__ == '__main__':
    unittest.main()