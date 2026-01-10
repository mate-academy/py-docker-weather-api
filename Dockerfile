FROM python:3.12-slim
LABEL authors="king.krollie@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r --no-cache-dir requirements.txt

COPY app/ .

CMD ["python", "main.py"]

