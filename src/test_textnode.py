import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_not_eq_different_url(self):
        node_a = TextNode("hello", TextType.BOLD)
        node_b = TextNode("hello", TextType.BOLD, url="https://example.com")
        self.assertNotEqual(node_a, node_b)
    def test_not_eq_different_text(self):
        node_c = TextNode("hello", TextType.ITALIC)
        node_d = TextNode("goodbye", TextType.ITALIC)
        self.assertNotEqual(node_c, node_d)
    def test_not_eq_different_text_type(self):
        node_e = TextNode("hello", TextType.BOLD)
        node_f = TextNode("hello", TextType.ITALIC)
        self.assertNotEqual(node_e, node_f)
    def test_eq_all(self):
        node_g = TextNode("test", TextType.BOLD, url="https://example.com")
        node_h = TextNode("test", TextType.BOLD, url="https://example.com")
        self.assertEqual(node_g, node_h)


if __name__ == "__main__":
    unittest.main()