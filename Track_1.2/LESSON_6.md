## Отчёт по 6 заданию
___

#### Была создана простая функция с четырьмя инпутами разных типов данных и на двух языках.

* Через командную строку сменил директорию, запустил файл, выполнил все инструкции. Результат:

![Результат работы программы](https://github.com/cyrilliusg/High-School-of-Programming/blob/main/images/screenshots/lesson_6.PNG)


### Исходный код:
```python
def IO_function():
    # Integer input
    int_val = int(input("Введите число: "))
    print(f"Введённое числовое значение: {int_val}")

    # Float input
    float_val = float(input("Введите дробное число: "))
    print(f"Введёное дробное значение: {float_val}")

    # Rus string input
    str_val = input("Введите строку на русском языке: ")
    print(f"Введённая строка на русском языке: {str_val}")

    # Eng string input
    str_val = input("Enter a string using eng symb: ")
    print(f"English string output: {str_val}")

IO_function()




```




