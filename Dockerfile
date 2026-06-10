FROM python:3.10.8-slim

WORKDIR /app

COPY requirements-docker.txt .
RUN pip install --no-cache-dir -r requirements-docker.txt

COPY app ./app

CMD ["python", "app/main.py"]
