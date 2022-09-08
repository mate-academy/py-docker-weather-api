FROM python:3.10.4-slim
LABEL maintainer="anton.lasko1993@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py", "runserver"]
