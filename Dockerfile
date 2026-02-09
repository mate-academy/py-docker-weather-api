# Використовуємо легкий базовий образ
FROM python:3.11-alpine

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо лише файл залежностей для кешування
COPY requirements.txt .

# Встановлюємо залежності без збереження кешу pip
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо вміст папки app у контейнер
COPY app/ ./app/

# Запускаємо скрипт
CMD ["python", "app/main.py"]