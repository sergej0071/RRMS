## Для запуску проекту у контексті другої лабороторної роботи необхідно:

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
5. Встановити MongoDBCompass
Після втановлення клієнту bd треба створити на базу даних 'TestDB' для подільшої роботи з нею.

6. Закоментити залежності бібліотек та сервісу 'django_apscheduler' та 'rrms_scheduler_app' у rrms_project/settings.py для корректної першої міграції
   ```sh
   #'django_apscheduler',
   #'rrms_scheduler_app',
   ```
7. Запустити міграцію
   ```sh
   python manage.py migrate
   ```
8. Відкоментувати сервіси 'django_apscheduler' та 'rrms_scheduler_app' у rrms_project/settings.py
   ```sh
   'django_apscheduler',
   'rrms_scheduler_app',
   ```
9. Запустити міграцію повторно
   python manage.py migrate
10. Запустити проект
   ```sh
   python manage.py runserver
   ```
11. Тестинг усіх модулів
```sh
python manage.py test
```
