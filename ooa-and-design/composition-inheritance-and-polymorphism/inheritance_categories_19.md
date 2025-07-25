## 1. Наследование подтипов (subtype inheritance)

```Dog``` и ```Cat ``` являются ```Animal```.

Родительский класс -- ```Animal``` обладает базовым набором операций.
Дочерние классы  переопределяют исходный тип.
---

## 2. Наследование с ограничением (restriction inheritance)

```SavingsAccount``` и ```StudentAccount ``` являются ```BankAccount```.

Родительский класс -- ```BankAccount``` обладает базовым набором операций (внести, снять, проверить баланс).
Дочерние классы  ограничивают исходный тип:

- ```SavingsAccount``` – сберегательный счёт. Минимум остатка не может опускаться ниже заданной суммы.
- ```StudentAccount ``` – студенческий счёт. Ограничения на макс. остаток, возвраст владельца, и прочее.


---

## 3. Наследование с расширением (extension inheritance)

```AutonomousVehicle``` является ```Vehicle```.

Родительский класс -- ```Vehicle``` обладает базовым набором свойств (скорость, тип двигателя, наличия водителя).
Дочерний класс ```AutonomousVehicle``` расширяет исходный тип: автономное транспортное средство, движущееся без участия водителя.
