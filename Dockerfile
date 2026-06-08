FROM python:3.8-slim-buster

WORKDIR /py-docker-weather-api

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

CMD ["python", "app/main.py"]