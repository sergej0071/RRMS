# RRMS - Research Results Monitoring System

## Відстежування змін по лабораторним. 

Кожна лаборатона робота представляє собою закінчену роботу та є повністью робочою. Кожній з них відповідає гілка релізу `release` та відповідний майлстоун по яким можна відстежувати зміни, які робилися командою. Нумерація релізів так і майлстоунів починається з одиниці, перший реліз відповідає другій лабораторній роботі. Майлстоуни можна знайти у вкладці Pull requests, гілки у вкладці code.

## Робота з arduino

Для завантаження скетчу потібно мати плату arduino Mega 2560 та 2 датчики: BMP280, DTH11.
Далі потрібно завантажити середовище [Arduino IDE](https://www.arduino.cc/en/software).

Після завантаження потрібно у Tools відповідну платформу та порт для подальшої роботи.
Для завантаження скетчу, який наявний у репозиторії під папкою arduino/ReadHumidityTemperaturePressure, потрібно встановити наступні бібліотеки використовуючи менеджер бібліотеками у Arduino ide. (Sketch-> Include Library -> Manage Library).
Бібліотеки (встановлювати із залежностями):

* [DHT-sensor-library](https://github.com/adafruit/DHT-sensor-library)
* [Adafruit_Sensor](https://github.com/adafruit/Adafruit_Sensor)
* [Adafruit_BMP280_Library](https://github.com/adafruit/Adafruit_BMP280_Library)

Схема підключення датчиків до arduino:

![Arduino](https://user-images.githubusercontent.com/82032813/216855248-030cdc00-8991-4075-9de9-72ca0d6c0788.png)

## Робота із бекедом

Для запуску проекту у контексті третьої лабороторної роботи необхідно:

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
4. Встановити необхідні бібліотеки
   ```sh
   pip install -r requirements.txt
   ```
5. Запустити міграцію
   ```sh
   python manage.py migrate
   ```
6. Запустити проект
   ```sh
   python manage.py runserver
   ```

## Робота з БД

У кожному релізі вже наявна необхідна міграція, яка була створена за допомогою команди 

py manage.py makemigrations. Для виконнання самого коду виконайте команду py manage.py migrate. Потрібно зауважити, щоб міграція успішно встановилася потрібно закоментувати у `\rrms_project\settings` в `INSTALLED_APPS` `rrms_scheduler_app` та `django_apscheduler`, після чого відкоментувати їх. Для запуску серверу виконайте команду `python manage.py runserver`.

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

АЛЕ, взаємодія між backend і frontend не відбувається до 5-6 лабораторних. У зв'язку з тим, що не збігаються endpoints/interfaces. Тому за замовчуванням константа `IS_MOCK` має значення `true`.