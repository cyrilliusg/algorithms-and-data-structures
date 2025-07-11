from typing import TypeVar, Generic, Iterable, Iterator
from abc import ABC, abstractmethod


# Базовый класс
class Animal(ABC):
    @abstractmethod
    def make_sound(self) -> None:
        pass


# Унаследованные
class Dog(Animal):
    def make_sound(self) -> None:
        print("Гав!")


class Cat(Animal):
    def make_sound(self) -> None:
        print("Мяу!")


# Делаем immutable list для хранения животных
T_co = TypeVar('T_co', covariant=True)


class AnimalsList(Generic[T_co]):
    def __init__(self, items: Iterable[T_co]) -> None:
        self.__items: Iterable[T_co] = items

    def __iter__(self) -> Iterator[T_co]:
        return iter(self.__items)


if __name__ == "__main__":
    # -------------------Полиморфный вызов метода-------------------
    pets: list[Animal] = [Dog(), Cat()]
    for p in pets:
        # Здесь мы не знаем заранее, какого именно подтипа будет animal, нужный make_sound() выберется динамически.
        p.make_sound()

    # -------------------Ковариантный вызов метода-------------------
    pets_container = AnimalsList(pets)
    for a in pets_container:
        # Механизм ковариантности позволяет списку Dog трактоваться как Sequence[Animal], и метод вызывается без явных проверок.
        a.make_sound()
