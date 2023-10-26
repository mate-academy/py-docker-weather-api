<<<<<<< HEAD
FROM python:3.10.8-slim
LABEL maintainer="savik1992@gmail.com"

ENV PYTHONUNBUFFERED 1
ENV API_KEY NONE

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
=======
FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    gettext \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
>>>>>>> 65fd3b4f0b1a8dce5c0d8f1e49c18f9f7e98d0c9
