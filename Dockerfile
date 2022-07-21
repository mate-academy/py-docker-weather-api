FROM python:3.10.4-slim-buster
LABEL maintainer="tarasnester414@gmail.com"

ENV PYTHONUNBUFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "app/main.py"]
