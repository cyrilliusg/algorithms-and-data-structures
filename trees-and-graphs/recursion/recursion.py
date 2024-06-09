from typing import Optional

import os


def power(n: int, m: int) -> int:
    """Рекурсивно возводит число n в степень m"""
    if m == 0:
        return 1  # Любое число в степени 0 равно 1
    if m == 1:
        return n  # Базовый случай рекурсии
    return n * power(n, m - 1)  # Рекурсивно умножаем n на результат n в степени (m-1)


def sum_of_digits(n: int) -> int:
    """Возвращает сумму цифр числа n. Вернёт 0 при переданном нуле"""
    if n == 0:
        return 0  # Базовый случай: если число равно 0, возвращаем 0
    return n % 10 + sum_of_digits(n // 10)  # Складываем последнюю цифру числа с суммой остальных цифр


def length_of_list(checkable_list: list) -> int:
    """Возвращает длину списка"""
    if not checkable_list:
        return 0  # Базовый случай: если список пустой
    checkable_list.pop(0)
    return 1 + length_of_list(checkable_list)  # прибавляем 1 + вызываем заново


def check_palindrome_recursively(row: str, left_index: int, right_index: int) -> bool:
    # Базовый случай: когда левый индекс больше или равен правому, все сравнения выполнены
    if left_index >= right_index:
        return True

    # Если крайние символы не равны, строка не является палиндромом
    if row[left_index] != row[right_index]:
        return False

    # Рекурсивно проверяем, уменьшая диапазон
    return check_palindrome_recursively(row, left_index + 1, right_index - 1)


def is_palindrome(input_row: str) -> bool:
    """Проверяет, является ли строка палиндромом"""
    start_left_index = 0  # левый индекс по умолчанию 0
    start_right_index = len(input_row) - 1  # Инициализируем правый индекс

    return check_palindrome_recursively(input_row, start_left_index, start_right_index)


def print_even_numbers_only_recursively(list_of_nums: list, current_idx: int) -> None:
    if current_idx >= len(list_of_nums):  # Базовый случай: если индекс вышел за пределы списка
        return
    if list_of_nums[current_idx] % 2 == 0:
        print(list_of_nums[current_idx])
    return print_even_numbers_only_recursively(list_of_nums, current_idx + 1)


def print_even_numbers_only(input_nums_list: list) -> None:
    """Выводит на печать только чётные числа из списка"""
    start_index = 0  # по умолчанию 0
    return print_even_numbers_only_recursively(input_nums_list, start_index)


def print_values_with_even_indexes_recursively(lst: list, current_index: int) -> None:
    if not lst or current_index >= len(lst):  # Базовый случай: если индекс вышел за пределы списка
        return
    print(lst[current_index])
    # увеличиваем индекс + 2 (на потенциально следующий чётный)
    current_index += 2
    return print_values_with_even_indexes_recursively(lst, current_index)


def print_values_with_even_indexes(input_list: list) -> None:
    """Выводит на печать только значения только с чётными индексами из списка"""
    start_index = 0  # по умолчанию 0
    return print_values_with_even_indexes_recursively(input_list, start_index)


def find_second_max_value_from_list_recursively(list_of_nums: list,
                                                curr_index: int,
                                                first_largest: int,
                                                second_largest: int) -> Optional[int]:
    if curr_index == len(list_of_nums):  # Базовый случай: достигли конца списка
        return second_largest  # Возвращаем второй максимум

    current_num = list_of_nums[curr_index]  # Текущее число для сравнения

    # Если текущее число больше или равно известного максимума или максимума пока нет (None)
    if current_num >= first_largest:
        first_largest, second_largest = current_num, first_largest  # Обновляем первый и второй максимумы

    # Если текущее число меньше первого, но больше или равно второму максимуму
    elif current_num >= second_largest:
        second_largest = current_num  # Обновляем второй максимум

    curr_index += 1
    # Рекурсивно обрабатываем следующий элемент списка
    return find_second_max_value_from_list_recursively(list_of_nums, curr_index, first_largest, second_largest)


def find_second_max_value_from_list(input_list_of_nums: list) -> Optional[int]:
    """Возвращает второе по величине число из списка. Если список меньше двух значений, то вернёт None"""
    if len(input_list_of_nums) < 2:
        return None

    start_index = 2
    # определяем первоначальные два значения
    if input_list_of_nums[0] > input_list_of_nums[1]:
        first_largest, second_largest = input_list_of_nums[0], input_list_of_nums[1]
    else:
        first_largest, second_largest = input_list_of_nums[1], input_list_of_nums[0]

    return find_second_max_value_from_list_recursively(input_list_of_nums, start_index,
                                                       first_largest, second_largest)


def find_files_in_directories(dir_path: str, files_names_list: Optional[list]) -> list:
    """Возвращает все файлы из текущего и вложенных каталогов по переданному пути"""
    if files_names_list is None:
        files_names_list = []

    if not dir_path or not os.path.isdir(dir_path):
        return files_names_list

    current_objects_in_directory = os.listdir(dir_path)
    if not current_objects_in_directory:
        return files_names_list

    for dir_obj_name in current_objects_in_directory:
        full_path = os.path.join(dir_path, dir_obj_name)  # Формируем полный путь к объекту
        if os.path.isdir(full_path):
            find_files_in_directories(full_path, files_names_list)  # Рекурсивный вызов для подкаталога
        elif os.path.isfile(full_path):
            files_names_list.append(full_path)  # Добавляем полный путь к файлу

    return files_names_list
