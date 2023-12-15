## Отчёт по запуску скриптов из midnight commander на WSL


#### После установки MC перешёл в репозиторий с проектами


![Первый запуск](https://github.com/cyrilliusg/High-School-of-Programming/blob/main/images/screenshots/lesson_8.1.PNG)

 Открыл главный файл с 8 урока с пакетами в режиме редактирования MC, и добавил новую строку:
```python
print("Запускаем скрипт из WSL")
```
![Режим редактирования](https://github.com/cyrilliusg/High-School-of-Programming/blob/main/images/screenshots/lesson_8.2.PNG)


По умолчанию, так же, как и в Far, необходимо установить ассоциации на python файлы, чтобы запускать по Enter.
Просто через консоль можно запускать как 
``` bash
python3 filename.py
```

#### Установка ассоциации
``` bash
regex/\.(py)$
    Open=python3 %f
```

#### Запуск файла
![Запуск файла](https://github.com/cyrilliusg/High-School-of-Programming/blob/main/images/screenshots/lesson_8.3.png)
