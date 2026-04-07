# Домашнее задание №3

Реализация лежит в Django-проекте **`project/`** (корень репозитория).

## Что сделано

1. **Тематика** — каталог фильмов: главная, личный кабинет, лента, карточка фильма, страница «категории» (жанр) — задел под авторизацию и избранное (см. шаблоны в `project/movies/templates/movies/web/`).

2. **Маршруты**
   - **`/api/...`** — заглушки API на `JsonResponse` в `project/movies/api_views.py`, URL — `project/movies/api_urls.py`.
   - **`/web/...`** — простые HTML-страницы в `project/movies/web_views.py`, URL — `project/movies/web_urls.py`.

3. **Ограничение методов** — `@require_http_methods(["GET"])` или `["POST"]` на соответствующих view (как в задании).

4. **Nginx** — пример конфига с `location /web/` и `location /api/`: файл `lesson-03/nginx/nginx.conf.example` (подставь `<PROJECT_ROOT>` и при необходимости пользователя `user`).

## Как запустить Django локально

```bash
cd project
source ../.venv/bin/activate   # или своё venv
pip install -r ../requirements.txt
python manage.py runserver
```

Проверка:

- http://127.0.0.1:8000/web/
- http://127.0.0.1:8000/api/profile/

## Как повесить nginx

1. Подними gunicorn с `project.wsgi:application` (например порт 8000).
2. Скопируй `nginx.conf.example`, подставь пути, запусти:

```bash
sudo nginx -c <путь>/lesson-03/nginx/nginx.conf
```
