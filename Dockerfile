FROM python:3.11.6-slim

LABEL maintainer="malovaniy.an@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY app/main.py app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "./app/main.py"]
