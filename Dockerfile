FROM python:3.13-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /weather_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app/ app/

CMD ["python", "app/main.py"]
