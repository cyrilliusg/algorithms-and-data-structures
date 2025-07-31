## Наследование вида

```python
from abc import ABC, abstractmethod


# Иерархия по виду напитка
class Drink(ABC):
    """АТД Напиток: задаёт интерфейс метода name()."""

    @abstractmethod
    def name(self) -> str:
        pass


class Espresso(Drink):
    def name(self) -> str:
        return "Espresso"


class Latte(Drink):
    def name(self) -> str:
        return "Latte"


class Cappuccino(Drink):
    def name(self) -> str:
        return "Cappuccino"


# Иерархия по размеру чашки
class CupSize(ABC):
    """АТД Размер чашки: метод volume_ml()."""

    @abstractmethod
    def volume_ml(self) -> int:
        pass


class Small(CupSize):
    def volume_ml(self) -> int:
        return 200


class Medium(CupSize):
    def volume_ml(self) -> int:
        return 300


class Large(CupSize):
    def volume_ml(self) -> int:
        return 400


# Класс заказа содержит оба критерия
class CoffeeOrder:
    def __init__(self, drink: Drink, size: CupSize):
        self.drink = drink  # has-a Drink
        self.size = size  # has-a CupSize

    def serve(self) -> None:
        print(f"Serving {self.size.volume_ml()} ml of {self.drink.name()}")

```