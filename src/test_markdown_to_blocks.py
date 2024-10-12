import unittest
from markdown_to_blocks import markdown_to_blocks, block_to_block_type, BLOCK_TYPE_PARAGRAPH, BLOCK_TYPE_HEADER, BLOCK_TYPE_UNORDERED_LIST, BLOCK_TYPE_ORDERED_LIST, BLOCK_TYPE_QUOTE, BLOCK_TYPE_CODE


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
            "This is a paragraph to test my newest funcion.  I need to make sure that is is working correctly.\nthis means this is still part of the paragraph.\nso it this.\nand this.",
            "*but this will be an unordered list item\n*another one\n*dj khaled",
        ]
        self.assertEqual(blocks, expected)

    def test_markdown_to_blocks_empty(self):
        markdown = ""
        blocks = markdown_to_blocks(markdown)
        expected = []
        self.assertEqual(blocks, expected)

    def test_markdown_to_blocks_no_newlines(self):
        markdown = "# Hello world!"
        blocks = markdown_to_blocks(markdown)
        expected = ["# Hello world!"]
        self.assertEqual(blocks, expected)
    
    def test_with_multiple_newlines(self):
        markdown = """
        this is a test with multiple new lines.



        between the blocks."""
        blocks = markdown_to_blocks(markdown)
        expected = ["this is a test with multiple new lines.", "between the blocks."]
        self.assertEqual(blocks, expected)

    def test_with_leading_and_trailing_blank_space(self):
        markdown = """
                     this is a test with a bunch of leading and trailing white space       




                            """
        blocks = markdown_to_blocks(markdown)
        expected = ["this is a test with a bunch of leading and trailing white space"]
        self.assertEqual(blocks, expected)


class TestBlockToBlockType(unittest.TestCase):
    def test_basic_function(self):
        block = "this is a paragraph"
        block_type = block_to_block_type(block)
        expected = BLOCK_TYPE_PARAGRAPH
        self.assertEqual(block_type, expected)

    def test_header(self):
        block = "# this is a header"
        block_type = block_to_block_type(block)
        expected = BLOCK_TYPE_HEADER
        self.assertEqual(block_type, expected)
    
    def test_unordered_list(self):
        block = "* this is an unordered list"
        block_type = block_to_block_type(block)
        expected = BLOCK_TYPE_UNORDERED_LIST
        self.assertEqual(block_type, expected)

    def test_ordered_list(self):
        block = """1. this is an ordered list
        2. this is the second item
        3. this is the third item"""
        block_type = block_to_block_type(block)
        expected = BLOCK_TYPE_ORDERED_LIST
        self.assertEqual(block_type, expected)
    
    def test_quote(self):
        block = "> this is a quote"
        block_type = block_to_block_type(block)
        expected = BLOCK_TYPE_QUOTE
        self.assertEqual(block_type, expected)
    
    def test_code(self):
        block = "```this is a code block```"
        block_type = block_to_block_type(block)
        expected = BLOCK_TYPE_CODE
        self.assertEqual(block_type, expected)

    def test_ordered_with_wrong_order(self):
        block = """1. this is an ordered list
        2. this is the second item
        4. this is the fourth item"""
        block_type = block_to_block_type(block)
        expected = BLOCK_TYPE_PARAGRAPH
        self.assertEqual(block_type, expected)
    


if __name__ == '__main__':
    unittest.main()