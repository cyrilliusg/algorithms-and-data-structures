import os
from zipfile import ZipFile
from random import randint


class DirectoryProcessor:
    def generate_files_by_extension(self, extension):
        """
        создаёт файлы с указанным расширением
        :param extension: расширение файла
        """
        for i in range(randint(3, 10)):
            with open(f'{i}{self._add_dot_to_extension(extension)}', 'w') as file:
                file.close()

    def del_files_by_extension(self, extension):
        """
        удаляет файлы с указанным расширением
        :param extension: расширение файла
        """
        for file_name in os.listdir():
            if file_name.endswith(extension) and os.path.isfile(file_name):
                os.remove(file_name)

    def _add_dot_to_extension(self, value):
        """
        Добавляет точку к расширению файла, если она отсутствует.
        :param value (str): Расширение файла.
        :return: Расширение файла с точкой в начале.
        """
        return '.' + value if not value.startswith('.') else value

    def _find_files_in_directory(self, path, extension):
        """
        Ищет файлы по расширению в пути
        :param path: путь директории
        :param extension: расширение
        :return: список файлов
        """
        if not os.path.isdir(path):
            return False

        files = []
        for file_name in os.listdir(path):
            if file_name.endswith(extension) and os.path.isfile(file_name):
                files.append(file_name)
        return files

    def archive_files_by_extension(self, name, extension):
        """
        создаёт архив и наполняет его файлами по расширению
        :param name: имя создаваемого архива
        :param extension: расширение файла для поиска
        :return: путь к файлу
        """
        extension = self._add_dot_to_extension(extension)
        files = self._find_files_in_directory(os.getcwd(), extension)

        if not files:
            return False
        zip_name = f'{name}.zip'
        with ZipFile(zip_name, 'w') as item:
            for file in files:
                item.write(file)

        return os.path.join(os.getcwd(), zip_name)


if __name__ == '__main__':
    directory_processor = DirectoryProcessor()
    extension = 'cpp'

    try:
        # опционально. генерируем файлы с желаемым расширением для теста
        directory_processor.generate_files_by_extension(extension)
        archive_path = directory_processor.archive_files_by_extension('test_archive', extension)
    except Exception as e:
        print(f'Произошла непредвиденная ошибка\n{e}')
    else:
        print(f' путь к файлу: {archive_path}')
    finally:
        # опционально. в конце удаляем ранее созданные файлы
        directory_processor.del_files_by_extension(extension)
