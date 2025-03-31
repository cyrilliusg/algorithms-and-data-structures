from typing import Any, Optional


class Node:
    """
    Класс узла двусвязного списка.
    """

    def __init__(self, value: Any) -> None:
        self.value = value
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None


class ParentList:
    """
    Родительский класс для реализации общих операций двунаправленного списка с курсором.
    В данном классе реализованы все операции, общие для LinkedList и TwoWayList,
    за исключением операции left(), которая будет добавлена в классе TwoWayList.
    """

    # Статусы для операций, зависящих от предусловий.
    # Значение 0 означает, что операция ещё не вызывалась.
    HEAD_NIL = 0
    HEAD_OK = 1
    HEAD_ERR = 2

    TAIL_NIL = 0
    TAIL_OK = 1
    TAIL_ERR = 2

    RIGHT_NIL = 0
    RIGHT_OK = 1
    RIGHT_ERR = 2

    PUT_RIGHT_NIL = 0
    PUT_RIGHT_OK = 1
    PUT_RIGHT_ERR = 2

    PUT_LEFT_NIL = 0
    PUT_LEFT_OK = 1
    PUT_LEFT_ERR = 2

    REMOVE_NIL = 0
    REMOVE_OK = 1
    REMOVE_ERR = 2

    REPLACE_NIL = 0
    REPLACE_OK = 1
    REPLACE_ERR = 2

    FIND_NIL = 0
    FIND_OK = 1
    FIND_ERR = 2

    ADD_TO_EMPTY_NIL = 0
    ADD_TO_EMPTY_OK = 1
    ADD_TO_EMPTY_ERR = 2

    ADD_TAIL_NIL = 0
    ADD_TAIL_OK = 1
    ADD_TAIL_ERR = 2

    GET_NIL = 0
    GET_OK = 1
    GET_ERR = 2

    def __init__(self) -> None:
        """
        Конструктор ParentList.
        Постусловие: создан пустой список; курсор не установлен.
        """
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.cursor: Optional[Node] = None

        # Инициализация статусов операций
        self._head_status = ParentList.HEAD_NIL
        self._tail_status = ParentList.TAIL_NIL
        self._right_status = ParentList.RIGHT_NIL
        self._put_right_status = ParentList.PUT_RIGHT_NIL
        self._put_left_status = ParentList.PUT_LEFT_NIL
        self._remove_status = ParentList.REMOVE_NIL
        self._replace_status = ParentList.REPLACE_NIL
        self._find_status = ParentList.FIND_NIL
        self._add_to_empty_status = ParentList.ADD_TO_EMPTY_NIL
        self._add_tail_status = ParentList.ADD_TAIL_NIL
        self._get_status = ParentList.GET_NIL

    # -------------------- Команды --------------------

    def head_op(self) -> None:
        """
        Команда head_op.
        Предусловие: список не пуст.
        Постусловие:
            - Если список не пуст, курсор устанавливается на первый узел.
            - Иначе курсор не изменяется.
        Статус:
            - HEAD_OK, если операция выполнена успешно;
            - HEAD_ERR, если список пуст.
        """
        if self.head is None:
            self._head_status = ParentList.HEAD_ERR
        else:
            self.cursor = self.head
            self._head_status = ParentList.HEAD_OK

    def tail_op(self) -> None:
        """
        Команда tail_op.
        Предусловие: список не пуст.
        Постусловие:
            - Если список не пуст, курсор устанавливается на последний узел.
            - Иначе курсор не изменяется.
        Статус:
            - TAIL_OK, если операция выполнена успешно;
            - TAIL_ERR, если список пуст.

        Additional comment:
        Данная операция устанавливает курсор на последний элемент списка.
        В данной реализации мы можем получить последний элемент за O(1).
        Если бы tail_op реализовывалась через последовательное перемещение курсора с помощью right() или иного обхода,
        то в худшем случае потребовалось бы пройти через все элементы (сложность O(n)).
        """
        if self.tail is None:
            self._tail_status = ParentList.TAIL_ERR
        else:
            self.cursor = self.tail
            self._tail_status = ParentList.TAIL_OK

    def right(self) -> None:
        """
        Команда right.
        Предусловие: курсор установлен и текущий узел не является хвостом.
        Постусловие:
            - Если существует правый сосед, курсор смещается на него.
            - Иначе курсор остаётся неизменным.
        Статус:
            - RIGHT_OK, если операция выполнена успешно;
            - RIGHT_ERR, если курсор не установлен или уже на последнем узле.
        """
        if self.cursor is None or self.cursor.next is None:
            self._right_status = ParentList.RIGHT_ERR
        else:
            self.cursor = self.cursor.next
            self._right_status = ParentList.RIGHT_OK

    def put_right(self, value: Any) -> None:
        """
        Команда put_right.
        Предусловие: список не пуст (курсор установлен).
        Постусловие: новый узел со значением value вставляется сразу после текущего узла.
        Статус:
            - PUT_RIGHT_OK, если операция выполнена успешно;
            - PUT_RIGHT_ERR, если курсор не установлен.
        """
        if self.cursor is None:
            self._put_right_status = ParentList.PUT_RIGHT_ERR
            return

        new_node = Node(value)
        new_node.prev = self.cursor
        new_node.next = self.cursor.next

        if self.cursor.next is not None:
            self.cursor.next.prev = new_node
        self.cursor.next = new_node

        if self.cursor == self.tail:
            self.tail = new_node

        self._put_right_status = ParentList.PUT_RIGHT_OK

    def put_left(self, value: Any) -> None:
        """
        Команда put_left.
        Предусловие: список не пуст (курсор установлен).
        Постусловие: новый узел со значением value вставляется сразу перед текущим узлом.
        Статус:
            - PUT_LEFT_OK, если операция выполнена успешно;
            - PUT_LEFT_ERR, если курсор не установлен.
        """
        if self.cursor is None:
            self._put_left_status = ParentList.PUT_LEFT_ERR
            return

        new_node = Node(value)
        new_node.next = self.cursor
        new_node.prev = self.cursor.prev

        if self.cursor.prev is not None:
            self.cursor.prev.next = new_node
        self.cursor.prev = new_node

        if self.cursor == self.head:
            self.head = new_node

        self._put_left_status = ParentList.PUT_LEFT_OK

    def remove(self) -> None:
        """
        Команда remove.
        Предусловие: список не пуст (курсор установлен).
        Постусловие:
            - Текущий узел удаляется.
            - Если у удаляемого узла есть правый сосед, курсор смещается на него,
              иначе — на левый сосед.
            - Если список становится пустым, курсор сбрасывается.
        Статус:
            - REMOVE_OK, если операция выполнена успешно;
            - REMOVE_ERR, если курсор не установлен.
        """
        if self.cursor is None:
            self._remove_status = ParentList.REMOVE_ERR
            return

        node_to_remove = self.cursor

        # Выбор нового положения курсора
        if node_to_remove.next is not None:
            self.cursor = node_to_remove.next
        elif node_to_remove.prev is not None:
            self.cursor = node_to_remove.prev
        else:
            self.cursor = None

        # Удаление узла из списка
        if node_to_remove.prev is not None:
            node_to_remove.prev.next = node_to_remove.next
        else:
            # Удаляется голова списка
            self.head = node_to_remove.next

        if node_to_remove.next is not None:
            node_to_remove.next.prev = node_to_remove.prev
        else:
            # Удаляется хвост списка
            self.tail = node_to_remove.prev

        self._remove_status = ParentList.REMOVE_OK

    def clear(self) -> None:
        """
        Команда clear.
        Предусловий: нет.
        Постусловие: все узлы удаляются, список становится пустым, курсор сбрасывается.
        """
        self.head = None
        self.tail = None
        self.cursor = None

        # Сброс статусов операций до начального состояния
        self._head_status = ParentList.HEAD_NIL
        self._tail_status = ParentList.TAIL_NIL
        self._right_status = ParentList.RIGHT_NIL
        self._put_right_status = ParentList.PUT_RIGHT_NIL
        self._put_left_status = ParentList.PUT_LEFT_NIL
        self._remove_status = ParentList.REMOVE_NIL
        self._replace_status = ParentList.REPLACE_NIL
        self._find_status = ParentList.FIND_NIL
        self._add_to_empty_status = ParentList.ADD_TO_EMPTY_NIL
        self._add_tail_status = ParentList.ADD_TAIL_NIL
        self._get_status = ParentList.GET_NIL

    def add_to_empty(self, value: Any) -> None:
        """
        Команда add_to_empty.
        Предусловие: список пуст.
        Постусловие:
            - В пустой список добавляется новый узел со значением value.
            - head, tail и курсор устанавливаются на этот узел.
        Статус:
            - ADD_TO_EMPTY_OK, если операция выполнена успешно;
            - ADD_TO_EMPTY_ERR, если список не пуст.
        """
        if self.head is not None or self.tail is not None or self.cursor is not None:
            self._add_to_empty_status = ParentList.ADD_TO_EMPTY_ERR
            return

        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.cursor = new_node
        self._add_to_empty_status = ParentList.ADD_TO_EMPTY_OK

    def add_tail(self, value: Any) -> None:
        """
        Команда add_tail.
        Предусловие: нет.
        Постусловие:
            - Если список пуст, операция эквивалентна add_to_empty.
            - Если список не пуст, новый узел добавляется в конец списка.
        Статус:
            - ADD_TAIL_OK, если операция выполнена успешно;
            - ADD_TAIL_ERR, если произошла ошибка.
        """
        if self.head is None:
            self.add_to_empty(value)
            if self._add_to_empty_status == ParentList.ADD_TO_EMPTY_OK:
                self._add_tail_status = ParentList.ADD_TAIL_OK
            else:
                self._add_tail_status = ParentList.ADD_TAIL_ERR
            return

        new_node = Node(value)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self._add_tail_status = ParentList.ADD_TAIL_OK

    def replace(self, value: Any) -> None:
        """
        Команда replace.
        Предусловие: список не пуст (курсор установлен).
        Постусловие: значение текущего узла заменяется на value.
        Статус:
            - REPLACE_OK, если операция выполнена успешно;
            - REPLACE_ERR, если курсор не установлен.
        """
        if self.cursor is None:
            self._replace_status = ParentList.REPLACE_ERR
            return

        self.cursor.value = value
        self._replace_status = ParentList.REPLACE_OK

    def find(self, value: Any) -> None:
        """
        Команда find.
        Предусловие: список не пуст (курсор установлен).
        Постусловие:
            - Поиск начинается с узла, следующего за текущим, и курсор устанавливается
              на первый найденный узел, значение которого равно value.
            - Если такой узел не найден, курсор остаётся неизменным.
        Статус:
            - FIND_OK, если искомый узел найден;
            - FIND_ERR, если узел не найден или курсор не установлен.

        Additional comment:
        При использовании АТД с курсором акцент делается на работу с одним текущим элементом.
        При использовании АТД с курсором акцент делается на работу с одним текущим элементом.
        Операция find(value), перемещающая курсор к следующему элементу, позволяет итеративно обходить список
        и обрабатывать найденные вхождения по одному.
        Операция find(value) позволяет итеративно обходить список, обрабатывая найденные вхождения по одному.
        Таким образом, вместо возврата всего списка узлов, пользователь может последовательно выполнять поиск
        и применять нужные команды (например, remove или replace) к каждому найденному элементу.
        """
        if self.cursor is None:
            self._find_status = ParentList.FIND_ERR
            return

        node = self.cursor.next
        found = False
        while node is not None:
            if node.value == value:
                self.cursor = node
                found = True
                break
            node = node.next

        if found:
            self._find_status = ParentList.FIND_OK
        else:
            self._find_status = ParentList.FIND_ERR

    def remove_all(self, value: Any) -> None:
        """
        Команда remove_all.
        Предусловие: нет.
        Постусловие:
            - Удаляются все узлы, значение которых равно value.
            - Если текущий узел удаляется, курсор обновляется: сначала пытаемся перейти к правому соседу,
              если его нет — к левому; если список оказывается пустым, курсор сбрасывается.
        """
        node = self.head
        while node is not None:
            next_node = node.next  # сохраняем ссылку, т.к. node может быть удалён
            if node.value == value:
                if node == self.cursor:
                    if node.next is not None:
                        self.cursor = node.next
                    elif node.prev is not None:
                        self.cursor = node.prev
                    else:
                        self.cursor = None

                if node.prev is not None:
                    node.prev.next = node.next
                else:
                    self.head = node.next

                if node.next is not None:
                    node.next.prev = node.prev
                else:
                    self.tail = node.prev
            node = next_node

    # -------------------- Запросы --------------------

    def get(self) -> Optional[Any]:
        """
        Запрос get.
        Предусловие: список не пуст (курсор установлен).
        Постусловие:
            - Возвращается значение текущего узла без его удаления.
        Статус:
            - GET_OK, если операция выполнена успешно;
            - GET_ERR, если курсор не установлен.
        """
        if self.cursor is None:
            self._get_status = ParentList.GET_ERR
            return None

        self._get_status = ParentList.GET_OK
        return self.cursor.value

    def size(self) -> int:
        """
        Запрос size.
        Предусловие: нет.
        Возвращает: количество узлов в списке.
        """
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def is_head(self) -> bool:
        """
        Запрос is_head.
        Предусловие: список не пуст (курсор установлен).
        Возвращает: True, если курсор указывает на первый узел, иначе False.
        """
        return (self.cursor == self.head) if self.cursor is not None else False

    def is_tail(self) -> bool:
        """
        Запрос is_tail.
        Предусловие: список не пуст (курсор установлен).
        Возвращает: True, если курсор указывает на последний узел, иначе False.
        """
        return (self.cursor == self.tail) if self.cursor is not None else False

    def is_value(self) -> bool:
        """
        Запрос is_value.
        Предусловие: нет.
        Возвращает: True, если курсор установлен (то есть список не пуст), иначе False.
        """
        return self.cursor is not None

    # -------------- Методы для получения статусов операций --------------

    def get_head_status(self) -> int:
        return self._head_status

    def get_tail_status(self) -> int:
        return self._tail_status

    def get_right_status(self) -> int:
        return self._right_status

    def get_put_right_status(self) -> int:
        return self._put_right_status

    def get_put_left_status(self) -> int:
        return self._put_left_status

    def get_remove_status(self) -> int:
        return self._remove_status

    def get_replace_status(self) -> int:
        return self._replace_status

    def get_find_status(self) -> int:
        return self._find_status

    def get_add_to_empty_status(self) -> int:
        return self._add_to_empty_status

    def get_add_tail_status(self) -> int:
        return self._add_tail_status

    def get_get_status(self) -> int:
        return self._get_status


class LinkedList(ParentList):
    """
    Класс LinkedList.
    Наследует весь функционал ParentList без расширения.
    В этой реализации операция left() недоступна.
    """
    pass


class TwoWayList(ParentList):
    """
    Класс TwoWayList.
    Наследует общий функционал из ParentList и добавляет операцию left(),
    позволяющую сдвигать курсор на один узел влево.
    """

    LEFT_NIL = 0
    LEFT_OK = 1
    LEFT_ERR = 2

    def __init__(self) -> None:
        super().__init__()
        self._left_status = TwoWayList.LEFT_NIL

    def left(self) -> None:
        """
        Команда left.
        Предусловие: курсор установлен и текущий узел не является головой.
        Постусловие:
            - Если существует левый сосед, курсор смещается на него.
            - Иначе курсор остаётся неизменным.
        Статус:
            - LEFT_OK, если операция выполнена успешно;
            - LEFT_ERR, если курсор не установлен или уже на первом узле.
        """
        if self.cursor is None or self.cursor.prev is None:
            self._left_status = TwoWayList.LEFT_ERR
        else:
            self.cursor = self.cursor.prev
            self._left_status = TwoWayList.LEFT_OK

    def get_left_status(self) -> int:
        """
        Запрос get_left_status.
        Предусловие: нет.
        Возвращает: статус последней операции left().
        """
        return self._left_status
