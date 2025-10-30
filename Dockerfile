FROM python:3.12
LABEL maintainer="navolokovz@gmail.com"

ENV PYTHOUNNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN ["python", "app/main.py"]
