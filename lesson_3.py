"""
Здравствуйте, Сергей Игоревич!

Посмотрев разбор прошлого задания, понял, что что-то намудрил с прошлым кодом.
Можно было в разы проще сделать, просто описав атрибуты, а я в основном делал методы, усложнял их.
Но, к сути текущего 3 занятия - ограничить взаимодействие пользователя с атрибутами напрямую (с помощью обращения
к атрибутам через методы, создание приватных атрибутов с помощью '__', и через декораторы setter и property),
как мне кажется, я и пришёл в конце.

Исходя из этого, реализацию прошлого задания, в принципе, можно отнести и к этому занятию, т.к. там и конструктор
__init__, и обращение через методы к атрибутам реализованы. Я немного подредактирую прошлый код, но в целом он будет тем же

И Ваша идея, что при моделировании сущностей в предметной области рассматривать их в первую очередь
через их действия, а не их свойства, очень интересна, потому, что у меня есть небольшая трудность
с придумыванием сущностей и их свойств, и такая методика может быть полезна.
"""


class Inventory:
    """
    Инвентарь. Всего доступно 6 слотов
    Управление предметами в инвентаре
    """

    def __init__(self):
        self.__total_size = 6
        self.__items = [InventoryItem(i) for i in
                        range(self.__total_size)]  # генератор списка из 6 объектов - ячеек инвентаря

    def add_item(self, index, item):
        """
        Добавляет предмет в инвентарь
        :param index: позиция в инвентаре
        :param item: предмет
        """
        self.__check_index(index)
        if not self.__items[index].is_available:  # обращаемся к свойству ячейки инвентаря
            raise ValueError('Ячейка уже занята')
        self.__items[index].append(item)

    def remove_item(self, index):
        """
        Удаляет предмет из инвентаря
        :param index: позиция в инвентаре
        """
        self.__check_index(index)
        self.__items[index].remove()

    def get_tool_tip(self, index):
        """
        Возвращает текст о предмете для всплывающей подсказке при наведении курсора
        :param index: позиция в инвентаре
        :return: Item.name
        """
        self.__check_index(index)
        return self.__items[index].get_name()

    def __check_index(self, index):
        """
        Метод для проверки индекса
        :param index: позиция в инвентаре
        """
        if index >= self.__total_size:
            raise ValueError('Индекс не может быть больше размера инвентаря')

    def current_occupancy(self):
        """
        :return: количество занятых слотов
        """
        current_occupancy = 0
        for inventory_item in self.__items:
            if not inventory_item.is_available:
                current_occupancy += 1
        return current_occupancy

    def __str__(self):
        """
        :return: выводит на печать имена всех предметов в инвентаре
        """

        return ''.join(
            [f'{inventory_item.value}\n' if inventory_item.value else 'Пусто\n' for inventory_item in self.__items])


class InventoryItem:
    """
    Ячейка в инвентаре. У нее есть индекс, имя(имя предмета), статус (занята или свободна)
    и методы, удаляющие предмет, добавляющие, и, как пример, вощзвращающие имя предмета
    """

    def __init__(self, index):
        self.index = index
        self.value = None
        self.is_available = True

    def remove(self):
        """
        Удаление предмета из ячейки
        """
        self.value = None
        self.is_available = True

    def append(self, value):
        """
        добавление предмета в ячейку
        :param value: объект класса Item
        :return:
        """
        self.value = value
        self.is_available = False

    def get_name(self):
        """
        :return: Имя предмета
        """
        return self.value.name


class Item:
    """
    Игровой предмет
    """

    def __init__(self):
        self.__name = None  # можно сделать через декоратор property и устанавливать через setter
        self.__is_active = None
        self.__active_ability = None
        self.__quantity = 1  # по умолчанию в единственном экземпляре, но, некоторые предметы могут быть 'расходниками' (например tango) и быть > 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        """
        Можно по сути сделать только установление имени как обязательного свойства, а всё остальное
        подтягивать в этом методе по имени, т.к. по идее все имена уникальные
        :param value: имя предмета
        :return:
        """
        self.__name = value

    def __str__(self):
        return self.__name


# создаём объект инвентаря
inventory = Inventory()

print('Текущая загруженность', inventory.current_occupancy())

# создаём предмет, присваиваем имя
first_item = Item()
first_item.name = 'Tango'
print(f'Добавили предмет {first_item.name}')
# добавляем в инвентарь
inventory.add_item(0, first_item)

# выводим загруженность и содержимое инвентаря
print('Текущая загруженность', inventory.current_occupancy())

print(inventory)
