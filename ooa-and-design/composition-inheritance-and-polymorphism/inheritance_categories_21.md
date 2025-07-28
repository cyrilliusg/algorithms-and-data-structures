## 1. Наследование реализации

```Car``` является ```BaseVehicle```.

Родительский класс ```BaseVehicle``` обладает методами ```start()``` и ```stop()```. Дочерний класс ```Car```
полностью наследует методы базового класса без изменений.

```python
class BaseVehicle:

    def start(self) -> None:
        print("Двигатель заведён (BaseVehicle.start)")

    def stop(self) -> None:
        print("Двигатель остановлен (BaseVehicle.stop)")


class Car(BaseVehicle):
    def open_trunk(self) -> None:
        print("Багажник открыт")
```

---

## 2. Льготное наследование

```Bicycle``` (или любое другое средство передвижения) является ```VehicleInterface```.

Родительский класс ```VehicleInterface``` -- АТД и обладает лишь спецификацией: ```move()``` и ```stop()```.
Реализация этих методов будет у наследников -- ```Bicycle``` наследует только интерфейс.

```python
from abc import ABC, abstractmethod


class VehicleInterface(ABC):
    """
    АТД транспортное средство
    """

    @abstractmethod
    def move(self) -> None:
        """Переместиться вперёд"""
        pass

    @abstractmethod
    def stop(self) -> None:
        """Остановиться"""
        pass


class Bicycle(VehicleInterface):
    """
    Реализация АТД
    """

    def move(self) -> None:
        print("Крутить педали вперед")

    def stop(self) -> None:
        print("Нажат тормоз")
```