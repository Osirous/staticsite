import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
	def test_eq(self):
		props = {"href": "https://www.google.com", "target": "_blank"}
		node = HTMLNode(tag="a", props=props)
		expected_output = ' href="https://www.google.com" target="_blank"'
		self.assertEqual(node.props_to_html(), expected_output)

class TestLeafNode(unittest.TestCase):
	def test_leafnode_with_tag_and_value(self):
		node1 = LeafNode("p", "This is some text that would be in a paragraph.")
		self.assertEqual(node1.to_html(), "<p>This is some text that would be in a paragraph.</p>")

	def test_leafnode_with_value_no_tag(self):
		node2 = LeafNode(value="Just some plain text.")
		self.assertEqual(node2.to_html(), "Just some plain text.")

	def test_leafnode_without_value(self):
		with self.assertRaises(ValueError) as context:
			node3 = LeafNode("div")
		self.assertTrue("LeafNode requires a value." in str(context.exception))

class TestParentNode(unittest.TestCase):
	def test_parentnode(self):
		node = ParentNode(
			"p",
			[
				LeafNode("b", "Bold text"),
				LeafNode(None, "Normal text"),
				LeafNode("i", "italic text"),
				LeafNode(None, "Normal text"),
			],
		)
		expected_output = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
		self.assertEqual(node.to_html(), expected_output)
	
	def test_nested_parentnode(self):
		nested_node = ParentNode(
			"div",
			[
				ParentNode(
					"p",
					[
						LeafNode("b", "Bold text"),
						LeafNode(None, "Normal text inside first paragraph."),
					],
				),
				ParentNode(
					"p",
					[
						LeafNode("i", "Italic text"),
						LeafNode(None, "Normal text inside second paragraph."),
					],
				),
			],
		)
		expected_output = (
			"<div>"
			"<p><b>Bold text</b>Normal text inside first paragraph.</p>"
			"<p><i>Italic text</i>Normal text inside second paragraph.</p>"
			"</div>"
		)
		self.assertEqual(nested_node.to_html(), expected_output)

if __name__ == "__main__":
	unittest.main()
