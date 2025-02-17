FROM python:3.13-alpine3.21

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/weather-api/

COPY requirements-build.txt .

RUN pip install --no-cache-dir -r requirements-build.txt

COPY . .

CMD ["python", "app/main.py"]
