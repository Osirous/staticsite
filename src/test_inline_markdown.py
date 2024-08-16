import unittest

from inline_markdown import (
	split_nodes_delimiter,
	split_nodes_image,
	split_nodes_link,
	extract_markdown_images,
	extract_markdown_links,
	text_to_textnodes,
)


from textnode import (
	TextNode,
	text_type_text,
	text_type_bold,
	text_type_italic,
	text_type_code,
	text_type_image,
	text_type_link,
)

class TestInline_markdown(unittest.TestCase):
	def test_delimiter_bold(self):
		node = TextNode("This is text with a **bolded** word", text_type_text)
		new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
		self.assertEqual(
			[
				TextNode("This is text with a ", text_type_text),
				TextNode("bolded", text_type_bold),
				TextNode(" word", text_type_text),
			],
			new_nodes,
		)

	def test_delimiter_double_bold(self):
		node = TextNode("This is text with **two** different **bolded** words", text_type_text)
		new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
		self.assertEqual(
			[
				TextNode("This is text with ", text_type_text),
				TextNode("two", text_type_bold),
				TextNode(" different ", text_type_text),
				TextNode("bolded", text_type_bold),
				TextNode(" words", text_type_text),
			],
			new_nodes,
		)

	def test_delimiter_italic(self):
		node = TextNode("This is text with an *italic* word", text_type_text)
		new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
		self.assertEqual(
			[
				TextNode("This is text with an ", text_type_text),
				TextNode("italic", text_type_italic),
				TextNode(" word", text_type_text),
			],
			new_nodes,
		)
	
	def test_delimiter_code(self):
		node = TextNode("This is text with `code block` words", text_type_text)
		new_nodes = split_nodes_delimiter([node], "`", text_type_code)
		self.assertEqual(
			[
				TextNode("This is text with ", text_type_text),
				TextNode("code block", text_type_code),
				TextNode(" words", text_type_text),
			],
			new_nodes,
		)
	
	def test_split_images(self):
		node = TextNode(
			"This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
			text_type_text,
		)
		new_nodes = split_nodes_image([node])
		self.assertEqual(
			[
				TextNode("This is text with an ", text_type_text),
				TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
				TextNode(" and another ", text_type_text),
				TextNode(
					"second image", text_type_image, "https://i.imgur.com/3elNhQu.png"
				),
			],
			new_nodes
		)
	
	def test_text_to_textnode(self):
		text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
		
		expected_nodes = [
        	TextNode("This is ", text_type_text),
    		TextNode("text", text_type_bold),
        	TextNode(" with an ", text_type_text),
        	TextNode("italic", text_type_italic),
        	TextNode(" word and a ", text_type_text),
        	TextNode("code block", text_type_code),
        	TextNode(" and an ", text_type_text),
        	TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
        	TextNode(" and a ", text_type_text),
        	TextNode("link", text_type_link, "https://boot.dev"),
        ]
		
		new_nodes = text_to_textnodes(text)
		self.assertEqual(expected_nodes, new_nodes)