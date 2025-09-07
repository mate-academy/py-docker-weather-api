# Вимога чекліста: slim-образ
FROM python:3.10.8-slim

# Оновлення сертифікатів/базових пакунків мінімально та чисто
RUN apt-get update \
 && apt-get install -y --no-install-recommends ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# Лише потрібна залежність для HTTPS-запитів
RUN pip install --no-cache-dir requests

# Кладемо код прямо в /app (щоб був /app/main.py, без /app/app)
WORKDIR /app
COPY app/ .

# Запуск (без вимоги до __init__.py)
CMD ["python", "-m", "main"]
