import unittest
from inline_markdown import split_nodes_delimiter
from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
    def test_split_bold_simple(self):
        node = TextNode("a **b** c", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "a ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "b")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[2].text, " c")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)

    def test_missing_delim(self):
        node = TextNode("a **b c", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)


if __name__ == "__main__":
    unittest.main()