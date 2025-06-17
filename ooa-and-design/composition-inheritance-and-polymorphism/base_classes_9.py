import copy
import pickle
from typing import Type, Any as TypingAny


class General(object):
    """
    Самый базовый класс: определяет семь фундаментальных операций:
      1. copy_to      — копирование содержимого в существующий объект
      2. clone        — глубокое клонирование в новый объект
      3. equals       — поверхностное сравнение
      4. deep_equals  — глубокое сравнение вложенных полей
      5. serialize    — сериализация в bytes (pickle)
      6. deserialize  — восстановление из bytes
      7. __str__      — текстовое представление (печать)
      8. is_instance_of — проверка типа
      9. get_type    — получить реальный класс объекта
    """

    def copy_to(self, other: 'General') -> None:
        """Копирует в другой существующий объект (поверхностно)."""
        if not isinstance(other, self.__class__):
            raise TypeError(f"copy_to: ожидается объект {self.__class__.__name__}")
        other.__dict__.clear()
        other.__dict__.update(self.__dict__)

    def clone(self) -> 'General':
        """Глубокое клонирование: создаёт новый объект и копирует в него всё содержимое."""
        return copy.deepcopy(self)

    def __eq__(self, other: TypingAny) -> bool:
        """Поверхностное сравнение: словари атрибутов должны совпадать."""
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def deep_equals(self, other: TypingAny) -> bool:
        """Глубокое сравнение, учитывающее вложенные структуры."""
        try:
            return pickle.dumps(self) == pickle.dumps(other)
        except Exception:
            return False

    def serialize(self) -> bytes:
        """Сериализация объекта в байты (pickle)."""
        return pickle.dumps(self)

    @classmethod
    def deserialize(cls, data: bytes) -> 'General':
        """Восстановление объекта из байтов (pickle)."""
        obj = pickle.loads(data)
        if not isinstance(obj, cls):
            raise TypeError("deserialize: данные не соответствуют классу")
        return obj

    def __str__(self) -> str:
        """Наглядное текстовое представление содержимого объекта."""
        attrs = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"<{self.__class__.__name__} {attrs} {hex(id(self))}>"

    def is_instance_of(self, typ: Type) -> bool:
        """Проверяет, является ли объект указанного типа или его потомком."""
        return isinstance(self, typ)

    def get_type(self) -> Type:
        """Возвращает реальный класс (type) объекта."""
        return type(self)


class Any(General):
    """
    Открытый для расширения класс Any.
    По умолчанию не добавляет ничего нового, но может быть доработан,
    и от него наследуются все новые прикладные классы.
    """
    pass
