import unittest
from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """
# Hello world! 

This is a paragraph to test my newest funcion.  I need to make sure that is is working correctly.
this means this is still part of the paragraph.  
so it this.
and this. 

*but this will be an unordered list item
*another one
*dj khaled
"""
        blocks = markdown_to_blocks(markdown)
        expected = [
            "# Hello world!",
            "This is a paragraph to test my newest funcion.  I need to make sure that is is working correctly. this means this is still part of the paragraph.  so it this. and this.",
            "*but this will be an unordered list item\n*another one\n*dj khaled",
        ]
        self.assertEqual(blocks, expected)




if __name__ == '__main__':
    unittest.main()