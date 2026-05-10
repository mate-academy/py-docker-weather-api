# Используем slim версию для уменьшения размера образа
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем только файлы зависимостей для кэширования слоев
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY app/ ./

# Запуск приложения
CMD ["python", "main.py"]