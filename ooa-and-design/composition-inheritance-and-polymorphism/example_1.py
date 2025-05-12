class Animal:
    """
        АТД Animal — базовый класс животного. Задаёт интерфейс и общее поведение для всех животных
    """
    # Статусы для make_sound
    MAKE_SOUND_NIL = 0
    MAKE_SOUND_OK = 1
    MAKE_SOUND_ERROR = 2

    def __init__(self, name: str):
        self._name = name  # общее поле для всех потомков
        self._make_sound_status = self.MAKE_SOUND_NIL

    # -------------------- Команды --------------------
    def clear(self) -> None:
        """Команда: очистка статусов операций"""
        self._make_sound_status = self.MAKE_SOUND_NIL

    # -------------------- Запросы --------------------

    def make_sound(self) -> None:
        """
        Метод, который должны реализовать все потомки
        В текущей реализации -- запрос (не меняет признаков объекта).
        Предусловие: нет.
        Постусловие:
          - Должен вызвать голос.
        """
        self._make_sound_status = self.MAKE_SOUND_OK
        return None

    def get_name(self) -> str:
        """Запрос: возвращает имя животного"""
        return self._name

    # -------------- Методы для получения статусов операций --------------
    def get_make_sound_status(self) -> int:
        """Возвращает статус последней make_sound(): MAKE_SOUND_NIL или MAKE_SOUND_OK или MAKE_SOUND_ERROR."""
        return self._make_sound_status


# Наследование: Dog расширяет Animal и даёт свою реализацию make_sound()
class Dog(Animal):
    def make_sound(self) -> None:
        print(f"{self.get_name()} говорит: Гав!")


# Наследование: Cat расширяет Animal и даёт свою реализацию make_sound()
class Cat(Animal):
    def make_sound(self) -> None:
        print(f"{self.get_name} говорит: Мяу!")


# Композиция: Person содержит («has-a») объект Animal
class Person:
    def __init__(self, name: str, pet: Animal):
        self._name = name
        self._pet = pet

    # Полиморфизм: работаем с разными животными через общий интерфейс Animal
    def play_with_pet(self) -> None:
        """Полиморфный вызов make_sound() питомца"""
        print(f"{self._name} играет со своим питомцем:")
        self._pet.make_sound()
