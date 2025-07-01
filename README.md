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
```

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

DJANGO_SETTINGS_MODULE='config.settings'
NGINX_PORT='80'

WEBSITE_DOMAIN=localhost:8000
DJANGO_SECRET_KEY='your-secret-key'
DJANGO_DEBUG='True'
DJANGO_ALLOWED_HOSTS='localhost 127.0.0.1 [::1]'
POSTGRES_DB='your-db-name'
POSTGRES_USER='your-db-user'
POSTGRES_PASSWORD='your-db-password'
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

> **Примітка:** `DB_*` змінні потрібні для зв'язку Django з базою, `POSTGRES_*`