import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a html node", None, None)
        node2 = HTMLNode("p", "This is a html node", None, None)
        self.assertEqual(node, node2)

    def test_eq2(self):
        children = [
            HTMLNode("span", "Child Text", None, None),
            HTMLNode("a", "Click me!", None, {"href": "https://example.com"})
        ]
        props = {"class": "my-class"}

        node = HTMLNode("p", "This is a html node", children, props)
        node2 = HTMLNode("p", "This is a html node", children, props)
        self.assertEqual(node, node2)
    
    def test_neq(self):
        children1 = [
            HTMLNode("span", "Child 1", None, None),
            HTMLNode("a", "Click here", None, {"href": "https://example.com"})
        ]
        children2 = [
            HTMLNode("span", "Different Child", None, None),
            HTMLNode("a", "Visit me!", None, {"href": "https://different.com"})
        ]
        props1 = {"class": "first-class"}
        props2 = {"id": "unique-id"}

        node1 = HTMLNode("p", "This is the first node", children1, props1)
        node2 = HTMLNode("p", "This is the second node", children2, props2)

        self.assertNotEqual(node1, node2)

    def test_repr(self):
        # Create a node with all attributes specified
        children = [
            HTMLNode("span", "Child Text", None, None),
            HTMLNode("a", "Click me!", None, {"href": "https://example.com"})
        ]
        props = {"class": "my-class"}
        node = HTMLNode("div", "Parent Text", children, props)

        # What should `repr(node)` output? Based on your `__repr__` method:
        expected_repr = ("HTMLNode(div, Parent Text, "
                         "[HTMLNode(span, Child Text, [], {}), "
                         "HTMLNode(a, Click me!, [], {'href': 'https://example.com'})], "
                         "{'class': 'my-class'})")

        # Assert that the actual repr string matches the expected one
        self.assertEqual(repr(node), expected_repr)
 


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_all(self):
        node = LeafNode("a","Hello man!",{"href": "https://test.com", "testing": "http://testing123.com"})
        self.assertEqual(node.to_html(), '<a href="https://test.com" testing="http://testing123.com">Hello man!</a>')





if __name__ == "__main__":
    unittest.main()
