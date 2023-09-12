# Yatube для блогеров на Django

Веб приложение, которое позволяет блогерам создавать посты, комментировать
записи и подписываться на других пользователей. Основной функционал приложения
покрыт полностью unit-тестами.

## Технологии

- Python 3.9.10
- Django 4.2.5
- SQLite
- Bootstrap
- Unittest

## Используемые стандарты

- pep8
- flake8
- black
- djlint
- pymarkdown
- mypy

## Как развернуть

1. Склонируйте проект в рабочую директорию.
2. Создайте виртуальное окружение.
3. Установите зависимости из файла `requirements.txt`.
4. Выполните миграции и запустите сервер в режиме разработчика
   (находясь в директории `yatube`):

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```
## Демо

![Иллюстрация к проекту](https://github.com/xanhex/yatube-django/blob/master/demo.jpg)