//Я взял за пример одну из моих программ. Она с GUI. В программе считываются excel-файлы, в файлах данные о персонале
компаний. Программа для анализа данных - в таблицах данные редактируются, формируются отчёты,
потом их выгружают обратно в excel. То есть это такой аналитический инструмент.

//Использование констант вместо магических строк. До:

```python
df = pandas.read_excel(path, sheet_name='3. Зарплатные данные', usecols="A:H,J:AA", decimal=",")
```

//После:

```python
SHEET_NAME = '3. Зарплатные данные'
USE_COLS = "A:H,J:AA"
DECIMAL = ","
df = pd.read_excel(path, sheet_name=SHEET_NAME, usecols=USE_COLS, decimal=DECIMAL)
```

//Использование Decimal для повышения точности финансовых расчетов. До:

```python
df[col] = df[col].astype(float)
```

//После:

```python
from decimal import Decimal

df[col] = df[col].apply(lambda x: Decimal(x))
```

// Проверка на наличие нежелательных значений с использованием констант. До:

```python
unwanted_values = df[~df['bonus_eligibility'].isin(['да', 'нет'])]
```

//После:

```python
VALID_BONUS_ELIGIBILITY = ['да', 'нет']
unwanted_values = df[~df['bonus_eligibility'].isin(VALID_BONUS_ELIGIBILITY)]
```

//Вынос текста sql-запроса в отдельную переменную в максимальной близости к использованию. До:

```python
allcodes_df = pandas.read_sql_query(f"""SELECT COUNT (DISTINCT code)...""")
```

//После:

```python
query_text_allcodes = f"""SELECT COUNT (DISTINCT code)..."""

allcodes_df = pandas.read_sql_query(query_text_allcodes, ...)
```

//Избегание магических чисел. До:

```python
if len(group) > 5:
    # некоторое действие
    pass
```

//После:

```python
MIN_GROUP_SIZE = 5
if len(group) > MIN_GROUP_SIZE:
    # некоторое действие
    pass

```

// Часть кода из алгоритма исправления ошибок в данных. Обрабатываем знаменатель в делении, исправляем названия
переменных. До:

```python
filtered_rawdata = df_rawdata[df_rawdata['code'] == code]  # берём записи с ошибочным кодом
total_rows = len(filtered_rawdata)  # всего записей по коду
filtered_rawdata = filtered_rawdata[filtered_rawdata['AFP'].notna()]  # оставляем только записи с бонусом
total_AFP = len(filtered_rawdata)  # кол-во записей с бонусом
min_remaining_AFP = total_AFP * 100 / total_rows  # % записей с бонусом от общего кол-ва записей по коду
```

//После:

```python
# Фильтрация данных по вычисленному выше коду
filtered_data_by_code = df_rawdata[df_rawdata['code'] == code]

# Подсчёт общего числа записей для данного кода
total_entries_by_code = len(filtered_data_by_code)
if total_entries_by_code == 0:
    pass  # Обработка ситуации отсутствия записей
    # Может быть return или continue

# Оставляем только записи с указанными значениями в поле 'AFP'
data_with_AFP = filtered_data_by_code[filtered_data_by_code['AFP'].notna()]

# Подсчёт записей с указанными значениями в 'AFP'
total_entries_with_AFP = len(data_with_AFP)

# Расчёт процента записей с 'AFP' от общего числа записей по данному коду
percentage_of_AFP_entries = total_entries_with_AFP * 100 / total_entries_by_code

```