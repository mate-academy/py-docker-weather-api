FROM python:3.11.6-alpine3.18

LABEL maintainer="danilsivkovic@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD ["python", "app/main.py"]