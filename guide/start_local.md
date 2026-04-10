# запуск проєкта локально

### якщо ви виконали минулі кроки то вам ще зробити пару наступних:

---

- В .env міняємо відповідне значення на 
```USE_DOCKER=0```

- Встановити venv
```bash
python -m venv venv
```
- Активувати його 
```bash
source venv/bin/activate
```
або
```CMD
venv\Scripts\activate
```

- длі треба встановити бібліотеки з requirements.txt
```bash
pip install -r requirements.txt
```

- Далі залишається створити міграції (базу даних)
```bash
python manage.py makemigrations
python manage.py migrate
```

- І запустити сервер
```bash
python manage.py runserver
```

---

## Тепер вітаю, ви запустили сервер