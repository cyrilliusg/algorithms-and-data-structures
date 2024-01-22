import random
import logging


def read_n_sum(first_num, second_num):
    """
    Основной метод.
    Принимает на вход 2 числа, считывает файлы с одноименными названиями и возвращает в них сумму чисел.
    """
    final_arr = []
    for file_name in [first_num, second_num]:
        file_path = f'{file_name}.txt'
        content = read_file(file_path)
        if content is None:  # если произошла ошибка или нет содержимого, то пропустить файл
            continue

        content = content.strip().split('\n')
        logging.info(f"Открыт файл {file_path}, содержимое: {content}")
        try:
            content = validate_numbers_array(content)
        except:
            continue  # если произошла ошибка или нет содержимого, то пропустить файл

        final_arr.extend(content)
    return sum(final_arr)


def read_file(path):
    """
    Метод по считыванию содержимого из файла.
    Принимает на вход путь к файлу и возвращает содержимое в виде строки.
    В случае ошибки считывания возвращает None.
    """
    try:
        with open(path, 'r') as file:
            return file.read()
    except OSError as e:
        logging.error(f"Ошибка при открытии файла {path}: {e}")
        return


def validate_numbers_array(arr, arr_len=3):
    """
    Метод проверяет переданный объект на соответствие требованиям задачи и конвертирует значения в числа.
    """
    if not isinstance(arr, list):
        logging.error(f"Ошибка в типе данных (не список): {arr}")
        raise TypeError("Входные данные не являются списком")

    if len(arr) != arr_len:
        logging.error(f"Не три значения: {arr}")
        raise ValueError("Список должен содержать ровно три элемента")

    result = []
    for item in arr:
        try:
            result.append(int(item))
        except ValueError:
            logging.error(f"Ошибка при конвертации значения {item} в число.\nПолный список: {arr}")
            raise
    return result


def create_files():
    for i in range(1, 11):
        file_content = '\n'.join(str(num) for num in random.sample(range(-1000, 1000), 3))
        with open(f'{i}.txt', 'w') as file:
            file.write(file_content)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    create_files()
    two_random_nums = random.sample(range(1, 11), 2)
    try:
        result = read_n_sum(two_random_nums[0], two_random_nums[1])
        logging.info(f"Сумма чисел: {result}")
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")
