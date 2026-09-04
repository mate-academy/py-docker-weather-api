FROM python:3.10.8-slim

LABEL maintainer="lukia"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app/ .

CMD ["python", "main.py"]
