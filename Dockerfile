FROM python:3.13-slim

LABEL maintainer="Fabio Silva"

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
