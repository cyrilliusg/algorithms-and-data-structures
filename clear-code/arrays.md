//1. Раньше в своей программе в качестве результата работы метода я возвращал список, где первым значением был
успех/неуспех, а вторым - либо текст ошибки, либо результирующее значение. Плюс иногда дополнительно нужно было
отправлять какой-то признак. Это всё было через списки/кортежи. На паре методов это ещё работает, но при написании
большой программы много возможностей совершить ошибку/опечататься с индексом - что угодно. Поэтому, я сделал отдельный
класс (тип данных) для обмена информацией между методами. 

// Было (пример метода)
```python
def clean_and_validate_dataframe(dataframe: pd.DataFrame) -> Tuple[bool, Union[str, pd.DataFrame]]:
    """
    Проверяет DataFrame на наличие строк и колонок после удаления строк, содержащих только NaN.

    Функция сначала удаляет все строки, которые полностью состоят из NaN. Затем проверяет DF на наличие колонок и строк.
    Если после удаления строк DF не содержит колонок или строк, функция возвращает соответствующее сообщение об ошибке.

    Параметры:
    - data_frame (pd.DataFrame): DataFrame для проверки.

    Возвращает:
        Tuple[bool, Union[str, pd.DataFrame]]. 
        Где первое значение - флаг успех/неуспех, 
        а второе - либо текст ошибки, либо результирующее значение
    """
    # Удаление строк, которые полностью состоят из NaN
    dataframe.dropna(axis=0, how='all', inplace=True)

    # Проверка на отсутствие колонок в DataFrame
    if dataframe.shape[1] == 0:
        return (False, 'Нет колонок')

    # Проверка на отсутствие строк в DataFrame
    if dataframe.shape[0] == 0:
        return (False, 'Нет строк')

    # Возвращение DataFrame, если он прошел все проверки
    return (True, dataframe)
```

// Стало
```python
class ModelInteractionFeedback:
    """
    Класс для инкапсуляции ответа модели контроллеру-интерфейсу.

    Attributes:
        success (bool): Флаг успеха или неудачи операции.
        role (str): код роли (внутренний код каждой модели виджета).
        value (Any): Значение результата при успешной операции.
        error (Any): Текст ошибки при неудаче.
    """

    def __init__(self,
                 success: bool = True,
                 value: Any = None,
                 role: Optional[str] = None,
                 error: Optional[str] = None):

        self.success = success
        self.value = value
        self.role = role
        self.error = error

    def get_role(self) -> str:
        """Возвращает код роли"""
        return self.role

    def is_successful(self) -> bool:
        """Возвращает True, если операция была успешной."""
        return self.success

    def get_value(self) -> Any:
        """Возвращает значение операции, если она была успешной, иначе None."""
        if self.success:
            return self.value
        return None

    def get_error(self) -> str:
        """Возвращает текст ошибки, если операция не была успешной."""
        if not self.success:
            return self.error
        return ""

    def __str__(self):
        return f"ModelInteractionFeedback(is_successful={self.success}, role={self.role}, value={self.value}, error={self.error})"
    
def clean_and_validate_dataframe(dataframe: pd.DataFrame) -> ModelInteractionFeedback:
    """
    Проверяет DataFrame на наличие строк и колонок после удаления строк, содержащих только NaN.

    Функция сначала удаляет все строки, которые полностью состоят из NaN. Затем проверяет DF на наличие колонок и строк.
    Если после удаления строк DF не содержит колонок или строк, функция возвращает соответствующее сообщение об ошибке.

    Параметры:
    - data_frame (pd.DataFrame): DataFrame для проверки.

    Возвращает:
        ModelInteractionFeedback: В случае успеха возвращает value - преобразованный DataFrame с данными.
                                  В случае ошибки возвращает error - строка с описанием ошибки.
    """
    # Удаление строк, которые полностью состоят из NaN
    dataframe.dropna(axis=0, how='all', inplace=True)

    # Проверка на отсутствие колонок в DataFrame
    if dataframe.shape[1] == 0:
        return ModelInteractionFeedback(False, error='Нет колонок')

    # Проверка на отсутствие строк в DataFrame
    if dataframe.shape[0] == 0:
        return ModelInteractionFeedback(False, error='Нет строк')

    # Возвращение DataFrame, если он прошел все проверки
    return ModelInteractionFeedback(True, value=dataframe)
```


//2. Использование стека для реализации буфера обмена. Ниже два базовых класса для буфера.

```python
class Stack:
    """Базовый класс Стека"""

    def __init__(self):
        self.stack = []

    def push(self, item: Any):
        """Добавление в стек"""
        self.stack.append(item)

    def pop(self) -> Any:
        """Возвращение последнего элемента (None если стек пустой)"""
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def __len__(self) -> int:
        """Размер стека"""
        return len(self.stack)

    def clear(self):
        """Очистить стек"""
        self.stack.clear()

    def __str__(self):
        return str(self.stack)


class CommandStack:
    """Буфер обмена"""

    def __init__(self):
        self.redo_stack = Stack()  # стек для повтора
        self.undo_stack = Stack()  # стек для отмены

    def add_command(self, action: Union[CreateCommand, UpdateCommand, DeleteCommand]):
        """добавить команду в буфер"""
        self.undo_stack.push(action)
        self.redo_stack.clear()  # Очищаем redo_stack, потому что новое действие изменяет контекст

    def undo(self) -> Union[None, CreateCommand, UpdateCommand, DeleteCommand]:
        """отменить последнее действие"""
        last_command = self.undo_stack.pop()
        if last_command is not None:
            self.redo_stack.push(last_command)
        return last_command

    def redo(self) -> Union[None, CreateCommand, UpdateCommand, DeleteCommand]:
        """повтор последнего отмененного действия"""
        last_command = self.redo_stack.pop()
        if last_command is not None:
            self.undo_stack.push(last_command)
        return last_command

    def clear_buffer(self):
        """очистить буфер"""
        self.redo_stack.clear()
        self.undo_stack.clear()
```


//3. Использование итерации по списку без индексации. Итерация происходит по списку с  колонок.
```python
def find_perimeter_and_remove_extra_columns(form_df: pd.DataFrame) -> ModelInteractionFeedback:
    """
    Удаляет из DataFrame колонки в заданном диапазоне, не содержащие определенный символ.

    Args:
    df (pd.DataFrame): Исходный DataFrame, в котором будет произведена фильтрация.

    Returns:
        ModelInteractionFeedback: В случае успеха возвращает value - DataFrame с удаленными колонками,
                                    не содержащими указанный символ в заданном диапазоне.
                                  В случае ошибки возвращает error - строка с описанием ошибки.
    """

    # Определение колонок для проверки
    indices_to_check = range(Constants.PERIMETER_START_COL, Constants.PERIMETER_END_COL + 1)
    indices_with_symbol = []

    # Поиск индексов колонок с символом
    for index in indices_to_check:
        column_name = form_df.columns[index]
        if form_df[column_name].astype(str).str.contains(Constants.PERIMETER_SYMBOL).any():
            indices_with_symbol.append(index)

    if not indices_with_symbol:
        return ModelInteractionFeedback(False, error=f"Не заполнено поле 'Периметр'")

    if len(indices_with_symbol) > 1:
        return ModelInteractionFeedback(False, error=f"Поле 'Периметр' заполнено более 1 раза")

    perimeter_col_name = form_df.columns[indices_with_symbol[0]]
    perimeter_name = form_df[perimeter_col_name].iloc[0]
    form_df[perimeter_col_name] = perimeter_name

    # Определение индексов колонок для удаления
    indices_to_drop = [index for index in indices_to_check if index not in indices_with_symbol]

    # Удаление колонок по их порядковым номерам 
    df_filtered = form_df.drop(form_df.columns[indices_to_drop], axis=1)

    return ModelInteractionFeedback(True, value=df_filtered)
```

