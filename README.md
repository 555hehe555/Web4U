# Web4U

**Web4U** — це проста соціальна мережа, створена на Django як pet-проєкт. Користувачі можуть створювати акаунти, додавати пости, залишати коментарі, ставити лайки. Проєкт містить REST API з автоматичною документацією через Swagger, базу даних PostgreSQL, контейнеризацію через Docker, а також підтримку статичних і медійних файлів.

## Основні можливості

- Реєстрація та аутентифікація користувачів
- CRUD для постів
- Коментарі до постів
- Система лайків
- REST API
- Swagger-документація
- Docker + Docker Compose
- база даний PostgreSQL (у Docker) або SQLite (локально)
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
DEBUG=True
SECRET_KEY='your_secret_key'

# Database
POSTGRES_DB=mydb
POSTGRES_USER=root
POSTGRES_PASSWORD=root
POSTGRES_HOST=db
POSTGRES_PORT=5432

# Admin user
ADMIN_NAME=admin
ADMIN_EMAIL=admin@example.com
ADMIN_PASSWORD=admin

DJANGO_SETTINGS_MODULE='myblog.settings'
NGINX_PORT='80'
```

Або можете вести команду:

```bash
# Windows
copy .env.example .env
```

```bash
# Linux / macOS
cp .env.example .env
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

**Swagger** — інтерактивна документація до API, яка дозволяє переглядати та тестувати запити безпосередньо з браузера.

Після запуску перейдіть за адресою:

```
http://localhost:8000/api/v1/docs/
```

або

```
http://127.0.0.1:8000/api/v1/docs/
```

---

## Примітки

* Якщо порт 8000 уже зайнятий, змініть його в `docker-compose.yml` у секції `ports`
* За замовчуванням всі дані зберігаються в тому `./postgres_data` на вашій машині
* Усі сервіси запускаються разом (Postgres, Django app, yt-django). Якщо не потрібен `yt-django`, можна закоментувати його у `docker-compose.yml`
* Ви можете швидко перемикатися між Docker та локальним режимом, змінюючи лише змінну USE_DOCKER у .env
