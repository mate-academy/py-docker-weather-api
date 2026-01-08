FROM python:3.13-slim

LABEL maintainer="ivanventik@example.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY app/main.py /app/main.py

RUN pip install --no-cache-dir requests

CMD ["python", "main.py"]
