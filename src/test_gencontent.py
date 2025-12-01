import unittest
from gencontent import extract_title, generate_page

class TestGencontent(unittest.TestCase):
    def test_extract_title(self):
        md = "# Title"
        title_text = extract_title(md)
        self.assertEqual(title_text, "Title")

    def test_title_with_spaces(self):
        md = "#  Title  "
        title_text = extract_title(md)
        self.assertEqual(title_text, "Title")

    def test_buried_title(self):
        md = """
Intro text
# Actual Title
Outro text
"""
        title_text = extract_title(md)
        self.assertEqual(title_text, "Actual Title")

    def test_no_hash(self):
        md = "Title"
        with self.assertRaises(Exception):
            extract_title(md)

    def test_generate_page(self):  
        with open("test_markdown.md", "w") as f:
            f.write("# Test Title\n\n**bold**")
        with open("test_template.html", "w") as f:
            f.write("<html><head><title>{{ Title }}</title></head><body>{{ Content }}</body></html>")
        generate_page("test_markdown.md", "test_template.html", "test_output.html")
        with open("test_output.html") as f:
            output = f.read()
        self.assertIn("Test Title", output)
        self.assertIn("<html>", output)

if __name__ == "__main__":
    unittest.main()