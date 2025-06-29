FROM python:3.11-slim

LABEL maintainer="ngayka@gmail.com"

ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ app/
CMD ["python", "app/main.py"]
