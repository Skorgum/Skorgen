import unittest
from markdown_blocks import markdown_to_blocks, BlockType, block_to_block_type

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_blocktype_heading1(self):
        block = "# This is a heading"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.HEADING)

    def test_block_to_blocktype_heading6(self):
        block = "###### This is a heading"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.HEADING)

    def test_block_to_blocktype_heading_too_many_hashes(self):
        block = "####### This is not a heading"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.PARAGRAPH)

    def test_block_to_blocktype_heading_no_space(self):
        block = "#This is not a heading"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.PARAGRAPH)

    def test_block_to_blocktype_code_missing_closing(self):
        block = "```\nThis is a code block\n"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.PARAGRAPH)

    def test_block_to_blocktype_code(self):
        block = "```\nThis is a code block\n```"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.CODE)

    def test_block_to_blocktype_quote(self):
        block = ">This is a quote block\n>with multiple lines"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.QUOTE)
    
    def test_block_to_blocktype_quote_missing_char(self):
        block = ">This is a quote line\nThis is not"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.PARAGRAPH)

    def test_block_to_blocktype_unordered_list(self):
        block = "- first\n- second\n- third"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.UNORDERED_LIST)

    def test_block_to_blocktype_unordered_list_bad_line(self):
        block = "- first\n-second\n- third"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.PARAGRAPH)

    def test_block_to_blocktype_ordered_list(self):
        block = "1. first\n2. second\n3. third"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.ORDERED_LIST)

    def test_block_to_blocktype_ordered_list_missing_item(self):
        block = "1. first\n3. third\n4. fourth"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.PARAGRAPH)

    def test_block_to_blocktype_ordered_list_missing_space(self):
        block = "1. first\n2.second\n3. third"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.PARAGRAPH)

    def test_block_to_blocktype_paragraph(self):
        block = "This is just some text with no markdown"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.PARAGRAPH)