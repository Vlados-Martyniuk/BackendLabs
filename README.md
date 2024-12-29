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


### 3. **/healthcheck (GET)**
   Перевірка стану сервісу.
   - **Відповідь**: JSON з поточною датою та статусом сервісу.
   - **Приклад відповіді**:
     ```json
     {
       "status": "OK",
       "date": "2024-11-06 14:30:00"
     }
     ```

### 4. **/user (POST)**
   Створити нового користувача.
   - **Тіло запиту**: JSON з полем `name`.
   - **Приклад запиту**:
     ```json
     {
       "name": "John Doe"
     }
     ```
   - **Відповідь**: JSON з даними створеного користувача, включаючи унікальний `id`.

### 5. **/user/<user_id> (GET)**
   Отримати дані користувача за ID.
   - **Відповідь**: JSON з даними користувача або 404, якщо користувач не знайдений.

### 6. **/user/<user_id> (DELETE)**
   Видалити користувача за ID.
   - **Відповідь**: 204 (No Content), якщо користувача успішно видалено або 404, якщо користувача не знайдено.

### 7. **/users (GET)**
   Отримати список усіх користувачів.
   - **Відповідь**: JSON з масивом усіх користувачів.

### 8. **/category (POST)**
   Створити нову категорію.
   - **Тіло запиту**: JSON з полем `name`.
   - **Приклад запиту**:
     ```json
     {
       "name": "Food"
     }
     ```
   - **Відповідь**: JSON з даними створеної категорії, включаючи унікальний `id`.

### 9. **/category (GET)**
   Отримати список усіх категорій.
   - **Відповідь**: JSON з масивом усіх категорій.

### 10. **/category/<category_id> (DELETE)**
   Видалити категорію за ID.
   - **Відповідь**: 204 (No Content), якщо категорію успішно видалено або 404, якщо категорію не знайдено.

### 11. **/record (POST)**
   Створити новий запис (зв'язок користувача з категорією).
   - **Тіло запиту**: JSON з полями `user_id`, `category_id` та `amount`.
   - **Приклад запиту**:
     ```json
     {
       "user_id": 1,
       "category_id": 2,
       "amount": 100
     }
     ```
   - **Відповідь**: JSON з даними створеного запису, включаючи унікальний `id` та часову мітку.

### 12. **/record/<record_id> (GET)**
   Отримати дані запису за ID.
   - **Відповідь**: JSON з даними запису або 404, якщо запис не знайдений.

### 13. **/record/<record_id> (DELETE)**
   Видалити запис за ID.
   - **Відповідь**: 204 (No Content), якщо запис успішно видалено або 404, якщо запис не знайдено.

### 14. **/record (GET)**
   Отримати список записів за фільтрами.
   - **Параметри запиту**: `user_id` (опціонально), `category_id` (опціонально).
   - **Відповідь**: JSON з масивом фільтрованих записів, або помилка 400, якщо жоден параметр не вказано.

Опис: Повертає статус сервісу і поточну дату у форматі JSON.

## Зупинка контейнера
Щоб зупинити контейнер, натисніть CTRL + C у терміналі, де запущено docker-compose up.    