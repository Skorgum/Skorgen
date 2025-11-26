import unittest
from textnode import TextNode, TextType
from extract_images_and_links import extract_markdown_images, extract_markdown_links

class TestExtract(unittest.TestCase):
    def test_extract_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.google.com)"
        )
        self.assertEqual([("link", "https://www.google.com")], matches)