# Web4U

**Web4U** — це невелика соціальна мережа, створена на Django, як pet-проєкт. Користувачі можуть створювати акаунти, додавати пости, залишати коментарі, ставити лайки. У проєкті реалізовано REST API з автоматичною документацією через Swagger, є база даних PostgreSQL, система контейнеризації Docker та підтримка статичних/медійних файлів.

## Основні можливості

- Реєстрація та аутентифікація користувачів
- CRUD для постів
- Коментарі до постів
- Система лайків
- REST API
- Swagger-документація
- Docker + Docker Compose
- Postgres база даних
- Автоматичне застосування міграцій
- Підтримка media/static файлів через volume

---

## Швидкий запуск проєкту

### 1. Клонувати репозиторій

```bash
git clone https://github.com/555hehe555/Web4U.git
cd web4u
````

### 2. Створити `.env` файл у корені проєкту

Використай шаблон нижче або створюй власний:

```
POSTGRES_DB=web4u
POSTGRES_USER=web4u_user
POSTGRES_PASSWORD=your_secure_password
POSTGRES_PORT=5432

DB_HOST=db
DB_NAME=web4u
DB_USER=web4u_user
DB_PASSWORD=your_secure_password
```

Або межете вести команду:

```bash
copy .env.example .env
```

> **Примітка:** `DB_*` змінні потрібні для зв’язку Django з базою, `POSTGRES_*` — для ініціалізації самої бази.

---

### 3. Запустити проєкт через Docker Compose

```bash
docker-compose up --build
```

> Після цього автоматично:
>
> * створиться база даних PostgreSQL
> * застосуються всі міграції
> * створиться суперкористувач (якщо реалізовано в `create_superuser.py`)
> * сервер Django буде доступний на `http://localhost:8000/`

---

## Swagger / API документація

Після запуску перейдіть за адресою:

```
http://localhost:8000/api/swagger/schema/
```

або

```
http://127.0.0.1:8000/api/swagger/schema/
```

---

## Примітки

* Якщо порт 8000 уже зайнятий, змініть його в `docker-compose.yml` у секції `ports`.
* За замовчуванням всі дані зберігаються в тому `./postgres_data` на вашій машині.
* Усі сервіси запускаються разом (Postgres, Django app, yt-django). Якщо не потрібен `yt-django`, можна закоментувати його у `docker-compose.yml`.
