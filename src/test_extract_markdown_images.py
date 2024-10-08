import unittest
from delimiter import extract_markdown_images


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

    