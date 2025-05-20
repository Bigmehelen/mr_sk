import categorizetwo
from unittest import TestCase

class TestCategorize(TestCase):

	def test_that_get_categorize_function_exists(self):
		categorizetwo.get_categorize(1)

	def test_that_get_categorise_return_input_as_result(self):
		actual = categorizetwo.get_categorize(10,15,21,30,45)
		expected = [10,15,30,45]
		self.assertEqual(actual, expected)

	def test_that_get_categorise_return_no_number_found(self):
		actual = categorizetwo.get_categorize(41,13,17,31,22)
		expected = 'No divisible numbers found'
		self.assertEqual(actual, expected)
