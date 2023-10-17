FROM python:3.10.4-alpine
LABEL maintainer="yevabrookman@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "app/main.py"]
