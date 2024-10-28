import unittest
from main import _min, _max, _sum, _mult, get_tuple_of_numbers


class MyTestCase(unittest.TestCase):
    """
    Проверка вспомогательных функций модуля main
    """
    def setUp(self):
        self.test_tuple = (1, 2, 3, 4, 5)
        self.test_str = '1 2 3 4 5'
        self.min_answer = 1
        self.max_answer = 5
        self.sum_answer = 15
        self.mult_answer = 120

    def test_min(self):
        """
        Тестирование функции main._min
        """
        self.assertEqual(_min(self.test_tuple), self.min_answer)

    def test_max(self):
        """
        Тестирование функции main._max
        """
        self.assertEqual(_max(self.test_tuple), self.max_answer)

    def test_sum(self):
        """
        Тестирование функции main._sum
        """
        self.assertEqual(_sum(self.test_tuple), self.sum_answer)

    def test_mult(self):
        """
        Тестирование функции main._mult
        """
        self.assertEqual(_mult(self.test_tuple), self.mult_answer)

    def test_tuple_of_numbers(self):
        """
        Тестирование функции main.get_tuple_of_numbers
        дополнительный тест
        """
        tuple_of_numbers = get_tuple_of_numbers(self.test_str)
        self.assertIsInstance(tuple_of_numbers, tuple)
        self.assertTupleEqual(tuple_of_numbers, self.test_tuple)


if __name__ == '__main__':
    unittest.main()
