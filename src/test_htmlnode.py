import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "This is text inside a paragraph", None, {"href": "https://www.google.com", "target": "_blank"})
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://www.google.com" target="_blank"')
        
    def test_props_to_html_without_props(self):
        node = HTMLNode("p", "This is text inside a paragraph")
        result = node.props_to_html()
        self.assertEqual(result, '')

    def test_props_to_html_with_empty_props(self):
        node = HTMLNode("p", "This is text inside a paragraph", None, {})
        result = node.props_to_html()
        self.assertEqual(result, "")

    def test_repr(self):
        node = HTMLNode("p", "This is text inside a paragraph", None, {"href": "https://www.google.com", "target": "_blank"})
        result = repr(node)
        expected = "HTMLNode('p', 'This is text inside a paragraph', [], {'href': 'https://www.google.com', 'target': '_blank'})"
        self.assertEqual(result, expected)

    def test_repr_with_children(self):
        child_node = HTMLNode("span", "child text")
        node = HTMLNode("p", "This is text inside a paragraph", [child_node], {"class": "text-muted"})
        result = repr(node)
        expected = "HTMLNode('p', 'This is text inside a paragraph', [HTMLNode('span', 'child text', [], None)], {'class': 'text-muted'})"
        self.assertEqual(result, expected)

    def test_node_without_tag(self):
        node = HTMLNode(value="This is text inside a tagless node")
        result = repr(node)
        expected = "HTMLNode(None, 'This is text inside a tagless node', [], None)"
        self.assertEqual(result, expected)

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

class TestLeafNode(unittest.TestCase):
    def test_tag(self):
        node = LeafNode("p", "This is a paragraph of text.")
        result = node.to_html()
        expected_result = "<p>This is a paragraph of text.</p>"
        self.assertEqual(result, expected_result)

    def test_no_tag(self):
        node = LeafNode(None, "This is a paragraph of text.")
        result = node.to_html()
        expected_result = "This is a paragraph of text."
        self.assertEqual(result, expected_result)

    def test_value(self):
        node = LeafNode("p", None, {"href": "https://www.google.com"})
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "The 'value' parameter is required for LeafNode")

    def test_empty_value(self):
        node = LeafNode("p", "", {"class": "text"})
        result = node.to_html()
        expected_result = '<p class="text"></p>'
        self.assertEqual(result, expected_result)

    def test_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        result = node.to_html()
        expected_result = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(result, expected_result)

    def test_no_tag_with_props(self):
        node = LeafNode(None, "This is a paragraph of text.", {"class": "text"})
        result = node.to_html()
        expected_result = "This is a paragraph of text."
        self.assertEqual(result, expected_result)

    def test_props_with_multiple_attributes(self):
        node = LeafNode("a", "This is a paragraph of text.", {"class": "text", "id": "button", "href": "https://www.google.com"})
        result = node.to_html()
        expected_result = '<a class="text" id="button" href="https://www.google.com">This is a paragraph of text.</a>'
        self.assertEqual(result, expected_result)

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

if __name__ == "__main__":
    unittest.main()