import logging
import os
import shutil


class DirectoryProcessor:
    def __init__(self):
        pass

    def _check_directory_exists(self, value):
        """
        Проверяет, является ли заданный путь папкой.

        Args:
            value (str): Путь к папке.

        Raises:
            ValueError: Если путь не является папкой.
        """
        if not os.path.isdir(value):
            raise ValueError("Необходимо передать путь к папке")

    def _add_dot_to_extension(self, value):
        """
        Добавляет точку к расширению файла, если она отсутствует.

        Args:
            value (str): Расширение файла.

        Returns:
            str: Расширение файла с точкой в начале.
        """
        return '.' + value if not value.startswith('.') else value

    def get_result(self, dir_path: str, end_file: str, flag: bool) -> list:
        """
        Ищет каталоги и файлы по указанному пути и расширению. Опционально: анализирует вложенные каталоги

        Args:
            dir_path (str): Путь к каталогу.
            end_file (str): Расширение файла.
            flag (bool): Булев флажок.

        Returns:
            list: Список из двух списков имён файлов и подкаталогов.
        """
        self._check_directory_exists(dir_path)

        # если окончание файла передано пустой строкой, то поиск любых файлов
        if end_file != '':
            end_file = self._add_dot_to_extension(end_file)

        result_files = []
        result_dirs = []
        target_dirs = [dir_path]

        if flag:
            for obj in os.listdir(dir_path):
                if os.path.isdir(obj):
                    target_dirs.append(os.path.abspath(obj))

        for dir_path in target_dirs:
            for obj in os.listdir(dir_path):
                obj_path = os.path.join(dir_path, obj)
                if os.path.isdir(obj_path):
                    result_dirs.append(obj)
                    continue  # вместо else проставил continue для читаемости
                if end_file == '':  # если окончание файла - пустая строка, то все файлы добавить
                    result_files.append(obj)
                    continue  # вместо else проставил continue для читаемости
                if obj_path.endswith(end_file):
                    result_files.append(obj)

        return [result_files, result_dirs]

    def delete_directory(self, directory_path: str) -> bool:
        """
        Удаляет заданный каталог и все файлы внутри него, оставляя подкаталоги нетронутыми.

        Args:
            directory_path (str): Путь к удаляемому каталогу.

        Returns:
            bool: True, если удаление прошло успешно, False в противном случае.
        """
        self._check_directory_exists(directory_path)

        directory_info = self.get_result(directory_path, '', False)
        if directory_info[1]:  # если список с подкаталогами не пустой
            return False

        for file_name in directory_info[0]:
            try:
                file_path = os.path.join(directory_path, file_name)
                os.unlink(file_path)
            except Exception as e:
                print(f"Ошибка при удалении файла: {e}")
                return False
        os.rmdir(directory_path)
        return True

    def create_temp_dir(self, folder_name, flag=True):
        """
        Создает временный каталог с указанным именем.

        Args:
            folder_name (str): Имя создаваемого каталога.
            flag (bool): Булев флажок для создания вложенного подкаталога.

        Returns:
            str: Путь к созданному каталогу.
        """
        if os.path.isdir(folder_name):
            shutil.rmtree(folder_name, ignore_errors=True)
        os.mkdir(folder_name)
        open(os.path.join(os.getcwd(), folder_name, 'temp_file.txt'), 'w')
        if flag:
            os.mkdir(os.path.join(folder_name, 'another_folder'))

        return os.path.join(os.getcwd(), folder_name)


if __name__ == '__main__':
    explorer = DirectoryProcessor()

    # Функция 4.1: печать файлов и каталогов по передаваемому пути
    print(explorer.get_result(os.getcwd(), 'txt', False))

    # Функция 4.2: удаление каталога с файлами по передаваемому пути (при отсутствии поткаталогов, иначе ничего).
    # дополнительно метод create_temp_dir создаёт временный каталог для демонстрации работы метода удаления,
    # с флагом: True- с подкаталогом, False - без каталога.
    success = explorer.delete_directory(os.path.join(os.getcwd(), explorer.create_temp_dir('temp_folder', False)))
    if success:
        print(f"Каталог успешно удален.")
    else:
        print(f"Ошибка при удалении каталога")
