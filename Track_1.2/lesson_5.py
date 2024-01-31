"""
Здравствуйте, Сергей Игоревич!

Собственно, скорее всего и ответ на мой предыдущий вопрос о наследовании башни от двух классов: строений, получающих и
наносящих урон - использование композиции, а не наследования.

В данном случае, я бы в качестве абстракции выделил 'принятие урона' и 'нанесение урона'. Принятие и нанесение урона -
это характерные для всех объектов признаки: как для строений, так и для героев, предметов. Класс Attack и Класс Defence.
"""

"""
4.1 Композиция
"""


class Attack:
    """
    Нанесение урона
    """

    def __init__(self, damage):
        self.damage = damage  # урон атакующего субъекта

    def perform_attack(self, target):
        target.defence.take_damage(self.damage)


class Defence:
    """
    Принятие урона
    """

    def __init__(self, base_health):
        self.base_health = base_health  # здоровье принимающего урон субъекта
        self.current_health = base_health
        self.health_modifiers = []  # Список модификаторов здоровья

    def take_damage(self, damage):
        self.current_health -= damage
        if self.current_health <= 0:
            self.on_destroy()

    def increase_health(self, amount):
        self.current_health += amount

    def add_health_modifier(self, modifier):
        self.health_modifiers.append(modifier)
        self.update_health()

    def update_health(self):
        self.current_health = self.base_health
        for modifier in self.health_modifiers:
            self.current_health += modifier

    def on_destroy(self):
        # Логика уничтожения или смерти
        pass


class Building:
    """
    Базовый класс строения
    """

    def __init__(self, x, y, w, l, side):
        # Двухмерные координаты для определения местоположения строения на карте
        self.__x = x
        self.__y = y
        self.__w = w  # ширина постройки
        self.__l = l  # длина постройки
        self._side = side  # сторона Света или Тьмы


class Tower(Building):
    def __init__(self, x, y, w, l, side, health, damage):
        super().__init__(x, y, w, l, side)
        self.defence = Defence(health)
        self.attack = Attack(damage)


class Creep:
    def __init__(self, health, damage):
        self.defence = Defence(health)
        self.attack = Attack(damage)


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

    def foo(self):
        return self.__class__.__name__


class HealItem(Item):
    def __init__(self, name, cost, rarity, health_bonus):
        super().__init__(name, cost, rarity)
        self.health_bonus = health_bonus

    def foo(self):
        return self.__class__.__name__


# Создаем башню
tower = Tower(x=100, y=100, w=100, l=100, side='Radiant', health=500, damage=50)

# Проверка здоровья башни
print(tower.defence.current_health)

# Башня получает предмет, увеличивающий здоровье
health_boost_item = HealItem(name='tango', cost=100, rarity=1, health_bonus=100)
tower.defence.add_health_modifier(health_boost_item.health_bonus)

# Проверка обновленного здоровья башни
print(tower.defence.current_health)

# Крип атакует башню
creep = Creep(health=100, damage=10)
creep.attack.perform_attack(tower)

# Проверка здоровья башни
print(tower.defence.current_health)

"""
4.2. Переопределение родительского класса. Вывод получился таким, что это и есть полиморфизм, а именно - полиморфизм подтипов. 
Мы, не зная какой объект, применяем к нему один и тот же метод.
"""


# Определение родительского класса
class Parent:
    def __str__(self):
        return self.__class__.__name__


# Определение первого дочернего класса. Не переопределил метод (оставил таким же, как у родительского)
class Child1(Parent):
    pass


# Определение второго дочернего класса
class Child2(Parent):
    def __str__(self):
        return "Имя класса Child2"


# для перемешивания списка
import random

# Создание списка из 250 объектов Child1 и 250 объектов Child2
objects_mixed = [Child1() if i < 250 else Child2() for i in range(500)]

# Перемешивание списка
random.shuffle(objects_mixed)

# Проверка первых 10 объектов списка после перемешивания
for obj in objects_mixed[:10]:
    print(obj)
print(objects_mixed[:10])

"""
4.3. Ad hoc полиморфизм. 
Я немного почитал сторонних источников, и пришел к тому, что в Python нельзя реализовать в чистом виде такую концепцию,
поскольку нет 'перегрузки функций'. Но смысл в том, что функция себя ведет по разному в зависимости от типа входных данных.
Наверно, что-то типа такого:
"""


class Circle:
    pass


class Polygon:
    pass


def draw(figure):
    if isinstance(figure, Circle):
        print('Рисуй круг')
    elif isinstance(figure, Polygon):
        print('Рисуй многоугольник')
    else:
        print('Рисуй линию')


for figure in [Circle(), Polygon(), Parent()]:
    draw(figure)
