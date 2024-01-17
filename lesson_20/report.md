# Отчёт о Пользовании Линтёром

#### Выбранный инструмент: Плагин Pylint в рамках IDE PyCharm

#### Тестовый код: класс DirectoryProcessor из 15 урока, в котором создаются и удаляются директории с файлами


В PyCharm по умолчанию уже встроена базовая проверка кода, поэтому, критических ошибок практически не было,
но, парочка всё же встретилась.

![Скриншот с ошибками линтёра](https://github.com/cyrilliusg/High-School-of-Programming/blob/main/lesson_20/error_logs.PNG)

1. Вызывал метод открытия файла 'open()' без конструкции 'with':

```python
open(os.path.join(os.getcwd(), folder_name, 'temp_file.txt'), 'w')
```

2. В аргументе метода была переменная 'dir_path', которую я ниже по коду метода переопределил в цикле:

```python
    def get_result(self, dir_path: str, end_file: str, flag: bool) -> list:


    self._check_directory_exists(dir_path)
...
target_dirs = [dir_path]
...
for dir_path in target_dirs:  # переопределил dir_path
    ...
```

3. В вызове метода 'open()' не был указан аргумент с типом кодировки файла:

```python
open(os.path.join(os.getcwd(), folder_name, 'temp_file.txt'), 'w')  # encoding='UTF-8'
```

4. В перехвачивании ошибки ('except') не указан явный тип ошибки, а просто любая ошибка ('Exception as e'):

```python
try:
    file_path = os.path.join(root, file)
    os.unlink(file_path)
except Exception as e:
    print(f"Ошибка при удалении файла: {e}")
    return False
```

5. Ну и остальные, менее примечательные ошибки, по типу:
    * Длина строки с комментарием
    * Ненужное использование f строки (без переданных аргументов)
    * Отсутствие документации к классу

**Конечно, встроенная проверка ошибок в PyCharm не покрывает данные ошибки, поэтому,
дополнительное пользование линтёром, безусловно, улучшает качество кода.**

