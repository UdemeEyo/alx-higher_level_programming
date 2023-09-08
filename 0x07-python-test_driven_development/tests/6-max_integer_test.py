import unittest
max_integer =__import__('6-max_integer').max_integer
class TestmaxInteger(unittest.TestCase):
    def test_max_integer(self):
        """
        It defines the max integer
        """
        test_list = [1,2,3,4,5,6,7,8]
        self.assertEqual(max_integer(test_list), max(test_list))
    def test_max_integer_neg(self):
        """
        It defines the max negative integer 
        """
        test_list = [1,-2,3,-4,5,-6,7,-8]
        self.assertEqual(max_integer(test_list), max(test_list))
    def test_max_integer_empty(self):
        """
        It defines the max integer with an empty list
        """
        test_list = []
        self.assertEqual(max_integer(test_list), None)
