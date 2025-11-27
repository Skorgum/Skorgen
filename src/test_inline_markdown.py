import unittest
from inline_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
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

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_no_images(self):
        node = TextNode(
            "This is text with no images",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with no images", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_image_at_start(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) with text after",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" with text after", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_image_at_end(self):
        node = TextNode(
            "There is no text after ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("There is no text after ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://www.google.com) and [another](https://www.boot.dev)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.google.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.LINK, "https://www.boot.dev"),
            ],
            new_nodes, 
        )

    def test_no_links(self):
        node = TextNode(
            "This is text with no links",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with no links", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_link_at_start(self):
        node = TextNode(
            "[link](https://www.google.com) with text after",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://www.google.com"),
                TextNode(" with text after", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_link_at_end(self):
        node = TextNode(
            "There is no text after [link](https://www.google.com)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("There is no text after ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.google.com"),
            ],
            new_nodes,
        )

    def test_image_and_link(self):
        node = TextNode(
            "This is an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://www.google.com)",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        new_nodes = split_nodes_link(new_nodes)
        self.assertListEqual(
            [
                TextNode("This is an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.google.com"),
            ],
            new_nodes,
        )

    def test_text_to_textnode(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            new_nodes,
        )
    
    def test_no_markdown(self):
        text = "This is text with no markdown"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is text with no markdown", TextType.TEXT),
            ],
            new_nodes,
        )
    
    def test_multiple_bold(self):
        text = "This is **bold** text because I **love bold**"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text because I ", TextType.TEXT),
                TextNode("love bold", TextType.BOLD),
            ],
            new_nodes,
        )

    def text_no_text(self):
        text = ""
        new_nodes = text_to_textnodes(text)
        self.assertEqual(
            [],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()