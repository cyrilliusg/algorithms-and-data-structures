## 1. Наследования вариаций

```FileLogger``` и ```MultiLogger ``` являются ```Logger```.

Родительский класс --```Logger``` обладает методом log, которое куда-то записывает сообщение.

Дочерний класс ```FileLogger``` (функциональная вариация), переопределяет только логику (пишет в файл вместо консоли).

Другой дочерний класс ```MultiLogger``` (вариация типа), может, например, обрабатывать как сообщение, так и список
сообщений. Но прямой перегрузки в Python не существует.

---

## 2. Наследование с конкретизацией (reification inheritance)

```Circle``` (или любая другая фигура) является ```Shape```.

Родительский класс -- ```Shape``` обладает операцией ```area()```, рассчитывающей свою площадь. 
Реализация конкретных расчётов будет реализована у потомков.

---

## 3. Структурное наследование (structure inheritance)
```python
class Point:
    def __init__(self, x: float, y: float):
        self.x, self.y = x, y

    def __lt__(self, other: "Point") -> bool:
        # сортировка по сумме координат
        return (self.x + self.y) < (other.x + other.y)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y
```