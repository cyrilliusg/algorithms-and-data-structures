import random
import string


class RandomKeyValueGenerator:
    """
    Класс RandomKeyValueGenerator для генерации случайных пар ключ-значение.

    Основные функции:
    - generate_random_pairs: Создает и печатает 100 случайных пар ключ-значение, затем удаляет их.
    - find_repeated_values: Возвращает значения из списка, которые повторяются минимум N раз.
    """

    def generate_random_pairs(self):
        """Генерирует 100 случайных пар ключ-значение, выводит и удаляет их."""
        n = 100  # количество пар
        keys = random.sample(range(0, 1000), n)  # уникальные ключи
        letters = string.ascii_lowercase  # доступные символы для значений
        # создание случайных строк в качестве значений
        values = [''.join(random.choice(letters) for i in range(5)) for x in range(n)]

        temp_dict = {}  # временный словарь для хранения пар

        for k, v in zip(keys, values):
            temp_dict[k] = v  # добавляем пару ключ-значение
            print(f'{k}: {temp_dict[k]}')  # печать
            del temp_dict[k]  # удаляем пару

        print(temp_dict)  # вывод пустого словаря после удаления всех пар

    def find_repeated_values(self, input_list, N):
        """
        Возвращает значения из списка, которые повторяются минимум N раз.

        :param input_list: Список для анализа
        :param N: Минимальное количество повторений для включения в результат
        """
        count_dict = {}  # словарь для подсчета количества каждого элемента
        for num in input_list:
            count_dict[num] = count_dict.get(num, 0) + 1  # подсчет элементов

        # возвращаем числа, повторяющиеся не менее N раз
        return [num for num, count in count_dict.items() if count >= N]


if __name__ == '__main__':
    pair_generator = RandomKeyValueGenerator()
    pair_generator.generate_random_pairs()
    # Пример вызова find_repeated_values с произвольными значениями
    pair_generator.find_repeated_values(random.sample(range(1, 10), 100), 10)
