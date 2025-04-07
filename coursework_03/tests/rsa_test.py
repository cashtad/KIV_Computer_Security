import unittest

from coursework_03 import rsa


class MyTestCase(unittest.TestCase):
    def test_readfile(self):
        filename = "customers-20.csv"
        data = rsa.read_plain_text(filename)


if __name__ == '__main__':
    unittest.main()
