FROM python:3.11-slim
LABEL maintainer="denischernish19012004@gmail.com"

ENV PYTHONBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .


CMD ["python", "app/main.py"]

