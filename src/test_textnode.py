import unittest
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
    text_node_to_html_node
)
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

        node3 = TextNode("This is the same", "bold")
        node4 = TextNode("This is different", "bold")
        self.assertNotEqual(node3, node4)

    def test_plain_text_conversion(self):
        node = TextNode("Here is some test text", text_type_text)
        expected = LeafNode(None, "Here is some test text")
        result = text_node_to_html_node(node)
        self.assertEqual(result.tag, expected.tag)
        self.assertEqual(result.value, expected.value)
    
    def test_bold_text_conversion(self):
        node = TextNode("Bold text", text_type_bold)
        expected = LeafNode("b", "Bold text")
        result = text_node_to_html_node(node)
        self.assertEqual(result.tag, expected.tag)
        self.assertEqual(result.value, expected.value)
        
    def test_italic_text_conversion(self):
        node = TextNode("Italic text", text_type_italic)
        expected = LeafNode("i", "Italic text")
        result = text_node_to_html_node(node)
        self.assertEqual(result.tag, expected.tag)
        self.assertEqual(result.value, expected.value)
    
    def test_code_text_conversion(self):
        node = TextNode("Code text", text_type_code)
        expected = LeafNode("code", "Code text")
        result = text_node_to_html_node(node)
        self.assertEqual(result.tag, expected.tag)
        self.assertEqual(result.value, expected.value)
    
    def test_link_text_conversion(self):
        node = TextNode("Example", text_type_link, url="http://example.com")
        expected = LeafNode("a", "Example")
        expected.props = {"href": "http://example.com"}
        result = text_node_to_html_node(node)
        self.assertEqual(result.tag, expected.tag)
        self.assertEqual(result.value, expected.value)
        self.assertEqual(result.props, expected.props)

    def test_image_text_conversion(self):
        node = TextNode("Alt text", text_type_image, url="http://example.com/image.png")
        expected = LeafNode("img", "")
        expected.props = {"src": "http://example.com/image.png", "alt": "Alt text"}
        result = text_node_to_html_node(node)
        self.assertEqual(result.tag, expected.tag)
        self.assertEqual(result.value, expected.value)
        self.assertEqual(result.props, expected.props)
        
if __name__ == "__main__":
    unittest.main()
