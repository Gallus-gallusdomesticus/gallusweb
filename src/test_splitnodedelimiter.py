import unittest

from textnode import TextNode, TextType
from splitnodedelimiter import split_nodes_delimiter, split_nodes_image, split_nodes_links


class TestSplitNodeDelimiter(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" word", TextType.TEXT)
        ]
    
        self.assertEqual(len(new_nodes), len(expected))
        for i in range(len(new_nodes)):
            self.assertEqual(new_nodes[i].text, expected[i].text)
            self.assertEqual(new_nodes[i].text_type, expected[i].text_type)


    def test_just_plain_text(self):
        node = TextNode("Just plain text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [TextNode("Just plain text", TextType.TEXT)]

        self.assertEqual(len(new_nodes), len(expected))
        for i in range(len(new_nodes)):
            self.assertEqual(new_nodes[i].text, expected[i].text)
            self.assertEqual(new_nodes[i].text_type, expected[i].text_type)

    def test_multiple_delimiter(self):
        node = TextNode("Text with `code` and `more code` examples", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected= [TextNode("Text with ", TextType.TEXT), 
        TextNode("code", TextType.CODE),
        TextNode(" and ", TextType.TEXT),
        TextNode("more code", TextType.CODE),
        TextNode(" examples", TextType.TEXT)
        ]

        self.assertEqual(len(new_nodes), len(expected))
        for i in range(len(new_nodes)):
            self.assertEqual(new_nodes[i].text, expected[i].text)
            self.assertEqual(new_nodes[i].text_type, expected[i].text_type)

    def test_non_text(self):
        node = TextNode("Bold text", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [TextNode("Bold text", TextType.BOLD)]

        self.assertEqual(len(new_nodes), len(expected))
        for i in range(len(new_nodes)):
            self.assertEqual(new_nodes[i].text, expected[i].text)
            self.assertEqual(new_nodes[i].text_type, expected[i].text_type)


    def test_unpaired_delimiter(self):
        node = TextNode("Text with `unpaired delimiter", TextType.TEXT)

        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)
    


#Test split node image

class TestSplitNodeImage(unittest.TestCase):
    def test_sample(self):
        node = TextNode(
        "This is text with a image ![image1](https://www.boot.dev/image) and ![image2](https://www.youtube.com/@bootdotdev/image)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected= [
        TextNode("This is text with a image ", TextType.TEXT),
        TextNode("image1", TextType.IMAGES, "https://www.boot.dev/image"),
        TextNode(" and ", TextType.TEXT),
        TextNode("image2", TextType.IMAGES, "https://www.youtube.com/@bootdotdev/image"),]

        self.assertEqual(len(new_nodes), len(expected))
        for i in range(len(new_nodes)):
            self.assertEqual(new_nodes[i].text, expected[i].text)
            self.assertEqual(new_nodes[i].text_type, expected[i].text_type)

    def test_mixed(self):
        node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and image ![image2](https://www.youtube.com/@bootdotdev/image)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected= [
        TextNode("This is text with a link [to boot dev](https://www.boot.dev) and image ", TextType.TEXT),
        TextNode("image2", TextType.IMAGES, "https://www.youtube.com/@bootdotdev/image"),
        ]



class TestSplitNodeLink(unittest.TestCase):
    def test_sample(self):
        node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_links([node])
        expected= [
        TextNode("This is text with a link ", TextType.TEXT),
        TextNode("to boot dev", TextType.LINKS, "https://www.boot.dev"),
        TextNode(" and ", TextType.TEXT),
        TextNode("to youtube", TextType.LINKS, "https://www.youtube.com/@bootdotdev")]

        self.assertEqual(len(new_nodes), len(expected))
        for i in range(len(new_nodes)):
            self.assertEqual(new_nodes[i].text, expected[i].text)
            self.assertEqual(new_nodes[i].text_type, expected[i].text_type)

    def test_mixed(self):
        node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and image ![image2](https://www.youtube.com/@bootdotdev/image)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_links([node])
        expected= [
        TextNode("This is text with a link ", TextType.TEXT),
        TextNode("to boot dev", TextType.LINKS, "https://www.boot.dev"),
        TextNode(" and image ![image2](https://www.youtube.com/@bootdotdev/image)", TextType.TEXT),
        ]

        self.assertEqual(len(new_nodes), len(expected))
        for i in range(len(new_nodes)):
            self.assertEqual(new_nodes[i].text, expected[i].text)
            self.assertEqual(new_nodes[i].text_type, expected[i].text_type)


if __name__ == "__main__":
    unittest.main()