# Отчёт по домашнему заданию №2

## 1. Установка и запуск nginx и gunicorn

- Виртуальное окружение создано в корне репозитория:

  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

- Все зависимости проекта, включая `gunicorn`, устанавливаются из корневого `requirements.txt`:

  ```bash
  pip install -r requirements.txt
  ```

- WSGI‑приложение размещено в `lesson-02/myapp.py`, точка входа для gunicorn — `myapp:app`.

- Запуск gunicorn:

  ```bash
  cd lesson-02
  ./run_app.sh
  # или
  # gunicorn --workers 4 myapp:app
  ```

## 2. Статика из public/ через nginx

- В каталоге `lesson-02` создана директория для статики и тестовый файл:

  ```bash
  cd lesson-02
  mkdir -p public
  echo "hello from nginx static" > public/test.txt
  ```

- В конфиге `lesson-02/nginx/nginx.conf` настроен `location /public/` (путь до проекта обозначен как `<PROJECT_ROOT>` и подставляется локально):

  ```nginx
  http {
      access_log <PROJECT_ROOT>/lesson-02/logs/access.log;
      log_format simple '$remote_addr $request $status';

      upstream gunicorn_backend {
          server 127.0.0.1:8000;
      }

      server {
          listen 80;
          server_name localhost;

          # Отдача статических файлов из public/
          location /public/ {
              alias <PROJECT_ROOT>/lesson-02/public/;
              autoindex on;
          }

          ...
      }
  }
  ```

- Запуск nginx с этим конфигом:

  ```bash
  sudo nginx -c /home/lerner/Cursor/Prog_Eng/MAI-Backend/lesson-02/nginx/nginx.conf
  ```

- Проверка:

  ```bash
  curl http://localhost/public/test.txt
  # hello from nginx static
  ```

## 3. WSGI‑приложение для генерации паролей (gunicorn)

- Реализация WSGI‑приложения — файл `lesson-02/myapp.py`.

- Приложение использует модули `random` и `string` и генерирует пароли согласно требованиям:

  - длина от 8 до 16 символов;
  - как минимум 1 цифра;
  - как минимум 1 строчная буква;
  - как минимум 1 заглавная буква;
  - как минимум 1 символ из `#[]().,!@&^%*`.

- Длина задаётся через переменную окружения `PASSWORD_LENGTH` (по умолчанию 12) и жёстко ограничивается диапазоном `[8, 16]`.

- Проверка локального ответа gunicorn (мимо nginx):

  ```bash
  curl http://127.0.0.1:8000
  # на каждый запрос возвращается новый пароль
  ```

## 4. Проксирование запросов через nginx (upstream gunicorn)

- В `nginx.conf` объявлен upstream и `location /gunicorn/`:

  ```nginx
  upstream gunicorn_backend {
      server 127.0.0.1:8000;
  }

  server {
      listen 80;
      server_name localhost;

      location /gunicorn/ {
          proxy_pass http://gunicorn_backend;
          proxy_set_header Host $host;
          proxy_set_header X-Real-IP $remote_addr;
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
          proxy_set_header X-Forwarded-Proto $scheme;
      }
  }
  ```

- При запущенных gunicorn и nginx:

  ```bash
  curl http://localhost/gunicorn/
  # пароль, сгенерированный WSGI-приложением, но уже через nginx
  ```

## 5. Измерение производительности (ab)

- Для измерений использовался `ab` (apachebench), нагружался именно nginx‑endpoint `/gunicorn/`, который проксирует в gunicorn.

- Команда с конкуренцией 41:

  ```bash
  ab -n 1000 -c 41 http://localhost/gunicorn/
  ```

  Ключевые результаты:

  - `Complete requests: 1000`
  - `Failed requests: 0`
  - `Requests per second: ~5783 [#/sec]`

  При таком уровне нагрузки сервер обрабатывает ~5800 запросов в секунду без ошибок.

- При увеличении конкуренции:

  - `-c 42` и выше:

    ```bash
    ab -n 1000 -c 42 http://localhost/gunicorn/
    ```

    появляются ошибки вида:

    - `apr_socket_recv: Connection reset by peer (104)`
    - число завершённых запросов < 1000

  - при `-c 48`, `-c 47`, `-c 45`, `-c 44`, `-c 43` также наблюдаются сбросы соединений и недобор по количеству успешных запросов.

- Таким образом:

  - стабильный уровень нагрузки без ошибок — около **5800 RPS** (`ab -n 1000 -c 41`);
  - увеличение нагрузки более чем на ~10% (конкуренция 42 и выше) приводит к появлению таймаутов/ошибок (`Connection reset by peer`), что удовлетворяет последнему пункту задания.\n
