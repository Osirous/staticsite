import unittest

from inline_markdown import (
	extract_markdown_images,
	extract_markdown_links,
)

class Test_Extract_Markdown(unittest.TestCase):
	def test_extract_markdown_images(self):
		text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
		expected_output = [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
		self.assertEqual(extract_markdown_images(text), expected_output)

	def test_extract_markdown_links(self):
		text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
		expected_output = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
		self.assertEqual(extract_markdown_links(text), expected_output)