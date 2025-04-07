import unittest

from coursework_03 import coder


class MyTestCase1(unittest.TestCase):
    def test_generate_numbers_test(self):
        filename = "customers-20.csv"
        data = coder.generate_numbers()


if __name__ == '__main__':
    unittest.main()
