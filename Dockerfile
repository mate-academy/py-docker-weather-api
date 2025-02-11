# Используем минимальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY app/ app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir requests

# Запускаем скрипт
CMD ["python", "app/main.py"]
