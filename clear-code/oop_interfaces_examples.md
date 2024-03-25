// 3.1

// 1 - Транспорт. Самый простой пример.

```python
class Car:
    def deliver(self):
        return "Доставка по асфальту"


class Ship:
    def deliver(self):
        return "Доставка по морю"


class TransportFactory:
    @staticmethod
    def get_transport(transport_type: str):
        if transport_type == "car":
            return Car()
        elif transport_type == "ship":
            return Ship()
        else:
            raise ValueError("Неизвестный транспорт")
```

// 2 - продукты

```python
from typing import Type, Dict


class Product:
    def use_product(self):
        pass


class ProductA(Product):
    def use_product(self):
        return "Использование продукта A"


class ProductB(Product):
    def use_product(self):
        return "Использование продукта B"


class ProductFactory:
    def __init__(self):
        self._creators: Dict[str, Type[Product]] = {}

    def register_product(self, product_id: str, creator: Type[Product]):
        self._creators[product_id] = creator

    def create_product(self, product_id: str) -> Product:
        creator = self._creators.get(product_id)
        if not creator:
            raise ValueError(f"ID продукта {product_id} не зарегистрирован.")
        return creator()


# Использование фабрики
factory = ProductFactory()
factory.register_product('A', ProductA)
factory.register_product('B', ProductB)

product_a = factory.create_product('A')

product_b = factory.create_product('B')
```

// 3 - животные

```python
class Pet:
    def speak(self):
        raise NotImplementedError


class Dog(Pet):
    def speak(self):
        return "Woof!"


class Cat(Pet):
    def speak(self):
        return "Meow!"


class PetFactory:
    pet_classes = {}

    @classmethod
    def register_pet(cls, key: str, pet_class: object):
        cls.pet_classes[key] = pet_class

    @classmethod
    def create_pet(cls, animal_type: str):
        pet_class = cls.pet_classes.get(animal_type)
        if pet_class is None:
            raise ValueError("Unknown animal type")
        return pet_class()


# Регистрация классов в фабрике
PetFactory.register_pet("dog", Dog)
PetFactory.register_pet("cat", Cat)

dog = PetFactory.create_pet("dog")
print(dog.speak())
```

// 3.2

// Я разрабатывал GUI для программы, в котором было главное окно и в нём разные вкладки (по типу браузера). Каждая
вкладка содержала разные виджеты и разную логику. Для проектировки различных окон я делал абстрактные классы для
Модели - Контроллера этих окон (MVC). До данного занятия они назывались с префиксом Abstract. Новые названия:

// TabModel

// TabController

// Menu