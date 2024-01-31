import random
import logging


def read_n_sum(first_num, second_num):
    """
    Основной метод.
    Принимает на вход 2 числа, считывает файлы с одноименными названиями и возвращает в них сумму чисел.
    """
    process_status = {
        0: 'Без ошибок',
        1: 'Ошибка считывания файла',
        2: 'Входные данные не являются списком',
        3: 'Список должен содержать ровно три элемента',
        4: 'Ошибка при конвертации значения в число.',
    }
    user_process_status = {first_num: process_status[0], second_num: process_status[0]}
    final_arr = []

    for file_name in [first_num, second_num]:
        file_path = f'{file_name}.txt'
        content = read_file(file_path)

        if content[1] != 0:  # если произошла ошибка или нет содержимого, то пропустить файл
            user_process_status[file_name] = process_status[content[1]]
            continue

        content = content[0]
        content = content.strip().split('\n')
        logging.info(f"Открыт файл {file_path}, содержимое: {content}")

        content = validate_numbers_array(content)
        if content[1] != 0:  # если содержимое не удовлетворяет требованиям, то пропустить файл
            user_process_status[file_name] = process_status[content[1]]
            continue

        content = content[0]

        final_arr.extend(content)
    return sum(final_arr) if final_arr else 0, user_process_status


def read_file(path):
    """
    Метод по считыванию содержимого из файла.
    Принимает на вход путь к файлу и возвращает содержимое в виде строки.
    В случае ошибки считывания возвращает None.
    """
    try:
        with open(path, 'r') as file:
            return file.read(), 0
    except OSError as e:
        logging.error(f"Ошибка при открытии файла {path}: {e}")
        return None, 1


def validate_numbers_array(arr, arr_len=3):
    """
    Метод проверяет переданный объект на соответствие требованиям задачи и конвертирует значения в числа.
    """
    if not isinstance(arr, list):
        logging.error(f"Ошибка в типе данных (не список): {arr}")
        return [[], 2]

    if len(arr) != arr_len:
        logging.error(f"Не три значения: {arr}")
        return [[], 3]

    result = []
    for item in arr:
        try:
            result.append(int(item))
        except ValueError:
            logging.error(f"Ошибка при конвертации значения {item} в число.\nПолный список: {arr}")
            return [[], 4]
    return result, 0


def create_files():
    for i in range(1, 11):
        file_content = '\n'.join(str(num) for num in random.sample(range(-1000, 1000), 3))
        with open(f'{i}.txt', 'w') as file:
            file.write(file_content)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    create_files()
    two_random_nums = random.sample(range(1, 11), 2)
    result = read_n_sum(two_random_nums[0], two_random_nums[1])
    logging.info(f"Сумма чисел: {result[0]}\nСтатус файлов: {result[1]}")
