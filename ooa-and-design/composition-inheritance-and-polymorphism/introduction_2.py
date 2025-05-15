class Animal:
    """
    АТД Animal — базовый класс животного.
    Задаёт интерфейс и общее поведение для всех животных.
    """
    MAKE_SOUND_NIL = 0
    MAKE_SOUND_OK = 1
    MAKE_SOUND_ERROR = 2

    def __init__(self, name: str):
        self._name = name
        self._make_sound_status = self.MAKE_SOUND_NIL

    # -------------------- Команды --------------------
    def clear(self) -> None:
        """Команда: сбросить статус последнего make_sound()."""
        self._make_sound_status = self.MAKE_SOUND_NIL

    # -------------------- Запросы --------------------
    def make_sound(self) -> None:
        """
        Базовая реализация «издаёт звук» (статус OK).
        Предусловие: нет.
        Постусловие: _make_sound_status == MAKE_SOUND_OK.
        """
        self._make_sound_status = self.MAKE_SOUND_OK

    def get_name(self) -> str:
        """Запрос: возвращает имя животного."""
        return self._name

    # ------ Методы для получения статусов операций ------
    def get_make_sound_status(self) -> int:
        """Возвращает статус последней make_sound()."""
        return self._make_sound_status


class Dog(Animal):
    """Наследник Animal: обычная собака с лаем."""

    def make_sound(self) -> None:
        """
        Переопределение базового метода:
        выводит 'Гав!' и устанавливает статус OK.
        """
        print(f"{self.get_name()} говорит: Гав!")
        self._make_sound_status = self.MAKE_SOUND_OK


# ------ Расширение класса-родителя ------
class GuardDog(Dog):
    """
    Расширение класса Dog:
    добавляем новую команду guard(), расширяющую интерфейс.
    """

    def guard(self) -> None:
        """
        Команда: охранять территорию.
        Предусловие: нет.
        Постусловие: вывод сообщения и статус MAKE_SOUND_OK.
        """
        print(f"{self.get_name()} охраняет территорию!")
        self._make_sound_status = self.MAKE_SOUND_OK


# ------ Специализация класса-родителя ------
class QuietDog(Dog):
    """
    Специализация класса Dog:
    переопределяем make_sound() для тихого лая.
    """

    def make_sound(self) -> None:
        """
        Специализированный тихий лай.
        Предусловие: нет.
        Постусловие: вывод 'тяв' и статус MAKE_SOUND_OK.
        """
        print(f"{self.get_name()} говорит: тяв!")
        self._make_sound_status = self.MAKE_SOUND_OK
