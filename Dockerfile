FROM python:3.10.8-slim

LABEL maintainer = "dimior1992@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "app/main.py"]
