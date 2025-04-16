import unittest
from main import sum_lists

class TestSumLists(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(sum_lists([1, 2, 3], [4, 5, 6]), [5, 7, 9])

    def test_with_negatives(self):
        self.assertEqual(sum_lists([-1, -2], [1, 2]), [0, 0])

    def test_with_zeros(self):
        self.assertEqual(sum_lists([0, 0], [0, 0]), [0, 0])

    def test_error_on_different_lengths(self):
        with self.assertRaises(ValueError):
            sum_lists([1, 2], [1])

if __name__ == '__main__':
    unittest.main()
