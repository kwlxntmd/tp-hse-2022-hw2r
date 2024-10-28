import os
import random


MIN_NUM = 1
MAX_NUM = 99
FILE_DIR_ABSOLUTE_PATH = '/Users/mac/PycharmProjects/tp-hse-2022-hw2r/test_files'
TUPLE_COUNT_NUMS = (1000, 10000, 100000, 200000, 400000, 800000, 1000000)


def generate_str_of_numbers(count_nums: int):
    """
    Генерирует строку из случайных чисел в определенном количестве.
    :param count_nums: количество чисел в строке.
    :return: срока из чисел разделенных пробелом.
    """
    nums_list = []
    while count_nums > 0:
        nums_list.append(random.randint(MIN_NUM, MAX_NUM))
        count_nums -= 1

    return ' '.join(map(str, nums_list))


def generate_file(count_nums: int):
    """
    Создает файл в который записывает строку из чисел
    :param count_nums: количество чисел
    :return: None
    """
    os.makedirs(FILE_DIR_ABSOLUTE_PATH, exist_ok=True)
    file_name = f'{FILE_DIR_ABSOLUTE_PATH}/{count_nums}.nums'
    with open(file_name, mode='w', encoding="utf-8") as file:
        file.write(generate_str_of_numbers(count_nums))


def _generate_files_by_tuple(tuple_count_nums: tuple):
    """
    Создает файлы в которые записывает строку из чисел.
    :param tuple_count_nums: картеж с количеством чисел.
    :return: None
    """
    for count_nums in tuple_count_nums:
        generate_file(count_nums)


def generate_files_by_tuple():
    """
    Создает файлы в которые записывает строку из чисел
    по кортежу TUPLE_COUNT_NUMS
    :return:
    """
    _generate_files_by_tuple(TUPLE_COUNT_NUMS)


if __name__ == '__main__':
    _generate_files_by_tuple(TUPLE_COUNT_NUMS)
