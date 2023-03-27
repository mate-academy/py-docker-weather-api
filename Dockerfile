FROM python:3.11.2-slim

LABEL maintainer = "soloha7965@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/main.py

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python"]