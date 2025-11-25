import unittest

from htmlnode import HTMLNode

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