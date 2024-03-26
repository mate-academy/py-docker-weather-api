FROM python:3.11-slim
LABEL maintainer="50513970@skin.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY app/ .

CMD ["python", "main.py"]
