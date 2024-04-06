//1. Связывание переменной во время запуска программы. Метод анализирует проводник пользователя и строит путь к БД на
диске пользователя. Выбор связи значения с переменной во время запуска программы очевиден: конечные запуски программы 
будут производиться на разных ПК и необходимо каждый раз его строить заново.

```python
class Settings:
    def __init__(self):
        self.data_db_path = PathBuilder.get_db_data_path()


class PathBuilder:

    @staticmethod
    def get_db_data_path() -> str:
        """
        Возвращает абсолютный путь к основному файлу данных базы данных (data) внутри директории базы данных.

        Возвращает:
            str: Полный путь к основному файлу данных базы данных.
        """
        db_directory_path = PathBuilder.get_db_directory_path()
        return os.path.join(db_directory_path, DataBaseConstants.DATA_NAME)


... Остальные методы по работе с директориями пользователя
```


//2. Связывание значения и переменной во время компиляции. Эта часть кода отвечает за получение некоторых данных 
для дальнейшего отображения их в интерфейсе (информация о пользовательской сессии). 
В этой части кода производится запрос к БД, получается статус сессии. Отображение информации будет происходить только 
если сессия готова к работе. Неготовность сессии - это либо ошибка при создании, либо незавершенное создание. 
Сами коды статусов готовности заведены в БД, но всё равно для задания какого-то поведения в программе, 
их необходимо отдельно определять в коде. Такие значения я вынес в класс с константами, с названием класса, аналогичному 
названиям таблиц в БД, и в коде ниже их использовал.
И также были использованы константы для управления виджетом, отображающим информацию. он может работать в режиме, 
когда у него посередине только один лейбл с надписью ошибки, либо же с большим числом виджетов для отображения 
разной информации. В данном случае, поскольку информации нет, точно так же используется константа 
для задания роли поведения этому виджету.


```python
class SessionStatus:
    DATA_SOURCE = 0
    FILE_MANAGER = 1
    CHOOSE_COMPANIES = 2
    CHOOSE_LOCATIONS = 3
    COMPANIES_PROPERTIES = 4
    REMATCHING = 5
    ERROR = 6
    READY = 7

class PivotDataConstants:
    UI_ROLE_BANNER = '0'
    UI_ROLE_PROPERTY = '1'
    
model_response = self.get_session_status(selected_row_session_id)
if not model_response.is_successful():
   return model_response
session_status_id = model_response.get_value()

if session_status_id == SessionStatus.ERROR:
   return ModelInteractionFeedback(True, value='Ошибка при создании. Нет информации',
                                   role=PivotDataConstants.UI_ROLE_BANNER)

if session_status_id != SessionStatus.READY:
   return ModelInteractionFeedback(True, value='Необходимо завершить создание. Нет информации.',
                                   role=PivotDataConstants.UI_ROLE_BANNER)
```



//3. Связывание переменной и значения во время написания кода. В данном примере производится обращение к общему методу 
для исполнения update запроса к БД и текст запроса присвоен переменной непосредственно перед исполнением. Поскольку,
это текст на другом ЯП - это не считается магической переменной.

```python
 def set_source_raw_data_id(self, session_id: int, source_raw_data_id: int) -> DbOperationResult:
   """Установить новый источник данных для сессии по её id и id источника данных"""
     query_text = "UPDATE session SET source_raw_data_id = (:source_raw_data_id) WHERE id = (:id)"
     return self.update(query_text,
                                  user_error_text=f'{self.set_source_raw_data_id.__name__}\n'
                                                  'Не удалось записать тип источника данных',
                                  source_raw_data_id=source_raw_data_id,
                                  id=session_id)
```