FROM python:3.9.13
LABEL maintainer="3lobites@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
COPY app/main.py main.py
COPY app/.env .env

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]
