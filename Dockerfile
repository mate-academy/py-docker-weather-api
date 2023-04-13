FROM python:3.9.10-slim-buster

LABEL maintainer="legus96@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
