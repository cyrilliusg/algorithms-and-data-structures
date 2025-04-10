from typing import Any


class QueueADT:
    """
        АТД QueueADT – концепция очереди.

        Операции:
          - size() -> int: запрос размера очереди.
          - get() -> Any: запрос значения из головы очереди.
          - enqueue(item: Any) -> None: команда добавления значения в конец очереди.
          - dequeue() -> Any: команда извлечения и возврата элемента из начала очереди.
          - clear() -> Any: команда очистки очереди.

        Для операций с предусловиями устанавливаются статусные флаги, доступные через методы
        get_get_status(), get_dequeue_status().
        """
    # Статусы для операции get:
    GET_NIL = 0
    GET_OK = 1
    GET_ERR = 2

    # Статусы для операции dequeue:
    DEQUE_NIL = 0
    DEQUE_OK = 1
    DEQUE_ERR = 2

    def __init__(self):
        self.__queue: list = []
        # Инициализация статусных флагов
        self.__get_status: int = self.GET_NIL
        self.__deque_status: int = self.DEQUE_NIL

    # -------------------- Команды --------------------
    def enqueue(self, item: Any) -> None:
        """
        Команда enqueue.
        Предусловие: нет.
        Постусловие:
            - Элемент добавлен в конец очереди.
        """
        self.__queue.append(item)

    def dequeue(self) -> Any:
        """
        команда dequeue.
        Предусловие: очередь не пуста.
        Постусловие:
            - Извлекается и возвращается значение очереди из головы.
        Статус:
            - DEQUEUE_OK, если операция выполнена успешно;
            - DEQUEUE_ERR, если очередь пуста.
        """
        if self.size() > 0:
            value = self.__queue.pop(0)
            self.__deque_status = self.DEQUE_OK
        else:
            value = None
            self.__deque_status = self.DEQUE_ERR
        return value

    def clear(self) -> None:
        """
        Команда clear.
        Предусловие: нет.
        Постусловие:
          - Массив очищается: count становится 0, емкость сбрасывается до 16.
        """
        self.__queue = []
        # Обнуление статусных флагов
        self.__get_status = self.GET_NIL
        self.__deque_status = self.DEQUE_NIL

    # -------------------- Запросы --------------------
    def get(self) -> Any:
        """
        Запрос get.
        Предусловие: очередь не пуста.
        Постусловие:
            - Возвращается значение очереди из головы.
        Статус:
            - GET_OK, если операция выполнена успешно;
            - GET_ERR, если очередь пуста.
        """
        if not self.__queue:
            self.__get_status = self.GET_ERR
            value = None
        else:
            self.__get_status = self.DEQUE_OK
            value = self.__queue[-1]
        return value

    def size(self) -> int:
        """
        Запрос size.
        Получить размер очереди
        """
        return len(self.__queue)

    # -------------- Методы для получения статусов операций --------------
    def get_get_status(self) -> int:
        return self.__get_status

    def get_dequeue_status(self) -> int:
        return self.__deque_status
