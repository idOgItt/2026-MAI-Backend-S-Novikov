# Домашнее задание №4

Модели и миграции — в приложении **`project/movies/`**.

## 1. PostgreSQL: пользователь и база

На сервере Postgres (пример команд; имена/пароли замени на свои):

```sql
CREATE USER mai_app WITH PASSWORD 'your_secret';
CREATE DATABASE mai_db OWNER mai_app;
GRANT ALL PRIVILEGES ON DATABASE mai_db TO mai_app;
```

В `project/project/settings.py` в `DATABASES['default']` должны совпадать `NAME`, `USER`, `PASSWORD`, `HOST`, `PORT` с созданными сущностями.

## 2. Схема данных (связи)

В `project/movies/models.py`:

| Связь        | Где |
|-------------|-----|
| **OneToOne** | `Profile.user` → `User` (расширение профиля) |
| **ForeignKey** | `Movie.genre` → `Genre` (уже было) |
| **ManyToMany** | `Movie.tags` ↔ `Tag` |

Миграция: `project/movies/migrations/0008_profile_and_tags.py`.

## 3. Применить миграции

```bash
cd project
source ../.venv/bin/activate
python manage.py migrate
```

Если Postgres ещё не поднят или креды другие — сначала поправь `DATABASES` или подними контейнер/сервис.
