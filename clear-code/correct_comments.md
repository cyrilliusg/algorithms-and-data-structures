// 1. Информативные комментарии. Было:

```python
# Получаем индексы ошибочных строк
incorrect_indexes = self.find_wrong_values_indexes(df)
```

//После: Комментарий можно убрать, переименовав функцию для большей ясности.

```python
incorrect_indexes = self.get_error_row_indexes(df)
```

// 2.Представление намерений. До:

```python
# Проверка только числовых фильтров
if row['Condition'] in self.condition_types['digit']:
```

//После: Изменить структуру условия для отражения намерений без комментария.

```python
if self.is_digit_filter(row['Condition']):
```

// 3.Прояснение. До:

```python
# Применяем функцию исправления и выводим результаты
corrections = self.correct_values(df, incorrect_indexes)
```

//После: Улучшить название функции и параметров для самоописания без комментария.

```python
corrections = self.apply_corrections_and_return_results(df, incorrect_indexes)
```

// 4. Предупреждения о последствиях

```python
# если индексов нет
if not incorrect_indexes:
    return False
```

//После: Использовать более понятное название переменной и структуры кода.

```python
if self.indexes_are_empty(incorrect_indexes):
    return False

```

// 5. Усиление. До:

```python
# Список для хранения индексов ошибочных строк
incorrect_rows = []
```

//После: Убрать комментарий, название переменной уже достаточно информативно.

```python
incorrect_rows = []
```

// 6. Усиление важности условий. До:

```python
# Устанавливаем наиболее строгие условия
conditions["Больше"] = [max(greater_than, greater_or_equal)] if greater_than != float(
    '-inf') or greater_or_equal != float('-inf') else []
```

//После: Убрать комментарий и ввести вспомогательную функцию для улучшения читаемости.

```python
conditions["Больше"] = self.define_stricter_conditions(greater_than, greater_or_equal)
```

// 7. Пояснение сложной логики

```python
       comparison_operations = {
    'Больше': lambda a, b: a < b,
    'Больше или равно': lambda a, b: a <= b,
    'Меньше': lambda a, b: a > b,
    'Меньше или равно': lambda a, b: a >= b
}

if (filter_a in ['Больше', 'Больше или равно'] and filter_b in ['Меньше', 'Меньше или равно']) or
        (filter_a in ['Меньше', 'Меньше или равно'] and filter_b in ['Больше', 'Больше или равно']):
    return comparison_operations.get(filter_a, lambda a, b: False)(value_a, value_b) and
        comparison_operations.get(filter_b, lambda a, b: False)(value_b, value_a)

return True  # Если ни одно из условий выше не сработало, фильтры согласованы


```

//После: Оформить блок кода в функцию с понятным названием, чтобы избежать дополнительных комментариев.

```python
return self.are_filters_consistent(condition1, condition2)
```

// 8. Прояснение использования регулярных выражений. До:

```python
self.regex = re.compile(r'^-?(\d*[\.,]?\d*%?)$')
```

//После: Объяснить назначение регулярного выражения в названии переменной.

```python
self.numeric_value_with_optional_percent_regex = re.compile(r'^-?(\d*[\.,]?\d*%?)$')
```

// 9. Прояснение

```python
# Если условия несовместимы (противоречат друг другу), добавляем их в список противоречий
if not is_consistent:
    conflicts.append((condition1, condition2))
```

//После: Включить причину добавления в список противоречий в саму функцию проверки согласованности.

```python
if self.conditions_conflict(condition1, condition2):
    conflicts.append((condition1, condition2))
```

// 10. Предупреждения о последствиях

```python
# Уменьшаем на 1 для преобразования в "Больше"
greater_or_equal -= 1 if greater_or_equal > 0 else 0
```

//После: Улучшить логику преобразования, чтобы она была яснее без комментария.

```python
greater_or_equal = self.adjust_for_strict_greater_comparison(greater_or_equal)
```

// 11. Прояснение назначения метода

```python
# Публичный метод по добавлению строки. Получает словарь, где ключи - индексы колонок, а значения - значения
def add_new_row(self, options: dict):
    ...
```

//После: Сократить комментарий, интегрировав информацию в название метода и аргументы.

```python
def add_new_row_by_column_indices(self, column_values: dict):
    ...
```

// 12.Информативные комментарии к сложным операциям

```python
# если диапазон вставки меньше буфера
if self.copy_clipboard.determine_case(self.copy_clipboard.data(), selected_ranges) == 3:
    # то создаём новый диапазон вставки на размер буфера, и, по сути, приводим к 0 случаю, когда диапазоны равны
    selected_ranges = self._create_new_past_range_df(self.copy_clipboard.increase_range(selected_ranges))
```

//После: Включить более подробное описание в название метода и избавиться от внутренних комментариев.

```python
if self.is_paste_range_smaller_than_buffer(selected_ranges):
    selected_ranges = self.create_expanded_paste_range(selected_ranges)
```