import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://www.boot.dev", "alt": "This is an image"})
    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

if __name__ == "__main__":
    unittest.main()