import unittest
from coursework_02 import decoder


class MyTestCase(unittest.TestCase):
    def test_shiftrows(self):
        matrix = [[1, 2, 3, 4], [8, 5, 6, 7], [11, 12, 9, 10], [14, 15, 16, 13]]
        # Проверка правильности сложения
        self.assertEqual(decoder.inv_shiftrows(matrix), [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]] )

    def test_subbytes(self):
        matrix =  [[0x23,0x1a,0x42, 0xc2], [0xc4,0xbe,0x04, 0x5d], [0xc7,0xc7,0x46, 0x3a],[0xe1,0x9a,0xc5, 0x18]]
        matrix_control =  [[0x32,0x43,0xF6, 0xA8],[0x88,0x5A,0x30,0x8D],[0x31,0x31,0x98,0xA2],[0xE0,0x37,0x07,0x34]]
        self.assertEqual(decoder.inv_subbytes(matrix), matrix_control)

    def test_mixcolumns(self):
        # Пример входной матрицы состояния (state)
        expected_result = [
            [0x63, 0xf2, 0x01, 0xc6],
            [0x47, 0x0a, 0x01, 0xc6],
            [0xa2, 0x22, 0x01, 0xc6],
            [0xf0, 0x5c, 0x01, 0xc6]
        ]

        # Ожидаемый результат после применения mixcolumns
        state = [
            [0x5d, 0x9f, 0x01, 0xc6],
            [0xe0, 0xdc, 0x01, 0xc6],
            [0x70, 0x58, 0x01, 0xc6],
            [0xbb, 0x9d, 0x01, 0xc6]
        ]

        # Применяем mixcolumns к состоянию
        result = decoder.inv_mixcolumns(state)

        # Проверяем, что результат совпадает с ожидаемым
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
