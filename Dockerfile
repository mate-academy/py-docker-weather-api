# 1. Базовий імідж
FROM python:3.11-slim

# 2. Робоча директорія всередині контейнера
WORKDIR /app

# 3. Скопіювати лише необхідне
COPY ./app ./app

# 4. Встановити requests
RUN pip install --no-cache-dir requests

# 5. Команда запуску
CMD ["python", "app/main.py"]
