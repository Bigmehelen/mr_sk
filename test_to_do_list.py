from unittest import TestCase
import to_do_list_manager

class Test_to_do_list(TestCase):

	def test_that_to_do_list_function_exist(self):
		to_do_list_manager.in_main()

	def test_that_to_do_list_function_exist(self):
		actual = to_do_list_manager.in_main(1)
		expected = Add_a_task
		self.assertEqual(actual, expected)
		
		
	def test_that_add_a_task_exist(self):
		to_do_list_manager.add_a_task()
