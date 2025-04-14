from typing import Any, Optional


# ========= БАЗОВЫЙ КЛАСС =========
class ParentQueueADT:
    """
    Базовый АТД для очередей.

    Содержит общее внутреннее хранилище (_container) и общие операции:
      - size() -> int: запрос размера очереди.
      - clear() -> None: команда очистки очереди.
      - addTail(item: Any) -> None: команда добавления значения в конец очереди.
      - removeFront() -> Optional[Any]: команда извлечения и возврата элемента из начала очереди.

    Эти операции универсальны как для стандартной очереди, так и для двусторонней.
    Также в данном классе определяются статусные флаги для операций addTail и removeFront.
    """
    # Статусы для addTail
    ADD_TAIL_NIL = 0
    ADD_TAIL_OK = 1

    # Статусы для removeFront
    REMOVE_FRONT_NIL = 0
    REMOVE_FRONT_OK = 1
    REMOVE_FRONT_ERR = 2

    def __init__(self) -> None:
        self._container: list[Any] = []
        self._add_tail_status: int = self.ADD_TAIL_NIL
        self._remove_front_status: int = self.REMOVE_FRONT_NIL

    # -------------------- Команды --------------------
    def clear(self) -> None:
        """
        Команда clear.
        Предусловие: нет.
        Постусловие: контейнер становится пустым.
        """
        self._container = []
        self._add_tail_status = self.ADD_TAIL_NIL
        self._remove_front_status = self.REMOVE_FRONT_NIL

    def addTail(self, item: Any) -> None:
        """
        Команда addTail.
        Предусловие: нет.
        Постусловие: элемент добавлен в конец контейнера.
        """
        self._container.append(item)
        self._add_tail_status = ParentQueueADT.ADD_TAIL_OK

    def removeFront(self) -> Optional[Any]:
        """
        Команда removeFront.
        Предусловие: контейнер не пуст.
        Постусловие:
          - Если контейнер не пуст, удаляет и возвращает элемент из начала.
          - Если пуст, возвращает None.
        """
        if self.size() == 0:
            self._remove_front_status = ParentQueueADT.REMOVE_FRONT_ERR
            return None
        value = self._container.pop(0)
        self._remove_front_status = ParentQueueADT.REMOVE_FRONT_OK
        return value

    # -------------------- Запросы --------------------
    def size(self) -> int:
        """
        Запрос size.
        Предусловие: нет.
        Возвращает: количество элементов в контейнере.
        """
        return len(self._container)

    # -------------- Методы для получения статусов операций --------------
    def get_add_tail_status(self) -> int:
        """
        Возвращает статус последней операции addTail.
        """
        return self._add_tail_status

    def get_remove_front_status(self) -> int:
        """
        Возвращает статус последней операции removeFront.
        """
        return self._remove_front_status


# ========= КЛАСС Queue =========
class Queue(ParentQueueADT):
    """
    АТД Queue – концепция стандартной очереди (FIFO).

    Операции:
      - enqueue(item: Any) -> None: команда добавления значения в конец очереди. (обертка для addTail).
      - dequeue() -> Optional[Any]: команда извлечения и возврата элемента из начала очереди. (обертка для removeFront).
      - get() -> Optional[Any]: запрос значения из головы очереди.
      - clear() -> None: команда очистки очереди. (переопределена из-за введения нового статуса для get().
      - size() – унаследован от ParentQueueADT.

    Статусные флаги для addTail и removeFront доступны через get_add_tail_status() и get_remove_front_status().
    Дополнительно здесь вводится статус для get().
    """
    # Статусы для get
    GET_NIL = 0
    GET_OK = 1
    GET_ERR = 2

    def __init__(self) -> None:
        super().__init__()
        self._get_status: int = Queue.GET_NIL

    # -------------------- Команды --------------------
    def enqueue(self, item: Any) -> None:
        """
        Обертка для addTail.
        Добавляет элемент в конец очереди.
        """
        self.addTail(item)

    def dequeue(self) -> Optional[Any]:
        """
        Обертка для removeFront.
        Удаляет и возвращает элемент из начала очереди.
        """
        return self.removeFront()

    def clear(self) -> None:
        """
        Команда clear.
        Предусловие: нет.
        Постусловие: контейнер становится пустым.
        """
        self._container = []
        self._add_tail_status = self.ADD_TAIL_NIL
        self._remove_front_status = self.REMOVE_FRONT_NIL
        self._get_status = Queue.GET_NIL

    # -------------------- Запросы --------------------
    def get(self) -> Optional[Any]:
        """
        Запрос get.
        Предусловие: очередь не пуста.
        Постусловие:
          - Если очередь не пуста, возвращает первый элемент без удаления.
          - Иначе возвращает None.
        Устанавливает статус: GET_OK или GET_ERR.
        """
        if self.size() == 0:
            self._get_status = Queue.GET_ERR
            return None
        self._get_status = Queue.GET_OK
        return self._container[0]

    # -------------- Методы для получения статусов операций --------------
    def get_get_status(self) -> int:
        """
        Возвращает статус последней операции get.
        """
        return self._get_status


# ========= КЛАСС Deque =========
class Deque(ParentQueueADT):
    """
    АТД Deque – концепция двусторонней очереди.

    Помимо общих операций addTail и removeFront, добавляются:
      - addFront(item: Any) -> None:
            Добавление элемента в начало очереди.
      - removeTail() -> Optional[Any]:
            Удаление и возврат элемента из конца очереди.
      - getFront() -> Optional[Any]:
            Возвращает первый элемент очереди без удаления.
      - getTail() -> Optional[Any]:
            Возвращает последний элемент очереди без удаления.
    - clear() -> None: команда очистки очереди. (переопределена из-за введения нового статуса для get().
      - size() – унаследована от ParentQueueADT.

    Для операций getFront, getTail и removeTail определены отдельные статусные флаги.
    """
    # Статусы для getFront:
    GET_FRONT_NIL = 0
    GET_FRONT_OK = 1
    GET_FRONT_ERR = 2

    # Статусы для getTail:
    GET_TAIL_NIL = 0
    GET_TAIL_OK = 1
    GET_TAIL_ERR = 2

    # Статусы для removeTail:
    REMOVE_TAIL_NIL = 0
    REMOVE_TAIL_OK = 1
    REMOVE_TAIL_ERR = 2

    def __init__(self) -> None:
        super().__init__()
        self._get_front_status = self.GET_FRONT_NIL
        self._get_tail_status = self.GET_TAIL_NIL
        self._remove_tail_status = self.REMOVE_TAIL_NIL

    # -------------------- Команды --------------------
    def clear(self) -> None:
        """
        Команда clear.
        Предусловие: нет.
        Постусловие: контейнер становится пустым.
        """
        self._container = []
        self._add_tail_status = self.ADD_TAIL_NIL
        self._remove_front_status = self.REMOVE_FRONT_NIL
        self._get_front_status = self.GET_FRONT_NIL
        self._get_tail_status = self.GET_TAIL_NIL
        self._remove_tail_status = self.REMOVE_TAIL_NIL

    def addFront(self, item: Any) -> None:
        """
        Команда addFront.
        Предусловие: нет.
        Постусловие: элемент добавляется в начало очереди.
        """
        self._container.insert(0, item)

    # addTail и removeFront уже наследуются из ParentQueueADT

    def removeTail(self) -> Optional[Any]:
        """
        Команда removeTail.
        Предусловие: очередь не пуста.
        Постусловие:
          - Если очередь не пуста, удаляет и возвращает последний элемент.
          - Иначе возвращает None.
        Устанавливает статус: REMOVE_TAIL_OK или REMOVE_TAIL_ERR.
        """
        if self.size() == 0:
            self._remove_tail_status = Deque.REMOVE_TAIL_ERR
            return None
        value = self._container.pop()
        self._remove_tail_status = Deque.REMOVE_TAIL_OK
        return value

    # -------------------- Запросы --------------------
    def getFront(self) -> Optional[Any]:
        """
        Запрос getFront.
        Предусловие: очередь не пуста.
        Постусловие:
          - Если очередь не пуста, возвращает первый элемент без удаления.
          - Иначе возвращает None.
        Устанавливает статус: GET_FRONT_OK или GET_FRONT_ERR.
        """
        if self.size() == 0:
            self._get_front_status = Deque.GET_FRONT_ERR
            return None
        self._get_front_status = Deque.GET_FRONT_OK
        return self._container[0]

    def getTail(self) -> Optional[Any]:
        """
        Запрос getTail.
        Предусловие: очередь не пуста.
        Постусловие:
          - Если очередь не пуста, возвращает последний элемент без удаления.
          - Иначе возвращает None.
        Устанавливает статус: GET_TAIL_OK или GET_TAIL_ERR.
        """
        if self.size() == 0:
            self._get_tail_status = Deque.GET_TAIL_ERR
            return None
        self._get_tail_status = Deque.GET_TAIL_OK
        return self._container[-1]

    # -------------- Методы для получения статусов операций --------------
    def get_getFront_status(self) -> int:
        return self._get_front_status

    def get_getTail_status(self) -> int:
        return self._get_tail_status

    def get_removeTail_status(self) -> int:
        return self._remove_tail_status
