FROM python:3.10-alpine

LABEL maintainer="alexsotnikov"

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY app/ .

RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev openssl-dev \
    && pip install --no-cache-dir requests \
    && apk del .build-deps gcc musl-dev libffi-dev openssl-dev

CMD ["python", "main.py"]
