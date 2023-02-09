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
5. Запустити проект
   ```sh
   python manage.py runserver
   ```
