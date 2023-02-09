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
6. Запустити міграцію
   ```sh
   python manage.py migrate
   ```
7. Запустити проект
   ```sh
   python manage.py runserver
   ```
8. Тестинг усіх модулів
```sh
python manage.py test
```
