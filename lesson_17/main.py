import os
from PIL import Image, ImageDraw, ImageFont


class DirectoryProcessor:
    # Основная функция для обработки директории
    def main_func(self, actual_extension, target_extension):
        actual_extension = self._add_dot_to_extension(actual_extension)
        target_extension = self._add_dot_to_extension(target_extension)
        path = os.getcwd()  # Получаем текущую рабочую директорию
        files = self._find_files_in_directory(path, actual_extension)  # Находим файлы с нужным расширением
        files = self._convert_files([os.path.join(path, file) for file in files],
                                    target_extension)  # Конвертируем файлы
        for file in files:  # Обрабатываем каждый файл
            self._process_image(file)

    # Конвертирует файлы в новый формат
    def _convert_files(self, files, extension):
        return [os.path.splitext(file)[0] + extension for file in files]

    # Обрабатывает изображение, добавляя прямоугольник и текст
    def _process_image(self, file_path):
        print(file_path)
        im = Image.open(file_path)  # Открываем изображение
        draw = ImageDraw.Draw(im)  # Инициализируем инструмент для рисования
        draw.fill = False
        sz = im.size
        mid_width, mid_length = int(sz[0] / 2), int(sz[1] / 2)  # Находим центр изображения
        rectangle_side = 100  # Размер стороны прямоугольника

        # Координаты прямоугольника
        rectangle_coordinates = [mid_width - rectangle_side, mid_length - rectangle_side,
                                 mid_width + rectangle_side, mid_length + rectangle_side]

        draw.rectangle(rectangle_coordinates)  # Рисуем прямоугольник
        font = ImageFont.truetype("arial.ttf", 15)  # Устанавливаем шрифт

        # Добавляем текст
        draw.multiline_text((mid_width, mid_length), 'Hello,\nWorld!', font=font)

        im.save(file_path)  # Сохраняем изменения
        del draw  # Удаляем инструмент для рисования

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


if __name__ == '__main__':
    directory_processor = DirectoryProcessor()
    directory_processor.main_func('jpg', 'png')  # Конвертируем jpg в png и обрабатываем изображения
