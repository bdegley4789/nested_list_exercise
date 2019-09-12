import random
import time
import unittest
import nested_lists

class nested_lists_tests(unittest.TestCase):

    # Description: Test flatten list if the size of the list is 0
    # Creator: Bryce Egley
    def test_flatten_list_size_0(self):
        input = []
        actual_item = nested_lists.flatten(input)
        expected_item = []
        self.assertEqual(actual_item, expected_item)

    # Description: Test flatten list if the size of the list is 1
    # Creator: Bryce Egley
    def test_flatten_list_size_1(self):
        input = [5]
        actual_item = nested_lists.flatten(input)
        expected_item = [5]
        self.assertEqual(actual_item, expected_item)

    # Description: Test flatten list is just a nested listed but there are no integers
    # Creator: Bryce Egley
    def test_flatten_list_empty_nested(self):
        input = [[[[]]]]
        actual_item = nested_lists.flatten(input)
        expected_item = []
        self.assertEqual(actual_item, expected_item)

    # Description: Test flatten list if the size of the list is 5 and there is lots of nesting
    # Creator: Bryce Egley
    def test_flatten_list_size_5(self):
        input = [[4, 3, 4, 1, [[1, 3, 5, 0, 4], 2, 1, [2, 5, [3, 2, 2, 5, [[4, 2, 0, 0, 4], 5, 4, 4, [1, 3, [[1, 3, 5, 4, 0], 0, 0, 2, 1], 2, 5]]], [1, [4, 0, 3, 3, [1, 2, 4, [5, [4, 0, [5, 1, 1, 1, 3], 5, 2], 2, 4, 2], 2]], 2, 3, 3], 4], 1]], 0, 5, [1, 1, 1, 3, 0], 1]
        actual_item = nested_lists.flatten(input)
        expected_item = [4, 3, 4, 1, 1, 3, 5, 0, 4, 2, 1, 2, 5, 3, 2, 2, 5, 4, 2, 0, 0, 4, 5, 4, 4, 1, 3, 1, 3, 5, 4, 0, 0, 0, 2, 1, 2, 5, 1, 4, 0, 3, 3, 1, 2, 4, 5, 4, 0, 5, 1, 1, 1, 3, 5, 2, 2, 4, 2, 2, 2, 3, 3, 4, 1, 0, 5, 1, 1, 1, 3, 0, 1]
        self.assertEqual(actual_item, expected_item)

    # Description: Test flatten list if the size of the list is 20 and only a little nesting
    # Creator: Bryce Egley
    def test_flatten_list_size_20(self):
        input = [6, 3, 16, 10, 1, 14, 11, 4, 15, 13, 14, 11, 7, 8, 14, [1, 2, 8, 19, 1, 16, 12, 3, 1, [16, 10, 10, 20, 14, 10, 19, 12, 18, 9, 13, 8, 19, 5, 10, 4, 13, 15, 12, 9], 11, 15, 20, 2, 16, 17, 15, 19, 8, 20], 3, 19, 18, 7]
        actual_item = nested_lists.flatten(input)
        expected_item = [6, 3, 16, 10, 1, 14, 11, 4, 15, 13, 14, 11, 7, 8, 14, 1, 2, 8, 19, 1, 16, 12, 3, 1, 16, 10, 10, 20, 14, 10, 19, 12, 18, 9, 13, 8, 19, 5, 10, 4, 13, 15, 12, 9, 11, 15, 20, 2, 16, 17, 15, 19, 8, 20, 3, 19, 18, 7]
        self.assertEqual(actual_item, expected_item)

if __name__ == '__main__':
    unittest.main()
