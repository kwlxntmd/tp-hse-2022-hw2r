def get_data_from_file(file_path: str):
    with open(file_path, encoding='utf-8') as file:
        data = file.readline().strip()
    return data


def get_tuple_of_numbers(data: str):
    tuple_of_numbers = None
    try:
        tuple_of_numbers = tuple(int(i) for i in data.split())
    except ValueError:
        print("Incorrect file data")
    return tuple_of_numbers


def _min(data: tuple):
    try:
        result = data[0]
        for i in range(1, len(data)):
            if data[i] < result:
                result = data[i]
        return result
    except IndexError:
        print("Can't find minimum value: Empty File")


def _max(data: tuple):
    try:
        result = data[0]
        for i in range(1, len(data)):
            if data[i] > result:
                result = data[i]
        return result
    except IndexError:
        print("Can't find maximum value: Empty File")


def _sum(data: tuple):
    result = 0
    for i in data:
        result += i
    return result


def _mult(data: tuple):
    result = 1
    for i in data:
        result *= i
    return result


def calculate_data(file_path: str):
    data = get_tuple_of_numbers(get_data_from_file(file_path))
    return _min(data), _max(data), _sum(data), _mult(data)


if __name__ == '__main__':
    _FILE_PATH = 'numbers.txt'
    min_, max_, sum_, mult_ = calculate_data(_FILE_PATH)
    print(
        "Минимальное число: " + str(min_),
        "Максимальное число: " + str(max_),
        "Сумма чисел: " + str(sum_),
        "Произведение чисел: " + str(mult_),
        sep="\n"
    )
