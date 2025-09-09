FROM python:3.13-slim

WORKDIR /app

RUN pip install --no-cache-dir requests

COPY app/ ./app/

CMD ["python", "app/main.py"]
