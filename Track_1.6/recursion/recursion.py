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


def is_palindrome(row: str, left_idx=0, right_idx=None) -> bool:
    """Проверяет, является ли строка палиндромом, используя индексы для проверки символов."""
    if right_idx is None:
        right_idx = len(row) - 1  # Инициализируем правый индекс если он не установлен

    # Базовый случай: когда левый индекс больше или равен правому, все сравнения выполнены
    if left_idx >= right_idx:
        return True

    # Если крайние символы не равны, строка не является палиндромом
    if row[left_idx] != row[right_idx]:
        return False

    # Рекурсивно проверяем, уменьшая диапазон
    return is_palindrome(row, left_idx + 1, right_idx - 1)


def print_even_numbers_only(list_of_nums: list, index=0) -> None:
    """Выводит на печать только чётные числа из списка, используя индекс для доступа к элементам."""
    if index >= len(list_of_nums):  # Базовый случай: если индекс вышел за пределы списка
        return
    if list_of_nums[index] % 2 == 0:
        print(list_of_nums[index])
    return print_even_numbers_only(list_of_nums, index + 1)


def print_values_with_even_indexes(checkable_list: list, index=0) -> None:
    """Выводит на печать только значения только с чётными индексами из списка"""
    if not checkable_list or index >= len(checkable_list):
        return
    print(checkable_list[index])  # печатаем первый (нулевой индекс) элемент
    # увеличиваем индекс + 2 (на потенциально следующий чётный)
    print_values_with_even_indexes(checkable_list, index + 2)


def find_second_max_value_from_list(list_of_nums: list,
                                    curr_idx: int = 0,
                                    first_largest: Optional[int] = None,
                                    second_largest: Optional[int] = None) -> Optional[int]:
    """Возвращает второе по величине число из списка. Если список меньше двух значений, то вернёт None"""
    if len(list_of_nums) < 2:
        return None

    if curr_idx == len(list_of_nums):  # Базовый случай: достигли конца списка
        return second_largest  # Возвращаем второй максимум

    current_num = list_of_nums[curr_idx]  # Текущее число для сравнения

    # Если текущее число больше или равно известного максимума или максимума пока нет (None)
    if first_largest is None or current_num >= first_largest:
        first_largest, second_largest = current_num, first_largest  # Обновляем первый и второй максимумы

    # Если текущее число меньше первого, но больше или равно второму максимуму
    elif second_largest is None or current_num >= second_largest:
        second_largest = current_num  # Обновляем второй максимум

    # Рекурсивно обрабатываем следующий элемент списка
    return find_second_max_value_from_list(list_of_nums, curr_idx + 1, first_largest, second_largest)


def find_files_in_directories(dir_path: str, files_names_list: Optional[list] = None) -> list:
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
