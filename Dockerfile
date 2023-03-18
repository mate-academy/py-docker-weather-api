FROM python:3.8.9-slim
LABEL maintainer="kolyazakharov94@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/main.py


COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .


CMD ["python", "app/main.py"]