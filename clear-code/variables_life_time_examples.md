//Я взял за пример одну из моих программ. Она с GUI. В программе считываются excel-файлы, в файлах данные о персонале
компаний. Программа для анализа данных - в таблицах данные редактируются, формируются отчёты,
потом их выгружают обратно в excel. То есть это такой аналитический инструмент.

// Данный пример до/после - примерно годовой давности, достаточно масштабный, покрывает несколько разных тем. Ниже я
выделю их.

//Ранее, процесс считывания файла и данных из него был одной 'длинной колбасой' с перемешкой логики из разных зон
ответственности в одном пространстве (плюс плохие названия переменных, плюс куча магических переменных, в общем
стилистика нулевая).

Часть кода ДО (комментариями пометил ключевые моменты):

```python
if self.ui.radioButton_sector.isChecked():  # Сигнал из интерфейса

    files_list = os.listdir(path)  # Работа с проводником
    anketas = []
    sectorName = path.split('/')[-1].lower()

    for file in files_list:
        if (file.endswith('.xlsx')):
            anketas.append(file.split('.')[0].lower())
    if len(anketas) == 0:
        error_box("В папке нет анкет")  # Действие для интерфейса
        self.setEnabled(True)
        return
    anketas = [client_id for client_id in anketas if client_id.split("_")[0] not in current_clients]
    if len(anketas) == 0:
        error_box("Все анкеты из папки уже есть в памяти")  # Действие для интерфейса
        self.setEnabled(True)
        return

geography = pd.read_sql_query("SELECT id AS location_id, city, region, district AS federal_district FROM location",
                              conn)  # Запрос к БД
for client_id in anketas:
    path = self.path + '/' + client_id + '.xlsx'
    self.progress.emit(f"Загружаем {client_id}")
    try:
        df = pd.read_excel(path, sheet_name='3. Зарплатные данные', usecols="A:H,J:AA",
                           decimal=",")  # опять работа с проводником - считывание файла
    except Exception as e:
        return False, (
            "Ошибка при считывании файла. Возможные причины:\n1.Файл был открыт во время работы функции\n2.Неверное название листа\n3.Нарушена структура файла\n4.Файл повреждён",
            e, file_name)
... и далее...
```

//Что исправлено:

1. Код переписан под MVC схему - интерфейс замкнут сам в себе, только принимает данные для виджетов из модели и отдаёт
   сигналы пользователя в контроллер, который в свою очередь общается с моделью - является промежуточным посредником.
   Модель и Представление взаимодействуют между собой с помощью отдельных структур данных (UserInteractionFeedback и ModelInteractionFeedback).
2. Запросы к БД происходят только через модели виджетов (виджеты не обращаются к БД). Сама точка обращения к БД во всей программе единая (Монолит).
3. Каждое потенциально отделимое логическое действие вынесено в отдельные методы (как методы классов, так и просто
   наборы методов без классов).
4. Все необъявленные переменные вынесены в классы констант для каждой логической сущности в программе.
5. Прописан docstring и аннотации типов в каждом методе.

// Что ещё можно улучшить:

1. После исправления все типы ошибок являются по сути теми же магическими переменными. Было бы хорошо описания ошибок
   вынести в отдельный класс (может даже единый для всей программы), только пока что я ещё не придумал как это сделать

//Далее приведу пример части кода по работе с проводником.

//Константы:

```python
class DataDefinitions:
    class AttributeTableFields:
        TYPE = 'type'
        SYSTEM_NAME = 'sys_name'
        ALLOWED_VALUES = 'fix_values'

    class DataTypeNames:
        INT = 'int'
        FLOAT = 'float'
        STR = 'str'
        COMMENT = 'comment'
        FIX = 'fix'
        DATE = 'date'

    ALLOWED_VALUES_SEPARATOR = ';'


class FileOptionsKeys:
    FILE_NAME = '0'
    FILE_EXTENSION = '1'
    USECOLS = '2'
    SHEET_NAME = '3'
    

class Extensions:
    csv = '.csv'
    xlsx = '.xlsx'
```

//Методы по проверке пути и параметров для считывания файла (электронной таблицы)

```python

def read_file(path: str,
              sheet_name: Optional[str] = None,
              usecols: Optional[str] = None) -> ModelInteractionFeedback:
    """
    Считывает данные из файла на основе заданных параметров.

    Аргументы:
        path (str): Путь к файлу, который необходимо считать.
        sheet_name (Optional[str]): Имя листа для считывания (используется для файлов Excel).
        usecols (Optional[str]): Столбцы, которые необходимо считать.

    Возвращает:
        ModelInteractionFeedback: В случае успеха возвращает value - DataFrame с данными.
                                  В случае ошибки возвращает error - строка с описанием ошибки.
    """

    model_response = _validate_and_prepare_file_reading_options(path, sheet_name, usecols)
    if not model_response.is_successful():
        return model_response

    file_options_params = model_response.get_value()

    model_response = _load_dataframe_from_file(*file_options_params.values())

    return model_response


def _validate_and_prepare_file_reading_options(path: Optional[str],
                                               sheet_name: Optional[str] = None,
                                               usecols: Optional[str] = None) -> ModelInteractionFeedback:
    """
    Валидирует аргументы и подготавливает информацию для считывания файла.

    Принимает на вход:
    - path (str, Optional): Путь к файлу.
    - sheet_name (str, Optional): Имя листа для считывания данных (для Excel файлов).
    - usecols (str, Optional): Строка, определяющая колонки, которые следует считывать.

    Возвращает:
        ModelInteractionFeedback: В случае успеха возвращает словарь с информацией о файле и параметрах считывания.
                                  В случае ошибки возвращает error - строка с описанием ошибки.
    """
    model_response = _validate_file_path(path)
    if not model_response.is_successful():
        return model_response

    file_name, file_extension = model_response.get_value()[0], model_response.get_value()[1]

    model_response = _validate_sheet_name(file_name, file_extension, sheet_name)
    if not model_response.is_successful():
        return model_response

    file_info = {
        FileOptionsKeys.FILE_NAME: file_name,
        FileOptionsKeys.FILE_EXTENSION: file_extension,
        FileOptionsKeys.USECOLS: usecols,
        FileOptionsKeys.SHEET_NAME: sheet_name
    }

    return ModelInteractionFeedback(True, value=file_info)


def _validate_file_path(file_path: str) -> ModelInteractionFeedback:
    """
    Валидирует путь к файлу, проверяя его существование и корректность расширения.

    Метод проверяет:
    - является ли указанная строка путем к файлу,
    - имеет ли файл расширение xlsx или csv,
    - существует ли файл по указанному пути.

    Аргументы:
        file_path (str): Путь к файлу для валидации.

    Возвращает:
        ModelInteractionFeedback: В случае успеха возвращает список с именем файла и его расширением.
                                  В случае ошибки возвращает error - строка с описанием ошибки.
    """
    if not os.path.isfile(file_path):
        return ModelInteractionFeedback(False, error='Путь не указывает на файл.')
    file_name, file_extension = os.path.splitext(file_path)
    if file_extension not in Extensions.get_file_extensions():
        return ModelInteractionFeedback(False,
                                        error=f"Недопустимое расширение файла. Ожидаются: {','.join(Extensions.get_file_extensions())}")
    if not os.path.exists(file_path):
        return ModelInteractionFeedback(False, error='Файл не существует по указанному пути.')

    return ModelInteractionFeedback(True, value=[file_name, file_extension])


def _load_dataframe_from_file(file_path_without_extension: str,
                              file_extension: str,
                              usecols: Optional[list[int]] = None,
                              sheet_name: Optional[str] = None) -> ModelInteractionFeedback:
    """
    Загружает данные из файла в DataFrame.

    Аргументы:
        file_path_without_extension (str): Путь к файлу без расширения.
        file_extension (str): Расширение файла (поддерживаются '.xlsx' и '.csv').
        usecols (Optional[list[int]], optional): Список индексов колонок, которые необходимо считать.
        sheet_name (Optional[str], optional): Имя листа для считывания (для файлов Excel).

    Возвращает:
        ModelInteractionFeedback: В случае успеха возвращает DataFrame с данными.
                                  В случае ошибки возвращает error - строка с описанием ошибки.
    """
    full_path = get_full_path(file_path_without_extension, file_extension)
    try:
        if file_extension == Extensions.csv:
            df = pd.read_csv(full_path, usecols=usecols)
        elif file_extension == Extensions.xlsx:
            df = pd.read_excel(full_path, usecols=usecols, sheet_name=sheet_name)
        else:
            return ModelInteractionFeedback(False, error=f"Неподдерживаемое расширение файла: {file_extension}")
    except Exception as e:
        return ModelInteractionFeedback(False, error=f"Ошибка при считывании файла: {str(e)}")

    return ModelInteractionFeedback(True, value=df)


def _validate_sheet_name(file_path_without_extension: str,
                         file_extension: str,
                         sheet_name: Optional[str]) -> ModelInteractionFeedback:
    """
    Проверяет наличие листа в csv или xlx файле.

    Аргументы:
        file_path_without_extension (str): Путь к файлу без расширения.
        file_extension (str): Расширение файла (поддерживаются '.xlsx' и '.csv').
        sheet_name (Optional[str], optional): Имя листа для считывания (для файлов Excel).

    Возвращает:
        Tuple[bool, Optional[str]]: В случае успеха возвращает кортеж (True, None).
                                    В случае ошибки возвращает кортеж (False, текст ошибки).
    """
    if file_extension != Extensions.xlsx:
        return ModelInteractionFeedback(True)

    full_path = get_full_path(file_path_without_extension, file_extension)

    sheet_exists = _sheet_exists_in_excel(full_path, sheet_name)

    if not sheet_exists:
        return ModelInteractionFeedback(False, error=f'Лист {sheet_name} отсутствует в файле')

    return ModelInteractionFeedback(True)


def _sheet_exists_in_excel(file_path: str, sheet_name: str) -> bool:
    """
    Проверяет наличие листа с заданным именем в файле Excel (формата .xlsx)
    без загрузки всех данных файла, что делает метод быстрым даже для больших файлов.

    Параметры:
    file_path : str
        Путь к файлу Excel, в котором нужно проверить наличие листа.
    sheet_name : str
        Название листа, наличие которого необходимо проверить.

    Возвращает:
    bool
        Возвращает True, если лист с заданным именем существует в файле, иначе False.
    """
    # Открываем книгу Excel в режиме только для чтения
    workbook = openpyxl.load_workbook(file_path, read_only=True)

    # Получаем список названий всех листов
    sheets = workbook.sheetnames

    # Закрываем книгу после получения списка листов
    workbook.close()

    # Проверяем, есть ли лист с заданным именем
    return sheet_name in sheets


def get_full_path(file_path_without_extension: str, file_extension: str) -> str:
    """
    Делает полный путь из двух частей пути

    Аргументы:
        file_path_without_extension (str): Путь к файлу без расширения.
        file_extension (str): Расширение файла .

    Возвращает:
        str - полный путь к файлу.
    """
    return f"{file_path_without_extension}{file_extension}"
```

//Методы для работы с DataFrame. Базовая проверка на валидность

```python
from numpy import nan
import pandas as pd

from App.Widgets.SessionWizard.constructor import ModelInteractionFeedback


class DataDefinitions:
    class AttributeTableFields:
        TYPE = 'type'
        SYSTEM_NAME = 'sys_name'
        ALLOWED_VALUES = 'fix_values'

    class DataTypeNames:
        INT = 'int'
        FLOAT = 'float'
        STR = 'str'
        COMMENT = 'comment'
        FIX = 'fix'
        DATE = 'date'

    ALLOWED_VALUES_SEPARATOR = ';'


def validate_and_transform_dataframe(dataframe: pd.DataFrame,
                                     attributes_info: pd.DataFrame) -> ModelInteractionFeedback:
    """
    Валидирует и трансформирует DataFrame на основе информации об атрибутах.

    Проверяет DataFrame на соответствие определенным критериям (например, количество колонок)
    и преобразует данные в соответствии с информацией об атрибутах.

    Аргументы:
        dataframe (pd.DataFrame): DataFrame для валидации и трансформации.
        attributes_info (pd.DataFrame): DataFrame с информацией об атрибутах, включая типы данных и допустимые значения.

    Возвращает:
        ModelInteractionFeedback: В случае успеха возвращает value - преобразованный DataFrame с данными.
                                  В случае ошибки возвращает error - строка с описанием ошибки.
    """

    model_response = clean_and_validate_dataframe(dataframe)

    if not model_response.is_successful():
        return model_response

    dataframe = model_response.get_value()

    model_response = check_dataframe_columns_number(dataframe, attributes_info)
    if not model_response.is_successful():
        return model_response

    # устанавливаем колонки в df в соответствии с установленным порядком
    dataframe.columns = attributes_info[DataDefinitions.AttributeTableFields.SYSTEM_NAME].tolist()

    validation_result = transform_and_validate_columns(dataframe, attributes_info)

    return validation_result


def transform_and_validate_columns(dataframe: pd.DataFrame,
                                   attributes_info: pd.DataFrame) -> ModelInteractionFeedback:
    """
    Трансформирует и валидирует колонки DataFrame в соответствии с указанными типами данных и ограничениями.

    Аргументы:
        dataframe (pd.DataFrame): DataFrame, в котором производится трансформация и валидация.
        attributes_info (pd.DataFrame): Информация об атрибутах для каждой колонки: типы данных и допустимые значения.

    Возвращает:
        ModelInteractionFeedback: В случае успеха возвращает value - преобразованный DataFrame с данными.
                                  В случае ошибки возвращает error - строка с описанием ошибки.
    """

    # уникальные типы данных колонок для данного типа файла
    unique_data_types = attributes_info[DataDefinitions.AttributeTableFields.TYPE].unique().tolist()

    # проходимся по каждому типу данных
    for data_type in unique_data_types:
        # все колонки для данного типа данных
        columns_of_this_data_type = attributes_info[
            attributes_info[DataDefinitions.AttributeTableFields.TYPE] == data_type][
            DataDefinitions.AttributeTableFields.SYSTEM_NAME].unique().tolist()
        # проходимся по каждой колонке в определённом типе данных
        for column in columns_of_this_data_type:
            # если тип данных нумерик
            if data_type in [DataDefinitions.DataTypeNames.INT, DataDefinitions.DataTypeNames.FLOAT]:
                dataframe = convert_column_to_float(dataframe, column)
            # если тип данных - фиксированное значение
            elif data_type in [DataDefinitions.DataTypeNames.FIX]:
                validation_result = validate_fixed_values(dataframe, attributes_info, column)
                if not validation_result.is_successful():
                    return validation_result

            # TODO: проверка и преобразование для типа данных str
            elif data_type in [DataDefinitions.DataTypeNames.STR]:
                pass
            # TODO: проверка и преобразование для типа данных date
            elif data_type in [DataDefinitions.DataTypeNames.DATE]:
                pass
            # TODO: проверка и преобразование для типа данных comment
            elif data_type in [DataDefinitions.DataTypeNames.COMMENT]:
                pass

    return ModelInteractionFeedback(True, dataframe)


def validate_fixed_values(dataframe: pd.DataFrame,
                          attributes_info: pd.DataFrame,
                          column_name: str) -> ModelInteractionFeedback:
    """
    Проверяет, что значения в указанной колонке соответствуют заранее определенному списку допустимых значений.

    Аргументы:
        dataframe (pd.DataFrame): DataFrame для проверки.
        attributes_info (pd.DataFrame): DataFrame с информацией про колонки.
        column_name (str): Название колонки для проверки на допустимые значения.

    Возвращает:
        ModelInteractionFeedback: В случае успеха возвращает value - преобразованный DataFrame с данными.
                                  В случае ошибки возвращает error - строка с описанием ошибки.
    """
    # получаем эталонные значения для данной колонки
    allowed_values = get_allowed_values_for_column(attributes_info, column_name)

    unwanted_values = dataframe[~dataframe[column_name].isin(allowed_values)]

    if not unwanted_values.empty:
        return ModelInteractionFeedback(False,
                                        error=f"В колонке: {column_name} имеются значения кроме {','.join(allowed_values)}")

    return ModelInteractionFeedback(True, dataframe)


def get_allowed_values_for_column(attributes_info: pd.DataFrame, column_name: str) -> list[str]:
    """
    Извлекает список допустимых значений для указанной колонки из DataFrame с информацией об атрибутах.

    Аргументы:
        attributes_info (pd.DataFrame): DataFrame с информацией об атрибутах.
        column_name (str): Название колонки, для которой требуется получить допустимые значения.

    Возвращает:
        list[str]: Список допустимых значений для колонки.
    """

    allowed_values = []
    allowed_value = attributes_info[attributes_info[DataDefinitions.AttributeTableFields.SYSTEM_NAME] == column_name][
        DataDefinitions.AttributeTableFields.ALLOWED_VALUES].values[0]
    if isinstance(allowed_value, str):
        allowed_values = allowed_value.split(DataDefinitions.ALLOWED_VALUES_SEPARATOR)
    return allowed_values


def check_dataframe_columns_number(dataframe: pd.DataFrame,
                                   attributes_info: pd.DataFrame) -> ModelInteractionFeedback:
    """
    Проверяет, соответствует ли количество колонок в DataFrame ожидаемому количеству на основе информации об атрибутах.

    Аргументы:
        dataframe (pd.DataFrame): DataFrame для проверки.
        attributes_info (pd.DataFrame): DataFrame с информацией об атрибутах, определяющий ожидаемое количество колонок.

    Возвращает:
        ModelInteractionFeedback: В случае успеха возвращает пустой value - просто логическая проверка.
                                    (количество колонок соответствует ожидаемому)
                                  В случае ошибки возвращает error - строка с описанием ошибки.
    """

    target_dataframe_columns_number = attributes_info.shape[0]
    if target_dataframe_columns_number != len(dataframe.columns):
        return ModelInteractionFeedback(False, error='Неверное число колонок')
    return ModelInteractionFeedback(True)


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


def convert_column_to_float(data_frame: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Преобразует указанную колонку DataFrame в числа с плавающей точкой.

    Шаги преобразования:
    1. Преобразование всех значений колонки в строки.
    2. Замена запятых на точки для корректного преобразования в числа с плавающей точкой.
    3. Замена пустых строк на '0' и преобразование в float64, округление значений.
    4. Замена округленных нулей на NaN, чтобы различать отсутствующие данные и нулевые значения.

    Параметры:
    - data_frame (pd.DataFrame): DataFrame, в котором будет преобразована колонка.
    - column_name (str): Название колонки для преобразования.

    Возвращает:
    - pd.DataFrame: DataFrame с преобразованной колонкой.
    """
    # Преобразование значений колонки в строки
    data_frame[column_name] = data_frame[column_name].astype(str)

    # Замена запятых на точки для корректного преобразования в числа с плавающей точкой
    data_frame[column_name] = data_frame[column_name].str.replace(',', '.')

    # Замена пустых строк на '0' и преобразование в float64
    data_frame[column_name] = data_frame[column_name].replace('', '0').fillna(0).astype('float64')

    # Округление значений до ближайшего целого числа
    data_frame[column_name] = data_frame[column_name].round()

    # Замена округленных нулей на NaN
    data_frame[column_name] = data_frame[column_name].replace(0, nan)

    return data_frame

```