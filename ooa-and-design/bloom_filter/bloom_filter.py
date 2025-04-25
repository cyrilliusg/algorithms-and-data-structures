class BloomFilterADT:
    """
    АТД BloomFilterADT — фильтр Блюма для строк.

    Основные операции:
      - add(item: str) -> None:
            Команда помещения элемента в фильтр.
      - contains(item: str) -> bool:
            Запрос проверки принадлежности: возможно ли, что элемент
            уже был добавлен.
      - clear() -> None:
            Команда сброса фильтра.
      - capacity() -> int:
            Запрос длины фильтра (количество бит).

    Для операций определены статусные коды:
      ADD_NIL, ADD_OK;
      CONTAINS_NIL, CONTAINS_OK, CONTAINS_ERR.
    """

    # Статусы для add
    ADD_NIL = 0
    ADD_OK = 1

    # Статусы для contains
    CONTAINS_NIL = 0
    CONTAINS_OK = 1
    CONTAINS_ERR = 2

    N_1 = 17
    N_2 = 223

    DEFAULT_V = 0

    BIT = 1

    def __init__(self, filter_len: int) -> None:
        """
        Конструктор self.
        Предусловие: filter_len > 0.
        Постусловие: создан пустой фильтр длины filter_len (все биты нулевые).
        """
        if filter_len <= 0:
            raise ValueError("Размер фильтра должен быть >= 0")
        self._filter_len = filter_len
        self._filter = 0  # всё 0
        self._add_status = self.ADD_NIL
        self._contains_status = self.CONTAINS_NIL

    def _hash1(self, item: str) -> int:
        v = self.DEFAULT_V
        for c in item:
            v = (v * self.N_1 + ord(c)) % self._filter_len
        return v

    def _hash2(self, item: str) -> int:
        v = self.DEFAULT_V
        for c in item:
            v = (v * self.N_2 + ord(c)) % self._filter_len
        return v

    # -------------------- Команды --------------------
    def add(self, item: str) -> None:
        """
        Команда add.
        Предусловие: нет.
        Постусловие:
          - Устанавливаются биты на позициях hash1(item) и hash2(item).
          - _add_status = ADD_OK.
        """
        idx1 = self._hash1(item)
        idx2 = self._hash2(item)
        self._filter |= (self.BIT << idx1)
        self._filter |= (self.BIT << idx2)
        self._add_status = self.ADD_OK

    def clear(self) -> None:
        """
        Команда clear.
        Предусловие: нет.
        Постусловие: все биты сброшены
        """
        self._filter = 0
        self._add_status = self.ADD_NIL
        self._contains_status = self.CONTAINS_NIL

    # -------------------- Запросы --------------------
    def contains(self, item: str) -> bool:
        """
        Запрос contains.
        Предусловие: нет.
        Постусловие:
          - Если оба бита (hash1, hash2) установлены, возвращает True, _contains_status = CONTAINS_OK.
          - Иначе возвращает False, _contains_status = CONTAINS_ERR.
        """
        idx1 = self._hash1(item)
        idx2 = self._hash2(item)
        b1 = (self._filter >> idx1) & self.BIT
        b2 = (self._filter >> idx2) & self.BIT
        if b1 and b2:
            self._contains_status = self.CONTAINS_OK
            return True
        else:
            self._contains_status = self.CONTAINS_ERR
            return False

    def capacity(self) -> int:
        """
        Запрос capacity.
        Возвращает: длину фильтра в битах.
        """
        return self._filter_len

    # -------------- Методы для получения статусов операций --------------

    def get_add_status(self) -> int:
        """Возвращает статус последней add(): ADD_NIL или ADD_OK."""
        return self._add_status

    def get_contains_status(self) -> int:
        """
        Возвращает статус последнего contains():
        CONTAINS_NIL, CONTAINS_OK или CONTAINS_ERR.
        """
        return self._contains_status
