FROM python:3.8.10-slim

LABEL maintainer="mazurinka29@gmail.com"

ENV  PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "app/main.py"]
