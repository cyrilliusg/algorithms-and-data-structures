//Я взял за пример одну из моих программ. Она с GUI. В программе считываются excel-файлы, в файлах данные о персонале
компаний. Программа для анализа данных - в таблицах данные редактируются, формируются отчёты,
потом их выгружают обратно в excel. То есть это такой аналитический инструмент.

// Данный пример до/после - достаточно масштабный, покрывает несколько разных тем. Ниже я выделю их.

//Метод из класса-контроллера главного окна со сменяющимися вкладками - шагами создания отчёта. До:

```python
def handle_request(self, request: dict):  # Использование словаря вместо собственной структуры данных
    """Базовый метод. принимает сигнал от главного окна сессии с кнопками вперед - назад.
    Общается с моделью, отправляет выбор в неё для анализа. и далее распределяет дальнейшее управление"""

    direction = request['code']  # Использование словаря
    current_window = self.view.stacked_widget.widget(self.model.current_page())

    if direction == '1':  # 1 - Далее, 0 - Назад. Неявное объявление переменной
        user_choice = current_window.controller.get_user_choice()
        # Использование кортежа вместо собственной структуры данных и Неявное объявление переменной. 
        if user_choice[1] is True:
            # Булева переменная: уводить в другой поток вычисление (при долгом процессе) или нет.
            # Плохое название методов, не отражающее однозначно полноту действий.
            self.init_worker(params=current_window.controller.get_user_choice())
        else:
            self.model.user_choice(user_choice)
    else:
        self.open_new_page(direction)
```
//Метод после изменений:
```python
def handle_request(self, request: UserInteractionFeedback): #принимаем не словарь, а объект класса UserInteractionFeedback (описан ниже)
    """Базовый метод. принимает сигнал от главного окна сессии с кнопками вперед - назад.
    Общается с моделью, отправляет выбор в неё для анализа. и далее распределяет дальнейшее управление"""

    current_window = self.view.stacked_widget.widget(self.model.current_page())

    direction = request.get_operation_code() # с помощью getter-a извлекаем код операции
    
    if direction == SessionWizardConstants.CODE_NAVIGATE_BACKWARD:  # Назад. Константа
        self.open_new_page(direction)
        
    # Более понятное название переменной
    user_input_data = current_window.controller.extract_user_selection()
    # с помощью getter-a извлекаем описание процесса (долгое или быстрое) и сравниваем с константной.
    if user_input_data.get_process_type() == SessionWizardConstants.LONG_PROCESS:
        # Более понятное название метода.
        self.launch_background_task(params=user_input_data)
    else:
        # Иначе без нового потока просто напрямую передаём в модель.
        self.model.process_user_input_data(user_input_data)

        
```
//Явная инициализация всех ранее неявно объявленных переменных (создал отдельный класс с константами для каждой модели).

```python
class SessionWizardConstants:
    DEFAULT_SESSION_ID = 1

    LONG_PROCESS = True
    FAST_PROCESS = False
    
    UI_ROLE_UPDATE = 'new'
    UI_ROLE_NOTICE = 'notice'

    NOTICE_QUESTION_TEXT = 'Изменение данных влечёт за собой стерение всех сделанных шагов.'
    'Вы уверены, что хотите продолжить?'

    WINDOW_TITLE = 'Мастер создания сессии'
    BACK_BUTTON_TEXT = 'Назад'
    NEXT_BUTTON_TEXT = 'Вперёд'
    CODE_NAVIGATE_FORWARD = 1
    CODE_NAVIGATE_BACKWARD = 0
    
    LAST_WINDOW_INDEX = 5
    FIRST_WINDOW_INDEX = 0
    
    WINDOW_NAVIGATION_STEP = 1
    
    DATA_SOURCE_WINDOW = 0
    FILE_MANAGER_WINDOW = 1
    CHOOSE_COMPANIES_WINDOW = 2
    CHOOSE_LOCATIONS_WINDOW = 3
    PIVOT_DATA_WINDOW = 4
    
    MINIMUM_SCENARIO = [DATA_SOURCE_WINDOW,
                        FILE_MANAGER_WINDOW,
                        PIVOT_DATA_WINDOW]
    
    RAWDATA_WITH_LOCATIONS_SCENARIO = [DATA_SOURCE_WINDOW,
                                       FILE_MANAGER_WINDOW,
                                       CHOOSE_LOCATIONS_WINDOW,
                                       PIVOT_DATA_WINDOW]
    
    RAWDATA_WITH_COMPANIES_SCENARIO = [DATA_SOURCE_WINDOW,
                                       FILE_MANAGER_WINDOW,
                                       CHOOSE_COMPANIES_WINDOW,
                                       PIVOT_DATA_WINDOW]
    
    SURVEY_RAWDATA_SCENARIO = [DATA_SOURCE_WINDOW,
                               FILE_MANAGER_WINDOW,
                               CHOOSE_COMPANIES_WINDOW,
                               CHOOSE_LOCATIONS_WINDOW,
                               PIVOT_DATA_WINDOW]
```

//Создание класса для организации обмена 'сообщениями' между виджетами
```python
class UserInteractionFeedback:
    """
    Класс для инкапсуляции результата выбора пользователя.

    Attributes:
        success (bool): Флаг успеха или неудачи операции.
        operation_code (str): код действия (внутренний код каждой модели виджета).
        process_type (str): Тип процесса ('LONG_PROCESS' или 'SHORT_PROCESS').
        value (Any): Значение результата при успешной операции.
        error (Any): Текст ошибки при неудаче.
    """

    def __init__(self, success: bool,
                 operation_code: str,
                 process_type: str = SessionWizardConstants.FAST_PROCESS,
                 value: Any = None,
                 error: Optional[str] = None):

        self.success = success
        self.operation_code = operation_code
        self.process_type = process_type
        self.value = value
        self.error = error

    def get_operation_code(self) -> str:
        """Возвращает код операции"""
        return self.operation_code

    def is_successful(self) -> bool:
        """Возвращает True, если операция была успешной."""
        return self.success

    def get_value(self) -> Any:
        """Возвращает значение операции, если она была успешной, иначе None."""
        if self.success:
            return self.value
        return None

    def get_error(self) -> str:
        """Возвращает текст ошибки, если операция не была успешной, иначе пустая строка."""
        if not self.success:
            return self.error
        return ""

    def get_process_type(self) -> str:
        """Возвращает тип процесса."""
        return self.process_type

    def __repr__(self):
        return f"UserChoiceResult(is_successful={self.success}, process_type='{self.process_type}', value={self.value}, error={self.error})"
```