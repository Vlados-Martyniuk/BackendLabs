# BackendLabs

## Вимоги

- Python 3.11 або вище
- Docker
- Docker Compose

## Встановлення

1. Клонуйте репозиторій:
   git clone <(https://github.com/Vlados-Martyniuk/BackendLabs.git)>


2. Встановіть залежності:
    pip install -r requirements.txt

## Використання з Docker

1. Збірка Docker образу:
    docker-compose build

2. Запуск контейнера:
    docker-compose up

3. Доступ до додатку: 
    Відкрийте браузер і перейдіть за адресою http://localhost:5000 для доступу до вашого Flask-додатку.

## Ендпоінти

1. hello_world
    Опис: Повертає простий текст "Hello, World!".

2. GET /healthcheck

Опис: Повертає статус сервісу і поточну дату у форматі JSON.

## Зупинка контейнера
Щоб зупинити контейнер, натисніть CTRL + C у терміналі, де запущено docker-compose up.    