import unittest

from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()