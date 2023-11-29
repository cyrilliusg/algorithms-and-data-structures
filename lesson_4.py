"""
Здравствуйте, Сергей Игоревич!

Опять немного убежал вперед паровоза и уже в прошлом задании расставил приватность на атрибуты)

У меня, мне кажется, были не совсем удачные для иерархии примеры классов в прошлом задании, поэтому, я предметную
область оставлю ту же, но сущности придумаю новые.

У меня к Вам вопрос, Ваша цитата: "Не выдумывайте никакие абстрактные сущности, только запутаетесь. Возьмите простые
физические вещи, например, автомобиль и двигатель, тарелка и еда, кошелёк и деньги и т. п.." - я правильно понял,что
условно автомобиль может унаследоваться от двигателя или еда от тарелки? Ведь мне кажется это не совсем корректно,
т.к. одно не исходит из другого, скорее двигатель будет атрибутом автомобиля, а сам автомобиль будет наследоваться от
абстрактного 'Vehicle', которым может быть любое транспортное средство, или даже средство с колесами.
Поправьте, пожалуйста, если я неправ.

"""

"""
1 Иерархия: Building - (DestructibleBuilding и  AttackingBuilding) - Barrack(DestructibleBuilding) - Tower (DestructibleBuilding, AttackingBuilding)

Скажите, пожалуйста, на сколько корректно я выделил сущности:
Я взял базовый класс строения, потом разбил его на способное атаковать и разрушаемое (в игре действительно есть строения,
которые могут атаковать и не иметь здоровья, или иметь здоровье и не атаковать, или и атаковать и быть разрушаемыми. И для
такого случая я унаследовался сразу от 2-х классов, но, т.к. они оба исходят из базового Building, то, были трудности с 
инициализацией объекта класса Tower, и пришлось добавлять args и kwargs. 
Самый ли я оптимальный метод выбрал?
"""


class Building:
    """
    Строение
    """

    def __init__(self, x, y, w, l, side):
        # Двухмерные координаты для определения местоположения строения на карте
        self.__x = x
        self.__y = y
        self.__w = w  # ширина постройки
        self.__l = l  # длина постройки
        self._side = side  # сторона Света или Тьмы


class DestructibleBuilding(Building):
    """
    Строение со здоровьем (разрушаемое)
    """

    def __init__(self, x, y, w, l, side, HP, *args, **kwargs):
        super().__init__(x, y, w, l, side, *args, **kwargs)
        self.__HP = HP

    def _get_damage(self, damage):
        if self.__HP - damage <= 0:
            self.__HP = 0
            self.__destruction_animation()
        else:
            self.__HP -= damage

    def _current_hp(self):
        return self.__HP

    def _regeneration(self, regeneration_speed):
        self.__HP += regeneration_speed

    def __destruction_animation(self):
        pass  # запускается анимация разрушения


class AttackingBuilding(Building):
    """
    Строение умеющее атаковать
    """

    def __init__(self, x, y, w, l, side, damage, *args, **kwargs):
        super().__init__(x, y, w, l, side, *args, **kwargs)
        self.__damage = damage  # башня может наносить урон
        self.__attack_speed = 1.0

    def _attack_actor(self):
        return self.__damage * self.__attack_speed


class Tower(DestructibleBuilding, AttackingBuilding):
    """
    Башня - со здоровьем и способностью атаковать
    """

    def __init__(self, x, y, w, l, side, tier):
        # существует 4 уровня башен, у каждой свой урон и здоровье
        if tier == 1:
            damage = 100
            HP = 100
        elif tier == 2:
            damage = 200
            HP = 200
        elif tier == 3:
            damage = 300
            HP = 300
        elif tier == 4:
            damage = 400
            HP = 400
        super().__init__(x, y, w, l, side, HP, damage)

    def get_damage(self, damage):
        self._get_damage(damage)

    def attack_actor(self):
        return self._attack_actor()

    def current_hp(self):
        return self._current_hp()


class Barrack(DestructibleBuilding):
    """
    Казарма
    """

    def __init__(self, x, y, w, l, side, HP=500):  # У всех бараков здоровье всегда 500
        super().__init__(x, y, w, l, side, HP)

        self.__regeneration_speed = 1.0

    def get_damage(self, damage):
        self._get_damage(damage)

    def current_hp(self):
        return self._current_hp()

    def regenerate(self):
        self._regeneration(self.__regeneration_speed)

    def side(self):
        return self._side


barrack = Barrack(100, 100, 200, 200, 'Dire')
tower = Tower(200, 200, 300, 300, 'Radiant', 3)

print(tower.current_hp())
tower.get_damage(100)
print(tower.current_hp())

print(barrack.current_hp())
barrack.get_damage(100)
print(barrack.current_hp())
barrack.regenerate()
print(barrack.current_hp())

print(barrack.side())

"""
2 Иерархия. Предметы. Item - Consumable - Usable
"""


class Item:
    """
    Базовый класс предмета
    """

    def __init__(self, name, cost, rarity):
        self.__name = name
        self.__cost = cost
        self.__rarity = rarity

    def purchase(self):
        return -self.__cost

    def sell(self):
        return self.__cost

    def get_name(self):
        return self.__name

    def get_rarity(self):
        return self.__rarity


class Consumable(Item):
    """
    Расходуемый предмет (не обязательно активный)
    """

    def __init__(self, name, cost, rarity, quantity):
        super().__init__(name, cost, rarity)

        self.__quantity = quantity

    def use(self):
        """
        не активное использование, а уменьшение остатка
        """
        if self.__quantity != 0:
            self.__quantity -= 1

    def stock(self):
        return self.__quantity


class UsableItem(Consumable):  # наследоваться в зависимости от того, расходный(Consumable) или нет (Item).
    """
    Активный предмет
    """

    def __init__(self, name, cost, rarity, quantity, duration):
        super().__init__(name, cost, rarity, quantity)
        self.__duration = duration  # длительность действия в секундах. если без времени, то равно нулю
        # self.__ability = Ability(name) #здесь в качестве атрибута может браться способность по имени предмета

    def activate(self):
        if self.stock() > 1:
            self.use()
            self.__ability()

    def __ability(self):
        print('Здесь логика действий активной способности с учётом времени')


tango = UsableItem('Tango', 150, 1, 3, 0)
print(tango.stock())
tango.use()
print(tango.stock())
