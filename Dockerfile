FROM python:3.9-slim-bullseye
LABEL maintainer="darkvader.ukr.net@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR root/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "/root/app/main.py"]
