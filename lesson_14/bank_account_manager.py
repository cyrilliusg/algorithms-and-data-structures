import logging
import random
import os


class BankAccount:
    """
    Класс банковского счета.
    Содержит закрытые атрибуты для номера счета, имени владельца и баланса.

    Экземпляры этого класса мы будем создавать.
    """

    def __init__(self):
        # Инициализация параметров счета
        self.__account_number = None  # номер счета
        self.__account_holder = None  # владелец счета
        self.__balance = None  # баланс счета

    def assign_account(self, *args):
        """Назначает детали счета для экземпляра BankAccount."""
        self.__set_account_holder(args[0])
        self.__set_account_number(args[1])
        self.__set_balance(args[2])

    def __set_account_number(self, value):
        """Устанавливает номер счета после проверки."""
        if isinstance(value, int) and value > 0:
            self.__account_number = value
        else:
            raise ValueError('Неверный номер счета')

    def __set_account_holder(self, value):
        """Устанавливает имя владельца счета после проверки."""
        if isinstance(value, str) and len(value) > 0:
            self.__account_holder = value
        else:
            raise ValueError('Неверное имя владельца счета')

    def __set_balance(self, value):
        """Устанавливает баланс после проверки."""
        if isinstance(value, int) and value >= 0:
            self.__balance = value
        else:
            raise ValueError('Неверное значение баланса')


class BankAccountGenerator:
    """Генерирует случайные данные для банковских счетов."""

    def __init__(self):
        self.default_names = ['Raz', 'Sardar', 'Mai', 'Heron', 'Osmond']

    def __generate_data(self, num):
        """Приватный метод для генерации случайных имен, балансов и ID счетов."""
        names = [random.choice(self.default_names) for i in range(num)]
        # Генерация балансов с диапазоном, который может симулировать ошибки для тестирования
        balances = random.sample(range(-100000, 100000), num)
        # Генерация ID счётов с диапазоном, который может симулировать ошибки для тестирования
        account_ids = random.sample(range(-1000, 100000), num)
        return names, balances, account_ids

    def generate(self, num):
        """Генерирует данные для указанного количества счетов."""
        if num < 0:
            raise ValueError("Количество счетов должно быть положительным")
        return self.__generate_data(num)


class IO_driver:
    """Обрабатывает ввод/вывод операций для данных банковского счета."""

    def __init__(self):
        self.start_line = 'BankAccount_'
        self.end_line = '.txt'
        self.data_processor = DataProcessor()

    def create_files(self, names, balances, account_ids):
        """Создает файлы для каждого банковского счета с его соответствующими данными."""
        for name, balance, account_id in zip(names, balances, account_ids):
            content = self.data_processor.process_to_output(name, balance, account_id)
            with open(self.start_line + str(account_id) + self.end_line, 'w') as file:
                file.write(content)

    def __get_files(self):
        """Возвращает список файлов банковских счетов."""
        return [file for file in os.listdir() if file.startswith(self.start_line)]

    def get_content(self, process=False):
        """Читает содержимое каждого файла банковского счета."""
        content = []
        for filename in self.__get_files():
            with open(filename, 'r') as file:
                if process:
                    content.append(self.data_processor.process_to_input(file.read()))
                else:
                    content.append(file.read())
        return content

    def del_files(self):
        """Удаляет все файлы банковских счетов."""
        for filename in self.__get_files():
            os.remove(filename)


class DataProcessor:
    """Обрабатывает данные в формат для хранения и обратно."""

    def process_to_output(self, *args):
        """Преобразует аргументы в строку, разделенную запятыми."""
        return ','.join(str(value) for value in args)

    def process_to_input(self, string):
        """Преобразует строку, разделенную запятыми, обратно в данные."""
        string = string.split(',')
        for i in range(len(string)):
            try:
                string[i] = int(string[i])
            except:
                continue
        return string


if __name__ == '__main__':
    # Настройка базовой конфигурации логирования
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    data_generator = BankAccountGenerator()
    io_driver = IO_driver()

    # Генерация и обработка 10 банковских счетов
    io_driver.create_files(*data_generator.generate(10))
    # Считываем из файлов данные (process=True) значит - с форматированием числовых данных
    content = io_driver.get_content(process=True)

    accounts = []
    for account_data in content:
        account_instance = BankAccount()
        try:
            account_instance.assign_account(*account_data)
        except Exception as e:
            logging.error(f'Ошибка создания счета: {account_data}. Системная ошибка: {e}')
        else:
            accounts.append(account_instance)
            logging.info(f'Счет успешно создан: {account_data}')

    # Опционально. очистка файлов после обработки, чтобы не засорять память, т.к. каждый раз разные id
    io_driver.del_files()
