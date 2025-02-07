FROM python:3.11.6-alpine3.18 as builder
LABEL maintainer="zaharsavchen@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

FROM builder

WORKDIR /app
COPY app/ .

CMD ["python", "main.py"]
