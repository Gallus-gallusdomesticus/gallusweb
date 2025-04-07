import unittest
from texttotextnode import text_to_textnodes
from textnode import TextNode, TextType


class TestTextToTextNode(unittest.TestCase):
    def test_text(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        text_node = text_to_textnodes(text)
        expected= [
        TextNode("This is ", TextType.TEXT),
        TextNode("text", TextType.BOLD),
        TextNode(" with an ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word and a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" and an ", TextType.TEXT),
        TextNode("obi wan image", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", TextType.TEXT),
        TextNode("link", TextType.LINKS, "https://boot.dev"),
        ]
        self.assertEqual(len(text_node), len(expected))
        for i in range(len(text_node)):
            self.assertEqual(text_node[i].text, expected[i].text)
            self.assertEqual(text_node[i].text_type, expected[i].text_type)