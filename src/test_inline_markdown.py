import unittest

from inline_markdown import *

class TestDelimiter(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )
    
    def test_bold(self):
        node = TextNode("This is text with a **bold** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bold", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_italic(self):
        node = TextNode("This is text with a *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_double_bold(self):
        node = TextNode("This is text with a **bold** word and **another**", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bold", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_bold)
            ],
            new_nodes,
        )

    def test_bold_multiword(self):
        node = TextNode("This is text with a **bold word** and **another**", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bold word", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("another", text_type_bold)
            ],
            new_nodes,
        )

class TestRegex(unittest.TestCase):
    def test_img(self):
        text = extract_markdown_images("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)")
        self.assertEqual(text, [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png")])

    def test_link(self):
        text = extract_markdown_links(text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)")
        self.assertEqual(text, [("link", "https://www.example.com"), ("another", "https://www.example.com/another")])

class TestSplitImageLinks(unittest.TestCase):
    def test_img(self):
        images = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            text_type_text,
        )
        new_images = split_nodes_image([images])
        self.assertListEqual(new_images, [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and another ", text_type_text),
                TextNode("second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png")
            ])
        
    def test_links(self):
        links = TextNode(
            "This is text with a [link](https://example.com/link1) and another [second link](https://example.com/link2).",
            text_type_text,
        )
        new_links = split_nodes_link([links])
        self.assertListEqual(new_links, [
                TextNode("This is text with a ", text_type_text),
                TextNode("link", text_type_link, "https://example.com/link1"),
                TextNode(" and another ", text_type_text),
                TextNode("second link", text_type_link, "https://example.com/link2"),
                TextNode(".", text_type_text)
            ])
        
    def test_no_img(self):
        no_images = TextNode(
            "This is text without any images.", 
            text_type_text,
        )
        new_no_images = split_nodes_image([no_images])
        self.assertListEqual(new_no_images, [
                TextNode("This is text without any images.", text_type_text)
            ])
        
    def test_no_links(self):
        no_links = TextNode(
            "This is text without any links.", 
            text_type_text,
        )
        new_no_links = split_nodes_link([no_links])
        self.assertListEqual(new_no_links, [
                TextNode("This is text without any links.", text_type_text)
            ])
    
    def test_text_to_textnodes(self):
        nodes = text_to_textnodes(
            "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word and a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
            ],
            nodes,
        )

        
    

if __name__ == "__main__":
    unittest.main()

