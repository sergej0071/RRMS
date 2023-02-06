# RRMS - Research Results Monitoring System

## Робота із бекедом

Кожна лаборатона робота представляє собою закінчену роботу та є повністью робочою. Кожній з них відповідає гілка релізу `release` та відповідний майлстоун по яким можна відстежувати зміни, які робилися командою. Нумерація релізів так і майлстоунів починається з одиниці, перший реліз відповідає другій лабораторній роботі. Майлстоуни можна знайти у вкладці Pull requests, гілки у вкладці code.

Для запуску проекту у контексті другої лабороторної роботи необхідно:

1. Клонувати проект на локальний комп'ютер.
   ```sh
   git clone https://github.com/sergej0071/RRMS.git
   ```
2. Створити віртуальну середу для роботи з проектом
   ```sh
   python -m venv env
   ```
3. Активувати віртуальну середу
   ```sh
   source env/activate
   ```
4. Встангвити необхідні бібліотеки
   ```sh
   pip install -r requirements.txt
   ```
5. Закоментити залежності бібліотек та сервісу 'django_apscheduler' та 'rrms_scheduler_app' у rrms_project/settings.py для корректної першої міграції
   ```sh
   #'django_apscheduler',
   #'rrms_scheduler_app',
   ```
6. Запустити міграцію
   ```sh
   python manage.py migrate
   ```
7. Відкоментувати сервіси 'django_apscheduler' та 'rrms_scheduler_app' у rrms_project/settings.py
   ```sh
   'django_apscheduler',
   'rrms_scheduler_app',
   ```
8. Запустити міграцію повторно
   python manage.py migrate
9. Запустити проект
   ```sh
   python manage.py runserver
   ```
10. Тестинг усіх модулів
```sh
python manage.py test
```


## Робота з frontend

Для запуску проекту Angular необхідно щоб на комп'ютер було встановлено:
* [node.js](https://nodejs.org/en/)
* [Angular CLI](https://angular.io/cli)

Для встановлення node.js її треба завантажити з офіційного сайту та встановити.
Для встановлення Angular CLI необхідно виконати наступну команду: `npm install -g @angular/cli`.

Для запуску програми необхідно:

* клонувати репозиторій;
* відкрити консоль у папці frontend;
* ввести `npm update`;
* ввести `ng serve`;
* відкрити в браузері `http://localhost:4200`.

Параметри роботи з API знаходяться в цьому файлі:
`frontend\src\app\shared\services\parse-api.service.ts`

Константа `IS_MOCK` відповідає за виведення мокових даних. Дня отримання даних з API вона має бути у стані `false`.
Константа `API_PATH` відповідає за шлях до використовуваного API.

Для запуску юніт тестів необхідно ввести команду `ng test`, проте якщо не перевести контстанту `IS_MOCK` у значення `false`, то 2 тести будуть валитися.
