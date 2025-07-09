from abc import ABC, abstractmethod


# Иерархия статусов
class SoundStatus(ABC):
    """АТД «статус звука»: задаёт общий интерфейс."""

    @abstractmethod
    def code(self) -> int:
        """Цифровой код статуса."""
        pass

    @abstractmethod
    def description(self) -> str:
        """Человеко-читаемое описание."""
        pass


class NilStatus(SoundStatus):
    def code(self) -> int:
        return 0

    def description(self) -> str:
        return "не было вызова make_sound"


class OkStatus(SoundStatus):
    def code(self) -> int:
        return 1

    def description(self) -> str:
        return "звук успешно издан"


class ErrorStatus(SoundStatus):
    def code(self) -> int:
        return 2

    def description(self) -> str:
        return "ошибка при издании звука"


# АТД Animal хранит статус-объект
class Animal:
    """
    АТД Animal — хранит _status не как int, а как SoundStatus.
    """

    def __init__(self, name: str):
        self._name = name
        self._status: SoundStatus = NilStatus()

    def clear(self) -> None:
        """Сбрасываем статус на NilStatus."""
        self._status = NilStatus()

    def make_sound(self) -> None:
        """
        Базовая реализация (может быть точкой расширения):
        просто записываем OkStatus.
        """
        self._status = OkStatus()

    def get_name(self) -> str:
        return self._name

    def get_status(self) -> SoundStatus:
        """Полиморфно возвращает текущий статус."""
        return self._status


# Потомки, которые делают своё переопределение make_sound
class Dog(Animal):
    def make_sound(self) -> None:
        print(f"{self.get_name()} Гав!")
        self._status = OkStatus()


class Cat(Animal):
    def make_sound(self) -> None:
        print(f"{self.get_name()} Мяу!")
        self._status = OkStatus()


if __name__ == "__main__":
    animals = [Dog("Dog 1"), Cat("Cat 1")]

    for a in animals:
        print(a.get_name(), "до make_sound():", a.get_status().description())
        a.make_sound()
        print(a.get_name(), "после make_sound():", a.get_status().description())
        a.clear()
        print(a.get_name(), "после clear():", a.get_status().description())
