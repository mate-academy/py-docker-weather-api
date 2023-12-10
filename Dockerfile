FROM python:3.10.12-slim
LABEL maintainer="sakhaline@gmail.com"

ENV PYTHONUNBUFFERED 1
ENV WEATHER_API_KEY ""

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
