import unittest

from htmlnode import LeafNode

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