import random
from sorting import bubble_sort


# моё сравнение двух списков
def compare_arrs(arr):
    target_arr = arr.copy()
    target_arr.sort()  # встроенная python сортировка
    bubble_sort(arr)  # моя сортировка
    return "Тест пройден" if arr == target_arr else "Тест не пройден"


if __name__ == '__main__':
    """
    Рассмотрим следующие состояния:
    1. числа в случайном порядке
    2. уже отсортированный список в обратном порядке
    3. список в котором одинаковые значения
    4. Уже отсортированный список
    """

    # Мои тесты:
    # 1 кейс
    test_arr = random.sample(range(-1000, 1000), 20)
    print("Случайная выборка", compare_arrs(test_arr))

    # 2 кейс
    test_arr = random.sample(range(-1000, 1000), 20)
    test_arr.sort()
    test_arr.reverse()
    print("Отсортированный в обратном порядке", compare_arrs(test_arr))

    # 3 кейс
    test_arr = [0] * 10
    print("Список одинаковых значений", compare_arrs(test_arr))

    # 4 кейс
    test_arr = random.sample(range(-1000, 1000), 20)
    test_arr.sort()
    print("Отсортированный список", compare_arrs(test_arr))
