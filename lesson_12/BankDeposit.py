import logging


class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Банковский баланс
        """
        assert isinstance(initial_balance,
                          (int, float)) and initial_balance >= 0, "Начальный баланс должен быть неотрицательным числом"
        self.__balance = initial_balance
        logging.info(f"Создан счет с начальным балансом: {self.__balance}")

    def deposit(self, amount):
        """
        Внести сумму на счет
        """
        assert isinstance(amount, (int, float)) and amount > 0, "Сумма вклада должна быть положительным числом"
        self.__balance += amount
        logging.info(f"Внесено: {amount}. Текущий баланс: {self.__balance}")

    def withdraw(self, amount):
        """
        Снять сумму со счета
        """
        assert isinstance(amount, (int, float)) and amount > 0, "Сумма снятия должна быть положительным числом"
        assert self.__balance - amount >= 0, f"Текущий баланс: {self.__balance}. Попытка снятия: {amount}. Недостаточно средств на счете. "
        self.__balance -= amount
        logging.info(f"Снято: {amount}. Текущий баланс: {self.__balance}")


# Демонстрация использования класса
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
try:
    account.withdraw(200)  # Это вызовет AssertionError
except AssertionError as error:
    logging.error(error)
