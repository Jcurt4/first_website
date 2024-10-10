import unittest
from textnode import TextNode
from delimiter import split_nodes_delimiter, extract_markdown_images, split_nodes_image, split_nodes_link



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


class TestMarkdownImage(unittest.TestCase):
    def test_basic_funtion(self):
        text = 'This is a test with an image ![alt text](image.jpg)'
        images = extract_markdown_images(text)
        self.assertEqual(len(images), 1)
        self.assertEqual(images[0][0], 'alt text')
        self.assertEqual(images[0][1], 'image.jpg')

    def test_with_multi_images(self):
        text = 'This is a test with an image ![alt text](image.jpg) and another ![alt text](image2.jpg)'
        images = extract_markdown_images(text)
        self.assertEqual(len(images), 2)
        self.assertEqual(images[0][0], 'alt text')
        self.assertEqual(images[0][1], 'image.jpg')
        self.assertEqual(images[1][0], 'alt text')
        self.assertEqual(images[1][1], 'image2.jpg')

    def test_no_images(self):
        text = 'This is a test with no images'
        images = extract_markdown_images(text)
        self.assertEqual(len(images), 0)

    def test_with_special_characters1(self):
        text = 'This is a test with an image ![alt text with spaces](image.jpg)'
        images = extract_markdown_images(text)
        self.assertEqual(len(images), 1)
        self.assertEqual(images[0][0], 'alt text with spaces')
        self.assertEqual(images[0][1], 'image.jpg')
        
    def test_with_special_characters2(self):
        text = 'This is a test with an image ![alt text with spaces](image with spaces.jpg)'
        images = extract_markdown_images(text)
        self.assertEqual(len(images), 1)
        self.assertEqual(images[0][0], 'alt text with spaces')
        self.assertEqual(images[0][1], 'image with spaces.jpg')

    def test_with_special_characters3(self):
        text = 'This is a test with special characters ![alt text with special characters !@#$%^&*](image.jpeg)'
        images = extract_markdown_images(text)
        self.assertEqual(len(images), 1)
        self.assertEqual(images[0][0], 'alt text with special characters !@#$%^&*')
        self.assertEqual(images[0][1], 'image.jpeg')

    def test_with_spaces(self):
        text = 'This is a test with spaces between ![alt text] (image.jpg)'
        images = extract_markdown_images(text)
        self.assertEqual(len(images), 1)
        self.assertEqual(images[0][0], 'alt text')
        self.assertEqual(images[0][1], 'image.jpg')

    def test_with_nested_brackets(self):
        text = 'This is a test with nested brackets ![alt text [with brackets]](image.jpg)'
        images = extract_markdown_images(text)
        self.assertEqual(len(images), 1)
        self.assertEqual(images[0][0], 'alt text [with brackets]')
        self.assertEqual(images[0][1], 'image.jpg')

    def test_with_nested_parantheses(self):
        text = 'This is a test with nested parantheses ![alt text (with parantheses)](image.jpg)'
        images = extract_markdown_images(text)
        self.assertEqual(len(images), 1)
        self.assertEqual(images[0][0], 'alt text (with parantheses)')
        self.assertEqual(images[0][1], 'image.jpg')

    def test_with_nested_brackets_in_image(self):
        text = 'This is a test with nested brackets in image ![alt text](image[with brackets].jpg)'
        images = extract_markdown_images(text)
        self.assertEqual(len(images), 1)
        self.assertEqual(images[0][0], 'alt text')
        self.assertEqual(images[0][1], 'image[with brackets].jpg')

    def test_with_nested_parantheses_in_image(self):
        text = 'This is a test with nested parantheses in image ![alt text](image(with parantheses).jpg)'
        images = extract_markdown_images(text)
        self.assertEqual(len(images), 1)
        self.assertEqual(images[0][0], 'alt text')
        self.assertEqual(images[0][1], 'image(with parantheses).jpg')


class TestSplitNodesImage(unittest.TestCase):
    def test_basic_function(self):
        node = TextNode('This is a test with an image ![alt text](image.jpg)', 'text')
        new_nodes = split_nodes_image([node])
        self.assertEqual(len(new_nodes), 2)
        self.assertEqual(new_nodes[0].text, 'This is a test with an image ')
        self.assertEqual(new_nodes[1].text, 'alt text')
        self.assertEqual(new_nodes[1].text_type, 'image')
        self.assertEqual(new_nodes[1].url, 'image.jpg')

    def test_with_multi_images(self):
        node = TextNode('This is a test with an image ![alt text](image.jpg) and another ![alt text](image2.jpg)', 'text')
        new_nodes = split_nodes_image([node])
        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0].text, 'This is a test with an image ')
        self.assertEqual(new_nodes[1].text, 'alt text')
        self.assertEqual(new_nodes[1].text_type, 'image')
        self.assertEqual(new_nodes[1].url, 'image.jpg')
        self.assertEqual(new_nodes[2].text, ' and another ')
        self.assertEqual(new_nodes[3].text, 'alt text')
        self.assertEqual(new_nodes[3].text_type, 'image')
        self.assertEqual(new_nodes[3].url, 'image2.jpg')

    def test_no_images(self):
        node = TextNode('This is a test with no images', 'text')
        new_nodes = split_nodes_image([node])
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, 'This is a test with no images')

    def test_with_special_characters1(self):
        node = TextNode('This is a test with an image ![alt text with spaces](image.jpg)', 'text')
        new_nodes = split_nodes_image([node])
        self.assertEqual(len(new_nodes), 2)
        self.assertEqual(new_nodes[0].text, 'This is a test with an image ')
        self.assertEqual(new_nodes[1].text, 'alt text with spaces')
        self.assertEqual(new_nodes[1].text_type, 'image')
        self.assertEqual(new_nodes[1].url, 'image.jpg')

    def test_with_special_characters2(self):
        node = TextNode('This is a test with an image ![alt text with spaces](image with spaces.jpg)', 'text')
        new_nodes = split_nodes_image([node])
        self.assertEqual(len(new_nodes), 2)
        self.assertEqual(new_nodes[0].text, 'This is a test with an image ')
        self.assertEqual(new_nodes[1].text, 'alt text with spaces')
        self.assertEqual(new_nodes[1].text_type, 'image')
        self.assertEqual(new_nodes[1].url, 'image with spaces.jpg')

    def test_with_special_characters3(self):
        node = TextNode('This is a test with special characters ![alt text with special characters !@#$%^&*](image.jpeg)', 'text')
        new_nodes = split_nodes_image([node])
        self.assertEqual(len(new_nodes), 2)
        self.assertEqual(new_nodes[0].text, 'This is a test with special characters ')
        self.assertEqual(new_nodes[1].text, 'alt text with special characters !@#$%^&*')
        self.assertEqual(new_nodes[1].text_type, 'image')
        self.assertEqual(new_nodes[1].url, 'image.jpeg')

class TestSplitNodesLink(unittest.TestCase):
    def test_basic_function(self):
        node = TextNode('This is a test with a link [alt text](https://bootdev.com)', 'text')
        new_nodes = split_nodes_link([node])
        self.assertEqual(len(new_nodes), 2)
        self.assertEqual(new_nodes[0].text, 'This is a test with a link ')
        self.assertEqual(new_nodes[1].text, 'alt text')
        self.assertEqual(new_nodes[1].text_type, 'link')
        self.assertEqual(new_nodes[1].url, 'https://bootdev.com')


if __name__ == "__main__":
    unittest.main()