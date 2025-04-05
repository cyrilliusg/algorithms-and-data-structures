import ctypes
from typing import Any, Optional


class DynArrayADT:
    """
    АТД DynArrayADT – динамический массив, реализующий концепцию динамического массива.

    Основные операции:
      - size() -> int: запрос размера массива.
      - get(index: int) -> Any: запрос значения по индексу.
      - set(index: int, value: Any) -> None: команда установки значения по индексу.
      - append(value: Any) -> None: команда добавления элемента в конец массива.
      - insert(index: int, value: Any) -> None: команда вставки элемента по индексу.
      - delete(index: int) -> None: команда удаления элемента по индексу.
      - pop() -> Any: команда удаления и возвращения последнего элемента.
      - clear() -> None: команда очистки массива.

    Для операций с предусловиями устанавливаются статусные флаги, доступные через методы
    get_get_status(), get_set_status(), get_append_status(), get_insert_status(), get_delete_status(), get_pop_status() и get_clear_status().
    """

    # Статусы для операции get:
    GET_NIL = 0
    GET_OK = 1
    GET_ERR = 2

    # Статусы для операции set:
    SET_NIL = 0
    SET_OK = 1
    SET_ERR = 2

    # Статусы для операции append:
    APPEND_NIL = 0
    APPEND_OK = 1

    # Статусы для операции insert:
    INSERT_NIL = 0
    INSERT_OK = 1
    INSERT_ERR = 2

    # Статусы для операции delete:
    DELETE_NIL = 0
    DELETE_OK = 1
    DELETE_ERR = 2

    # Статусы для операции pop:
    POP_NIL = 0
    POP_OK = 1
    POP_ERR = 2

    def __init__(self) -> None:
        """
        Конструктор DynArrayADT.
        Предусловие: нет.
        Постусловие: создан пустой динамический массив с count = 0 и capacity = 16.
        """
        self.count = 0
        self.capacity = 16
        self.array = self._make_array(self.capacity)
        # Инициализация статусных флагов
        self._get_status = DynArrayADT.GET_NIL
        self._set_status = DynArrayADT.SET_NIL
        self._append_status = DynArrayADT.APPEND_NIL
        self._insert_status = DynArrayADT.INSERT_NIL
        self._delete_status = DynArrayADT.DELETE_NIL
        self._pop_status = DynArrayADT.POP_NIL

    def size(self) -> int:
        """
        Запрос size.
        Предусловие: нет.
        Возвращает: текущее количество элементов в массиве.
        """
        return self.count

    def _make_array(self, new_capacity: int) -> Any:
        """
        Вспомогательная функция: создает новый массив заданной емкости.
        """
        return (new_capacity * ctypes.py_object)()

    def _resize(self, new_capacity: int) -> None:
        """
        Вспомогательная команда resize.
        Предусловие: new_capacity >= count.
        Постусловие: емкость массива изменена на new_capacity, все элементы сохранены.
        """
        new_array = self._make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def get(self, index: int) -> Optional[Any]:
        """
        Запрос get.
        Предусловие: 0 <= index < count.
        Постусловие:
          - Если предусловие выполнено, возвращается элемент с индексом index, _get_status = GET_OK.
          - Иначе _get_status = GET_ERR и возвращается None.
        """
        if index < 0 or index >= self.count:
            self._get_status = DynArrayADT.GET_ERR
            return None
        self._get_status = DynArrayADT.GET_OK
        return self.array[index]

    def set(self, index: int, value: Any) -> None:
        """
        Команда set.
        Предусловие: 0 <= index < count.
        Постусловие:
          - Если предусловие выполнено, элемент с индексом index устанавливается равным value, _set_status = SET_OK.
          - Иначе _set_status = SET_ERR.
        """
        if index < 0 or index >= self.count:
            self._set_status = DynArrayADT.SET_ERR
            return
        self.array[index] = value
        self._set_status = DynArrayADT.SET_OK

    def append(self, value: Any) -> None:
        """
        Команда append.
        Предусловие: нет.
        Постусловие:
          - Элемент value добавляется в конец массива.
          - Если count == capacity, емкость массива удваивается.
          - _append_status = APPEND_OK.
        """
        if self.count == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.count] = value
        self.count += 1
        self._append_status = DynArrayADT.APPEND_OK

    def insert(self, index: int, value: Any) -> None:
        """
        Команда insert.
        Предусловие: 0 <= index <= count.
        Постусловие:
          - Элемент value вставляется на позицию index, сдвигая все последующие элементы вправо.
          - Если count == capacity, емкость удваивается.
          - _insert_status = INSERT_OK при успешной вставке, иначе INSERT_ERR.
        """
        if index < 0 or index > self.count:
            self._insert_status = DynArrayADT.INSERT_ERR
            return
        if self.count == self.capacity:
            self._resize(2 * self.capacity)
        for i in range(self.count, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.count += 1
        self._insert_status = DynArrayADT.INSERT_OK

    def delete(self, index: int) -> None:
        """
        Команда delete.
        Предусловие: 0 <= index < count.
        Постусловие:
          - Элемент с индексом index удаляется, а все последующие сдвигаются влево.
          - Если после удаления count < capacity/2, емкость уменьшается до max(int(capacity/1.5), 16).
          - _delete_status = DELETE_OK при успешном удалении, иначе DELETE_ERR.
        """
        if index < 0 or index >= self.count:
            self._delete_status = DynArrayADT.DELETE_ERR
            return
        for i in range(index, self.count - 1):
            self.array[i] = self.array[i + 1]
        self.count -= 1
        self.array[self.count] = None  # Для корректной сборки мусора
        if self.count < self.capacity // 2:
            new_capacity = int(self.capacity / 1.5)
            if new_capacity < 16:
                new_capacity = 16
            self._resize(new_capacity)
        self._delete_status = DynArrayADT.DELETE_OK

    def pop(self) -> Optional[Any]:
        """
        Команда pop.
        Предусловие: массив не пуст.
        Постусловие:
          - Последний элемент удаляется и возвращается.
          - Если после удаления count < capacity/2, емкость уменьшается до max(int(capacity/1.5), 16).
          - _pop_status = POP_OK при успешном выполнении, иначе POP_ERR.
        """
        if self.count == 0:
            self._pop_status = DynArrayADT.POP_ERR
            return None
        value = self.array[self.count - 1]
        self.delete(self.count - 1)
        self._pop_status = DynArrayADT.POP_OK
        return value

    def clear(self) -> None:
        """
        Команда clear.
        Предусловие: нет.
        Постусловие:
          - Массив очищается: count становится 0, емкость сбрасывается до 16.
        """
        self.count = 0
        self.capacity = 16
        self.array = self._make_array(self.capacity)
        # Обнуление статусных флагов
        self._get_status = DynArrayADT.GET_NIL
        self._set_status = DynArrayADT.SET_NIL
        self._append_status = DynArrayADT.APPEND_NIL
        self._insert_status = DynArrayADT.INSERT_NIL
        self._delete_status = DynArrayADT.DELETE_NIL
        self._pop_status = DynArrayADT.POP_NIL

    # Методы для получения статусов операций

    def get_get_status(self) -> int:
        return self._get_status

    def get_set_status(self) -> int:
        return self._set_status

    def get_append_status(self) -> int:
        return self._append_status

    def get_insert_status(self) -> int:
        return self._insert_status

    def get_delete_status(self) -> int:
        return self._delete_status

    def get_pop_status(self) -> int:
        return self._pop_status
