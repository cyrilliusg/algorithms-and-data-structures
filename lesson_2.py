"""
1.1.

1. Microsoft Excel
Если рассматривать GUI часть, то, программу можно представить как набор "виджетов", взаимодействующих между собой.
Есть базовый класс 'Widget', имеющий схожие для всех виджетов свойства (т.н. ядро), например: size, color, is_enabled.
От него  создают уже конкретные виджеты с индивидуальными свойствами (наследуя все свойства ядра),либо, так же пытаются
группировать в схожие группы, например: разные виды кнопок в один класс Button с дополнительными свойствами,
характерными именно для кнопок (например: флаг is_checked - нажата кнопка или нет), и только потом уже выводить
в частные случаи той или иной кнопки (PushButton, RadioButton, CheckBox).

Подводя итог по Excel, это могут быть классы
- Item (ячейка) имеющая value (значение), format (текстовый, числовой, процентный), color, font и т.д. (каждый из
   перечисленных атрибутов также можно разложить на классы, например, font состоит из size, bold, weight ....);
- Table (таблица) имеющая shape (размеры), заголовки и состоящая из ячеек (Item);
- Sheet - основное окно для таблицы, состоящее из table и видимо какой-то поверх абстракции, потому что в excel таблица -
   это не только ячейки (можно же например вставлять картинки и свободно передвигать их, наверно какая-то система координат)
- Верхняя панель инструментов состоит из Button, Combobox, LineEdit и прочих виджетов, которые выводят свои диалоговые окна,
принимают сигналы и (-или) значения, передают их в Controller, который в свою очередь взаимодействует с Моделью (в зависимости
от того, что за действие, но, например с таблицей (Table)) и Controller вносит какие-то изменения в неё
- MainWindow состоит из верхней панели и нижнего контейнера (TabWidget), который хранит в себе вкладки (Sheet)


2. Dota 2 (по ней будут созданы классы в 1.2)
Если рассмотреть 'бизнес-логику' (если я правильно применяю термин в данном контексте), то, это MOBA игра с персонажами,
у которых есть свои характеристики и способности, в игре они могут иметь инвентарь с предметами, каждый предмет обладает своими
характеристиками, так же есть окружающий мир, с которым взаимодействует игрок через персонажа (деревья, крипы (которые
в свою очередь вражеские/союзные/нейтральные), постройки (так же вражеские/союзные/нейтральные). Персонаж может
наносить урон как физический (от атаки), так и от способностей; применять урон к другим персонажам/крипам/постройкам.
Урон может быть физический, магический, чистый, смешанный.

"""


class Inventory:
    """
    Инвентарь. Всего доступно 6 слотов
    Управление предметами в инвентаре
    """

    def __init__(self):
        self.__total_size = 6
        self.items = [InventoryItem(i) for i in range(self.__total_size)]  # генератор списка из 6 объектов - ячеек инвентаря

    def add_item(self, index, item):
        """
        Добавляет предмет в инвентарь
        :param index: позиция в инвентаре
        :param item: предмет
        """
        self.__check_index(index)
        if not self.items[index].is_available:
            raise ValueError('Ячейка уже занята')
        self.items[index].append(item)

    def remove_item(self, index):
        """
        Удаляет предмет из инвентаря
        :param index: позиция в инвентаре
        """
        self.__check_index(index)
        self.items[index].remove()

    def get_tool_tip(self, index):
        """
        Возвращает текст о предмете для всплывающей подсказке при наведении курсора
        :param index: позиция в инвентаре
        :return: Item.name
        """
        self.__check_index(index)
        return self.items[index].get_name()

    def __check_index(self, index):
        """
        Метод для проверки индекса
        :param index: позиция в инвентаре
        """
        if index >= self.__total_size:
            raise ValueError('Индекс не может быть больше размера инвентаря')

    def __str__(self):
        """
        :return: выводит на печать имена всех предметов в инвентаре
        """

        return ''.join(
            [f'{inventory_item.value}\n' if inventory_item.value else 'Пусто\n' for inventory_item in self.items])


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

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __str__(self):
        return self.__name


# имена предметов
items_names = ['Tango', 'Observer Ward', 'Clarity', 'Smoke of Deceit', 'Faerie Fire', 'Bottle']

# создаём инвентарь
inventory = Inventory()

print('Изначально:\n', inventory)
# итерируемся по списку и добавляем предметы в инвентарь
for i in range(len(items_names)):
    item = Item()
    item.name = items_names[i]
    inventory.add_item(i, item)

print('Добавили предметы:\n', inventory)

inventory.remove_item(1)
print('Удалили 2 предмет:\n', inventory)


"""
3. Побочный эффект от передачи объектов по ссылке

В данном случае может быть проблема в том, что мы можем изменить значения предметов в инвентаре вне класса инвентаря, 
например:
"""
# Допустим, мы решаем изменить имя предмета вне класса Inventory:
item_to_modify = inventory.items[2].value  # Получаем ссылку на третий предмет Item
item_to_modify.name = "Новое имя"  # Изменяем имя

print('Извне изменили предмет:\n', inventory)

"""
Получилось так, что мы получили ссылку на item_to_modify и изменили атрибут предмета.
Чтобы этого избежать, наверно, список items в Inventory нужно сделать приватным, чтобы нельзя было извне получить доступ
"""
