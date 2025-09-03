FROM python:3.12-slim
LABEL maintainer='kostya.m.2002@gmail.com'

ENV PYTHONUNBUFFERED=1

WORKDIR  /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]

