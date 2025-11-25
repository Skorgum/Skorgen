import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node_with_props = HTMLNode(props={"href": "https://google.com"})
        html_string = node_with_props.props_to_html()
        self.assertEqual(html_string, " href=\"https://google.com\"")
    def test_no_props(self):
        node_with_props = HTMLNode(props=None)
        html_string = node_with_props.props_to_html()
        self.assertEqual(html_string, "")
    def test_empty_props(self):
        node_with_props = HTMLNode(props={})
        html_string = node_with_props.props_to_html()
        self.assertEqual(html_string, "")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, skorgum!")
        self.assertEqual(node.to_html(), "<p>Hello, skorgum!</p>")
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, skorgum!")
        self.assertEqual(node.to_html(), "<a>Hello, skorgum!</a>")
    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, skorgum!")
        self.assertEqual(node.to_html(), "<b>Hello, skorgum!</b>")
    def test_leaf_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    def test_no_tag(self):
        node = LeafNode(None, "I forgot my tag!")
        self.assertEqual(node.to_html(), "I forgot my tag!")
    def test_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
    