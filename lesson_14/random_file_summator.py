import random
import logging


def create_files():
    for i in range(1, 11):
        file_content = '\n'.join(str(num) for num in random.sample(range(-1000, 1000), 3))
        with open(f'{i}.txt', 'w') as file:
            file.write(file_content)


def read_n_sum(first_num, second_num):
    final_arr = []
    for file_num in [first_num, second_num]:
        file_path = f'{file_num}.txt'
        content = read_file(file_path)
        logging.info(f"Открыт файл {file_path}, содержимое: {content}")

        if not isinstance(content, list) or len(content) != 3:
            raise ValueError(f'Ошибка в файле {file_path}: Неверное количество чисел')

        content = convert_nums(content)
        final_arr.extend(content)
    return sum(final_arr)


def read_file(path):
    try:
        with open(path, 'r') as file:
            return file.read().strip().split('\n')
    except Exception as e:
        logging.error(f"Ошибка при открытии файла {path}: {e}")
        raise


def convert_nums(content):
    try:
        return [int(num) for num in content]
    except ValueError as e:
        logging.error(f"Ошибка преобразования данных: {e}")
        raise


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    create_files()
    two_random_nums = random.sample(range(1, 11), 2)
    try:
        result = read_n_sum(two_random_nums[0], two_random_nums[1])
        print(f"Сумма чисел: {result}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
