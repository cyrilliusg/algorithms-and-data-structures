from typing import Any, Optional


class NativeDictionaryADT:
    """
    АТД NativeDictionaryADT — отображение «строка → значение» на основе открытой адресации.

    Основные операции:
      - put(key: str, value: Any) -> None:
            Команда добавления или обновления пары (key, value).
      - get(key: str) -> Optional[Any]:
            Запрос получения значения по ключу.
      - contains(key: str) -> bool:
            Запрос проверки наличия ключа в словаре.
      - size() -> int:
            Запрос числа пар в словаре.
      - capacity() -> int:
            Запрос максимальной ёмкости словаря.
      - clear() -> None:
            Команда очистки словаря.

    Для операций put, get и contains определены статусные коды:
      PUT_NIL / PUT_OK / PUT_ERR;
      GET_NIL / GET_OK / GET_ERR;
      CONTAINS_NIL / CONTAINS_OK / CONTAINS_ERR.
    """

    # Статусы для put
    PUT_NIL = 0
    PUT_OK = 1
    PUT_ERR = 2

    # Статусы для get
    GET_NIL = 0
    GET_OK = 1
    GET_ERR = 2

    # Статусы для contains
    CONTAINS_NIL = 0
    CONTAINS_OK = 1
    CONTAINS_ERR = 2

    # Коэффициенты для a, b, p
    A, B, P = 2, 3, 17

    # Шаг для put
    STEP = 3

    def __init__(self, capacity: int) -> None:
        """
        Конструктор.
        Предусловие: capacity > 0.
        Постусловие: создан пустой словарь ёмкости capacity.
        """
        if capacity <= 0:
            raise ValueError("Емкость должна быть > 0")
        self._capacity = capacity
        self._keys: list[Optional[str]] = [None] * capacity
        self._values: list[Optional[Any]] = [None] * capacity
        self._size = 0

        # статусные флаги
        self._put_status = self.PUT_NIL
        self._get_status = self.GET_NIL
        self._contains_status = self.CONTAINS_NIL

    def _hash(self, key: str) -> int:
        """простая хеш‑функция по длине UTF‑8"""
        length = len(key.encode('utf-8'))
        return (self.A * length + self.B) % self.P % self._capacity

    def _next_idx(self, idx: int) -> int:
        """
        Вспомогательный метод линейного пробирования:
        возвращает следующий индекс при шаге STEP по модулю capacity.
        """
        return (idx + self.STEP) % self._capacity

    # -------------------- Команды --------------------
    def put(self, key: str, value: Any) -> None:
        """
        Команда put.
        Предусловие: key — строка; в словаре не заполнено более capacity() пар.
        Постусловие:
          - Если key уже есть, его значение обновляется, _put_status = PUT_OK.
          - Иначе, если есть свободный слот, пара вставляется, size() увеличивается, _put_status = PUT_OK.
          - Если свободных слотов нет, _put_status = PUT_ERR.
        """
        if self._size >= self._capacity:
            self._put_status = self.PUT_ERR
            return

        idx = self._hash(key)

        first_empty = None

        for _ in range(self._capacity):
            k = self._keys[idx]
            if k is None:
                # запомним первый свободный
                first_empty = idx
                break
            if k == key:
                # ключ найден — обновляем
                self._values[idx] = value
                self._put_status = self.PUT_OK
                return
            idx = self._next_idx(idx)

        # нет мест
        if first_empty is None:
            self._put_status = self.PUT_ERR
            return

        # вставляем в первый свободный слот
        self._keys[first_empty] = key
        self._values[first_empty] = value
        self._size += 1
        self._put_status = self.PUT_OK

    def clear(self) -> None:
        """
        Команда clear.
        Предусловие: нет.
        Постусловие: словарь очищен, size() == 0, все слоты свободны.
        """
        self._keys = [None] * self._capacity
        self._values = [None] * self._capacity
        self._size = 0
        self._put_status = self.PUT_NIL
        self._get_status = self.GET_NIL
        self._contains_status = self.CONTAINS_NIL

    # -------------------- Запросы --------------------
    def get(self, key: str) -> Optional[Any]:
        """
        Запрос get.
        Предусловие: key — строка.
        Постусловие:
          - Если key найден, возвращает значение и _get_status = GET_OK.
          - Иначе возвращает None и _get_status = GET_ERR.
        """
        idx = self._hash(key)

        for _ in range(self._capacity):
            k = self._keys[idx]
            if k is None:
                self._get_status = self.GET_ERR
                return None
            if k == key:
                self._get_status = self.GET_OK
                return self._values[idx]
            idx = self._next_idx(idx)

        self._get_status = self.GET_ERR
        return None

    def contains(self, key: str) -> bool:
        """
        Запрос contains.
        Предусловие: key — строка.
        Постусловие:
          - Если key найден, возвращает True и _contains_status = CONTAINS_OK.
          - Иначе возвращает False и _contains_status = CONTAINS_ERR.
        """
        idx = self._hash(key)

        for _ in range(self._capacity):
            k = self._keys[idx]
            if k is None:
                self._contains_status = self.CONTAINS_ERR
                return False
            if k == key:
                self._contains_status = self.CONTAINS_OK
                return True
            idx = self._next_idx(idx)

        self._contains_status = self.CONTAINS_ERR
        return False

    def capacity(self) -> int:
        """Запрос capacity. Возвращает максимальную ёмкость словаря."""
        return self._capacity

    def size(self) -> int:
        """Запрос size. Возвращает текущее число пар (key, value)."""
        return self._size

    # -------------- Методы для получения статусов операций --------------
    def get_put_status(self) -> int:
        """Возвращает статус последней put(): PUT_NIL/PUT_OK/PUT_ERR."""
        return self._put_status

    def get_get_status(self) -> int:
        """Возвращает статус последнего get(): GET_NIL/GET_OK/GET_ERR."""
        return self._get_status

    def get_contains_status(self) -> int:
        """Возвращает статус последнего contains(): CONTAINS_NIL/CONTAINS_OK/CONTAINS_ERR."""
        return self._contains_status
