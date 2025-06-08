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


# Подкласс Dog переопределяет метод make_sound()
class Dog(Animal):
    def make_sound(self) -> None:
        print(f"{self.get_name()} говорит: Гав!")


# Подкласс Cat тоже переопределяет make_sound()
class Cat(Animal):
    def make_sound(self) -> None:
        print(f"{self.get_name()} говорит: Мяу!")


if __name__ == "__main__":
    pets: list[Animal] = [Dog("Животное 1"), Cat("Животное 2")]

    # Для каждого объекта вызов make_sound() будет привязан к своей реализации
    for pet in pets:
        print("Взаимодействие с питомцем:")
        pet.make_sound()  # здесь Python обнаружит, чей именно make_sound() вызывать
