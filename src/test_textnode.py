import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_neq(self):    
        node3 = TextNode("This is a text node", TextType.LINKS)
        node4 = TextNode("This is a text node", TextType.IMAGES)
        self.assertNotEqual(node3, node4)
        
    def test_neq2(self):   
        node4 = TextNode("This is a text node", TextType.ITALIC, "bootdev.com")
        node5 = TextNode("This is a text node", TextType.ITALIC, "bootdev.co")
        self.assertNotEqual(node4, node5)
        
    def test_eq2(self):    
        node6 = TextNode("This is a text node", TextType.TEXT)
        node7 = TextNode("This is a text node", TextType.TEXT, None)
        self.assertEqual(node6, node7)
    


    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, TEXT, https://www.boot.dev)", repr(node)
        )





if __name__ == "__main__":
    unittest.main()
