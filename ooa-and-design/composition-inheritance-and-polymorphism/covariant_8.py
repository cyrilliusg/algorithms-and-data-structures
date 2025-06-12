from typing import TypeVar, Generic, Sequence, Callable


# Базовые классы для примера
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


class Dog(Animal):
    def make_sound(self) -> None:
        print("Гав!")


class Cat(Animal):
    def make_sound(self) -> None:
        print("Мяу!")


# Python — динамически типизированный язык.
# В данном примере демонстрируются аннотации только для статического анализа типов.
# Во время выполнения python не проверяет типы T_co или T_contra — это только "подсказки" для анализа.

# КОВАРИАНТНОСТЬ
# Контейнер, который только возвращает объекты T_co
T_co = TypeVar('T_co', covariant=True)


class Producer(Generic[T_co]):
    def __init__(self, item: T_co):
        self._item = item

    def get(self) -> T_co:
        """Возвращает объект типа T_co."""
        return self._item


# Из-за covariant=True, Producer[Dog] является подтипом Producer[Animal]
dog_producer: Producer[Dog] = Producer(Dog('Name 1'))
animal_producer: Producer[Animal] = dog_producer  # вот так сработает

a: Animal = animal_producer.get()  # возвращаем Animal, но фактически это Dog
a.make_sound()

# КОНТРАВАРИАНТНОСТЬ
# «Потребитель», который только принимает (принимает) объекты T_contra
T_contra = TypeVar('T_contra', contravariant=True)


class Consumer(Generic[T_contra]):
    def __init__(self, func: Callable[[T_contra], None]):
        self._func = func

    def accept(self, value: T_contra) -> None:
        """Обрабатывает объект типа T_contra."""
        self._func(value)


def handle_animal(a: Animal) -> None:
    print("Handling an animal:")
    a.make_sound()


# Благодаря contravariant=True, Consumer[Animal] является подтипом Consumer[Dog]
animal_consumer: Consumer[Animal] = Consumer(handle_animal)
animal_consumer.accept(Dog('Name 1'))  # Обработка животного, чьим наследником является собака

# КОВАРИАТИВНОСТЬ И КОНТРВАРИАТИВНОСТЬ В СТАНДАРТНОЙ БИБЛИОТЕКЕ:
# Sequence — ковариантный контейнер
dogs: Sequence[Dog] = [Dog('Name 1'), Dog('Name 2')]
animals: Sequence[Animal] = dogs  # OK благодаря covariance
for x in animals:
    x.make_sound()  # Гав! Гав!
