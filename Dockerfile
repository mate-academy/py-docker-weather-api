FROM python:3.13-alpine

WORKDIR /app

RUN pip install --no-cache-dir requests

COPY app/main.py main.py

CMD ["python", "main.py"]
