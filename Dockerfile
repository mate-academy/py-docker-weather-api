FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install --no-cache-dir requests

COPY app /app

CMD ["python", "main.py"]
