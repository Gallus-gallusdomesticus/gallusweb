import unittest
from extractlinks import extract_markdown_images, extract_markdown_links

class TestExtractLinks(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and [links](https://www.boot.dev)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_empty_markdown_images(self):
        matches = extract_markdown_images(
            "Image with no alt text: ![](https://example.com/image.png)"
        )
        self.assertListEqual([("", "https://example.com/image.png")], matches)

    def test_empty_url_images(self):
        matches = extract_markdown_images(
            "Image with no URL: ![alt text]()"
        )
        self.assertListEqual([("alt text", "")], matches)

    def test_broken_images(self):
        matches = extract_markdown_images(
            "This is broken syntax: ![alt text](missing-parenthesis"
        )
        self.assertListEqual([], matches)
    
    def test_nested_square_images(self):
        matches = extract_markdown_images(
            "Nested brackets: ![Some [nested]](https://example.com)"
        )
        self.assertListEqual([("Some [nested]", "https://example.com")], matches)
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [links](https://www.boot.dev) and ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("links", "https://www.boot.dev")], matches)

    def test_nested_square_links(self):
        matches = extract_markdown_links(
            "Nested brackets: [Some [nested]](https://example.com)"
        )
        self.assertListEqual([("Some [nested]", "https://example.com")], matches)
        