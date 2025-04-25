from typing import Any, Optional, Iterator


class HashTableADT:
    """
    АТД HashTableADT — хэш-таблица как хранилище неупорядоченных значений.

    Основные операции:
      - add(value: Any) -> None:
            Команда добавления value в таблицу.
      - remove(value: Any) -> None:
            Команда удаления value из таблицы.
      - contains(value: Any) -> bool:
            Запрос проверки принадлежности value таблице.
            Всегда возвращает True/False, и устанавливает _contains_status в CONTAINS_TRUE/CONTAINS_FALSE.
      - size() -> int:
            Запрос числа элементов в таблице.
      - capacity() -> int:
            Запрос максимальной ёмкости таблицы.
      - clear() -> None:
            Команда очистки таблицы, возвращающая ёмкость к исходному значению.

    Для каждой команды с предусловием введены статусные коды:
      ADD_NIL, ADD_OK, ADD_ERR;
      REMOVE_NIL, REMOVE_OK, REMOVE_ERR;
      CONTAINS_NIL, CONTAINS_TRUE, CONTAINS_FALSE.
    """
    # Статусы для add
    ADD_NIL = 0
    ADD_OK = 1
    ADD_ERR = 2

    # Статусы для remove
    REMOVE_NIL = 0
    REMOVE_OK = 1
    REMOVE_ERR = 2

    # Статусы для contains
    CONTAINS_NIL = 0
    CONTAINS_TRUE = 1
    CONTAINS_FALSE = 2

    def __init__(self, capacity: int) -> None:
        """
        Конструктор.
        Предусловие: capacity > 0.
        Постусловие: создана пустая таблица размером capacity.
        """
        if capacity <= 0:
            raise ValueError("Емкость не может быть меньше или равно нулю")
        self._capacity = capacity
        self._size = 0
        self._slots: list[Optional[Any]] = [None] * capacity
        self._tombstone = object()

        # Инициализация статусов
        self._add_status = HashTableADT.ADD_NIL
        self._remove_status = HashTableADT.REMOVE_NIL
        self._contains_status = HashTableADT.CONTAINS_NIL

    def __hash(self, value: Any) -> int:
        # базовый хэш + приведение к [0..capacity-1]
        return hash(value) % self._capacity

    # -------------------- Команды --------------------
    def add(self, value: Any) -> None:
        """
        Команда добавления value в таблицу.
        Предусловие: таблица не заполнена полностью.
        Постусловие:
          * Если value уже есть в таблице, ничего не меняется, _add_status = ADD_OK.
          * Иначе, вставляется value, _add_status = ADD_OK.
          * Если нет свободного слота (таблица полна), _add_status = ADD_ERR.
        """
        if self._size >= self._capacity:
            self._add_status = HashTableADT.ADD_ERR
            return

        idx = self.__hash(value)
        first_tomb: Optional[int] = None

        for _ in range(self._capacity):
            slot = self._slots[idx]
            if slot is None:
                # свободный слот — вставляем либо в первую tomb, либо сюда
                target = first_tomb if first_tomb is not None else idx
                self._slots[target] = value
                self._size += 1
                self._add_status = HashTableADT.ADD_OK
                return

            if slot is self._tombstone:
                # запомним первую могилу
                if first_tomb is None:
                    first_tomb = idx

            elif slot == value:
                # уже есть — ничего не делаем
                self._add_status = HashTableADT.ADD_OK
                return

            idx = (idx + 1) % self._capacity

        # если дошли сюда — нет пустых и tomb, или capacity==0
        self._add_status = HashTableADT.ADD_ERR

    def remove(self, value: Any) -> None:
        """
        Команда удаления value из таблицы.
        Предусловие: нет.
        Постусловие:
          * Если value найден, удаляется (ставится «могила»), _remove_status = REMOVE_OK.
          * Иначе, _remove_status = REMOVE_ERR.
        """
        idx = self.__hash(value)
        for _ in range(self._capacity):
            slot = self._slots[idx]
            if slot is None:
                # пустой слот — value нет
                self._remove_status = HashTableADT.REMOVE_ERR
                return

            if slot is not self._tombstone and slot == value:
                # нашли — ставим tomb
                self._slots[idx] = self._tombstone
                self._size -= 1
                self._remove_status = HashTableADT.REMOVE_OK
                return

            idx = (idx + 1) % self._capacity

        self._remove_status = HashTableADT.REMOVE_ERR

    def clear(self) -> None:
        """Команда clear. Очищает таблицу, сбрасывая все слоты и счётчик."""
        self._slots = [None] * self._capacity
        self._size = 0
        self._add_status = HashTableADT.ADD_NIL
        self._remove_status = HashTableADT.REMOVE_NIL
        self._contains_status = HashTableADT.CONTAINS_NIL

    # -------------------- Запросы --------------------

    def contains(self, value: Any) -> bool:
        """
        Запрос contains.
        Предусловие: нет.
        Постусловие:
          - Если value в таблице, возвращает True и _contains_status = CONTAINS_TRUE.
          - Иначе, возвращает False и _contains_status = CONTAINS_FALSE.
        """
        idx = self.__hash(value)
        for _ in range(self._capacity):
            slot = self._slots[idx]
            if slot is None:
                # пустой слот — дальше value нет
                self._contains_status = HashTableADT.CONTAINS_FALSE
                return False
            if slot is not self._tombstone and slot == value:
                self._contains_status = HashTableADT.CONTAINS_TRUE
                return True
            # пробуем следующий
            idx = (idx + 1) % self._capacity

        # обошли всю таблицу — не нашли
        self._contains_status = HashTableADT.CONTAINS_FALSE
        return False

    def size(self) -> int:
        """Запрос size. Возвращает текущее количество элементов."""
        return self._size

    def capacity(self) -> int:
        """Запрос capacity. Возвращает максимальную ёмкость таблицы."""
        return self._capacity

    # -------------- Методы для получения статусов операций --------------

    def get_add_status(self) -> int:
        """Возвращает статус последней add(): ADD_NIL/ADD_OK/ADD_ERR."""
        return self._add_status

    def get_remove_status(self) -> int:
        """Возвращает статус последней remove(): REMOVE_NIL/REMOVE_OK/REMOVE_ERR."""
        return self._remove_status

    def get_contains_status(self) -> int:
        """Возвращает статус последней contains(): CONTAINS_NIL/CONTAINS_TRUE/CONTAINS_FALSE."""
        return self._contains_status

    def _elements(self) -> Iterator[Any]:
        """Вспомогательный метод: перебрать все существующие значения."""
        for slot in self._slots:
            if slot is not None and slot is not self._tombstone:
                yield slot


class PowerSet(HashTableADT):
    """
    АТД PowerSet — множество, унаследованное от HashTableADT, с ограничением по capacity.

    Дополнительные операции:
      - intersection(other: PowerSet) -> PowerSet
      - union(other: PowerSet) -> PowerSet
      - difference(other: PowerSet) -> PowerSet
      - issubset(other: PowerSet) -> bool
    """

    def __init__(self, capacity: int = 17) -> None:
        super().__init__(capacity)

    # -------------------- Команды --------------------

    # Переопределяем add/contains/remove, чтобы вернуть булево и использовать статус
    def add(self, value: Any) -> bool:
        """
        Вставка value в множество.
        Возвращает True, если элемент был добавлен или уже присутствовал;
        False, если место закончилось.
        """
        super().add(value)
        return self.get_add_status() == self.ADD_OK

    def remove(self, value: Any) -> bool:
        """
        Удаление value из множества.
        Возвращает True, если элемент был найден и удалён, иначе False.
        """
        super().remove(value)
        return self.get_remove_status() == self.REMOVE_OK

    # -------------------- Запросы --------------------
    def contains(self, value: Any) -> bool:
        """
        Проверка наличия value в множестве.
        """
        result = super().contains(value)
        return result

    def size(self) -> int:
        """Количество элементов в множестве."""
        return super().size()

    def intersection(self, other: "PowerSet") -> "PowerSet":
        """Пересечение множеств."""
        cap = max(self.capacity(), other.capacity())
        result = PowerSet(cap)
        # итерируем по меньшему
        if self.size() <= other.size():
            small, big = self, other
        else:
            small, big = other, self
        for v in small._elements():
            if big.contains(v):
                result.add(v)
        return result

    def union(self, other: "PowerSet") -> "PowerSet":
        """Объединение множеств."""
        cap = max(self.capacity(), other.capacity())
        result = PowerSet(cap)
        for v in self._elements():
            result.add(v)
        for v in other._elements():
            result.add(v)
        return result

    def difference(self, other: "PowerSet") -> "PowerSet":
        """Разность множеств: элементы self, отсутствующие в other."""
        result = PowerSet(self.capacity())
        for v in self._elements():
            if not other.contains(v):
                result.add(v)
        return result

    def issubset(self, other: "PowerSet") -> bool:
        """Проверка, является ли other подмножеством self (other ⊆ self)."""
        for v in other._elements():
            if not self.contains(v):
                return False
        return True
