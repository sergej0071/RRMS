## Для запуску проекту у контексті другої лабороторної роботи необхідно:

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
7. Тестинг усіх модулів
   ```sh
   python manage.py test
   ```