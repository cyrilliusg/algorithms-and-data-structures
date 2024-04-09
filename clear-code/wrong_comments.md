// 1. Было: Избыточные комментарии

```python
# Подключаем слоты для кнопок
self.table_widget.create_button.clicked.connect(self.create_session)
self.table_widget.edit_button.clicked.connect(self.edit_session)
self.table_widget.delete_button.clicked.connect(self.delete_session)
self.table_widget.load_button.clicked.connect(self.load_session)
```

//После: Комментарий просто утверждает очевидное, что и так понятно из вызовов метода connect(). Этот комментарий можно
удалить

// 2. Было: Шум

```python
# Виджет с таблицей и кнопками управления
self.table_widget = SessionTableWidget()
```

//После: Комментарий не добавляет новой информации к названию переменной table_widget, которое и так ясно указывает на
его функционал. Такой комментарий можно считать "шумом" и удалить.

// 3. Было: Бормотание

```python
def delete_extra_rows(form_df: pd.DataFrame) -> pd.DataFrame:
    # Фильтруем DataFrame, оставляя только строку с указанным индексом
    filtered_df = form_df.loc[[Constants.DATA_ROW_INDEX]]

    return filtered_df
```

//После:Комментарий в функции повторяет то, что и так очевидно из кода. Лучше его удалить или написать новый для
объяснения, почему важно оставить только одну строку, поскольку это не очевидно сразу.

// 4. Было: Шум

```python
merged_df.rename(columns={'id_x': 'attribute_report_id'}, inplace=True)

# Преобразуем form_df в нужный формат
form_df_melted = form_df.melt(var_name='sys_name', value_name='value')
```

//После:этот комментарий повторяет, что делает метод melt() без добавления какой-либо
новой информации. Комментарий можно убрать.

// 5. Было: Шум

```python
# устанавливаем колонки в df в соответствии с установленным порядком
dataframe.columns = attributes_info[DataDefinitions.AttributeTableFields.SYSTEM_NAME].tolist()
```

//После: Этот комментарий просто повторяет, что делает код, не добавляя новой информации. Его можно опустить или
заменить комментарием, объясняющим, почему порядок колонок важен для последующих операций.

// 6. Было: Неочевидные комментарии

```python
# список хранящий первичные ключи со строками, для которых уже было предупреждение о редактировании
self.already_warned_rows = []
```

//После:

```python
# Список ID строк, для которых пользователь уже видел предупреждение о редактировании данных.
self.already_warned_rows = []
```

// 7. Было: Шум

```python
def get_rawdata_type(self, session_id: int) -> Optional[str]:
    """Получить тип источника данных"""
    db_response = self.db_model.get_rawdata_type(session_id)
```

//После: комментарий дублирует название метода, не добавляя полезной информации.

```python
# Возвращает тип данных текущей сессии, идентифицированный по session_id
```

// 8. Было: Избыточные комментарии

```python
# в нём хранится отпечаток таблицы при открытии окна
self.file_manager_state_before_changes: Optional[pd.DataFrame] = None
```

//После: Комментарий описывает очевидное предназначение переменной. Удалить

// 9. Было: Нелокальная информация

```python
# Если тип данных анкета, то проверяем имя анкеты
if self.source_data_type == FileManagerConstants.QUESTIONNAIRE:
    model_response = self._process_questionnaire_name(file_path)
```

//После: Комментарий раскрывает детали имплементации, которые могут быть лучше описаны в самом методе проверки.
Лучше перенести комментарий непосредственно в метод _process_questionnaire_name, уточнив его действие в контексте
использования.

// 10. Было: Плохой комментарий:

```python
# получаем все первичные ключи file manager
all_file_manager_pks = self.get_all_pk(self.session_id)
```

//После:  Комментарий просто повторяет код без добавления новой информации.

```python
# Получение списка всех первичных ключей файлов, связанных с текущей сессией, для их последующей обработки.
all_file_manager_pks = self.get_all_pk(self.session_id)
```

// 11. Было: Плохой комментарий

```python
# если нет первичных ключей и выключено уведомление (вызов из главного sessionwizard)
if not all_file_manager_pks:
    return [ModelInteractionFeedback(True)]
```

//После: комментарий размещен в нелогичном месте, что может вызвать путаницу при чтении кода.

```python
# Проверка на отсутствие файлов в file manager для данной сессии. Если файлы отсутствуют, возвращается успешный результат без ошибок.
if not all_file_manager_pks:
    return [ModelInteractionFeedback(True)]
```

// 12. Было: Плохой комментарий

```python
# Сбросить все флаги для уведомлений
self.file_deletion_alert = False
self.target_list_alert = False
```

//После:  Комментарий не дает понимания о том, когда и почему нужно сбрасывать эти флаги.

```python
# Сброс флагов уведомлений при начале новой операции для избежания ложных предупреждений на основе предыдущего состояния.
self.file_deletion_alert = False
self.target_list_alert = False
```

// 13. Было: Плохой комментарий

```python
# Добавляем информацию
self.raw_data_attributes_info = model_response.get_value()
```

//После:  Комментарий не объясняет, какую именно информацию добавляют и для чего она используется.

```python
# Сохранение информации о структуре данных файла в переменную.
self.raw_data_attributes_info = model_response.get_value()
```

// 14. Было: Плохой комментарий

```python
# Проверяем
if not db_response.is_successful():
    QMessageBox.critical(None, 'Ошибка', db_response.get_error())
```

//После:  Слишком неспецифичный и малоинформативный комментарий.

```python
# Проверка успешности выполнения запроса к базе данных и вывод сообщения об ошибке в случае неудачи.
if not db_response.is_successful():
    QMessageBox.critical(None, 'Ошибка', db_response.get_error())
```

// 15. Было: Плохой комментарий

```python
# Сохраняем путь
db_response = self.db_model.set_path(self.session_id, file_path)
```

//После:  Комментарий не поясняет, зачем и в каком контексте происходит сохранение пути.

```python
# Регистрация пути к файлу в базе данных для управления доступом к файлу в рамках сессии.
db_response = self.db_model.set_path(self.session_id, file_path)
```