FROM python:3.11-slim-buster

WORKDIR /weather_app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]