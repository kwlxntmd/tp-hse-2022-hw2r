import time
import unittest

import matplotlib.pyplot as plt

from main import calculate_data, _min, _max, _sum, _mult, \
    get_data_from_file, get_tuple_of_numbers
from file_generator import FILE_DIR_ABSOLUTE_PATH, MIN_NUM, MAX_NUM, \
    generate_files_by_tuple


class TestTimeSpentCalcFunction(unittest.TestCase):
    """
    Проверка функций main.calculate_data
    с фиксированием времени работы теста и
    построением результирующего графика
    """

    @classmethod
    def setUpClass(cls):
        generate_files_by_tuple()
        cls.timer = {}

    @classmethod
    def tearDownClass(cls):
        lists = sorted(cls.timer.items())
        x, y = zip(*lists)
        plt.title(f'Время работы теста для чисел от {MIN_NUM} до {MAX_NUM}')
        plt.xlabel('Количество, млн. чисел')
        plt.ylabel('Время, сек')
        plt.plot(x, y)
        plt.show()

    def setUp(self):
        self.startTime = time.time()
        self.nums_count = None

    def tearDown(self):
        spent_time = time.time() - self.startTime
        spent_time = round(spent_time, 3)
        self.timer[self.nums_count] = spent_time
        print(f'{self.id}: {spent_time}')

    def test_1000_nums(self):
        self.nums_count = 1000
        file_path = f'{FILE_DIR_ABSOLUTE_PATH}/{self.nums_count}.nums'
        result = calculate_data(file_path)
        self.assertIsInstance(result, tuple)

    def test_10000_nums(self):
        self.nums_count = 10000
        file_path = f'{FILE_DIR_ABSOLUTE_PATH}/{self.nums_count}.nums'
        result = calculate_data(file_path)
        self.assertIsInstance(result, tuple)

    def test_100000_nums(self):
        self.nums_count = 100000
        file_path = f'{FILE_DIR_ABSOLUTE_PATH}/{self.nums_count}.nums'
        result = calculate_data(file_path)
        self.assertIsInstance(result, tuple)

    def test_200000_nums(self):
        self.nums_count = 200000
        file_path = f'{FILE_DIR_ABSOLUTE_PATH}/{self.nums_count}.nums'
        result = calculate_data(file_path)
        self.assertIsInstance(result, tuple)

    def test_400000_nums(self):
        self.nums_count = 400000
        file_path = f'{FILE_DIR_ABSOLUTE_PATH}/{self.nums_count}.nums'
        result = calculate_data(file_path)
        self.assertIsInstance(result, tuple)

    def test_800000_nums(self):
        self.nums_count = 800000
        file_path = f'{FILE_DIR_ABSOLUTE_PATH}/{self.nums_count}.nums'
        result = calculate_data(file_path)
        self.assertIsInstance(result, tuple)

    def test_1000000_nums(self):
        self.nums_count = 1000000
        file_path = f'{FILE_DIR_ABSOLUTE_PATH}/{self.nums_count}.nums'
        result = calculate_data(file_path)
        self.assertIsInstance(result, tuple)


class TestTimeSpentSupFunction(unittest.TestCase):
    """
    Проверка вспомогательных функций main.calculate_data
    с фиксированием времени работы теста и
    построением результирующего графика
    """

    @classmethod
    def setUpClass(cls):
        generate_files_by_tuple()
        cls.timer = {}

    @classmethod
    def tearDownClass(cls):
        value_list = list(cls.timer.items())
        tests, times = zip(*value_list)
        times = list(cls.timer.values())
        plt.figure(figsize=(10, 5))
        plt.bar(tests, times, color='maroon', width=0.4)
        plt.xlabel('Тестовая функция')
        plt.ylabel('Время, сек')
        plt.title(f'Время работы тестов вспомогательных функций '
                  f'для чисел от {MIN_NUM} до {MAX_NUM}')
        plt.show()

    def setUp(self):
        self.startTime = time.time()
        self.nums_count = 1000000
        file_path = f'{FILE_DIR_ABSOLUTE_PATH}/{self.nums_count}.nums'
        data_from_file = get_data_from_file(file_path)
        self.nums = get_tuple_of_numbers(data_from_file)

    def tearDown(self):
        spent_time = time.time() - self.startTime
        spent_time = round(spent_time, 3)
        self.timer[self._testMethodName] = spent_time
        print(f'{self.id}: {spent_time}')

    def test_min(self):
        """
        Тестирование функции main._min
        """
        self.assertIsInstance(_min(self.nums), int)

    def test_max(self):
        """
        Тестирование функции main._max
        """
        self.assertIsInstance(_max(self.nums), int)

    def test_sum(self):
        """
        Тестирование функции main._sum
        """
        self.assertIsInstance(_sum(self.nums), int)

    def test_mult(self):
        """
        Тестирование функции main._mult
        """
        self.assertIsInstance(_mult(self.nums), int)


if __name__ == '__main__':
    unittest.main()