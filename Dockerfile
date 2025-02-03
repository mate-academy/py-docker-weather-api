FROM python:3.12.8-alpine3.21
LABEL maintainer="koliesnichenko2018@ukr.net"
LABEL description="Container for fetching weather data using WeatherAPI"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
