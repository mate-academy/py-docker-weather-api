FROM python:3.12.15-slim-bookworm AS builder

WORKDIR /app

COPY . . 

RUN pip install -r requirements.txt


CMD ["python", "app/main.py"]