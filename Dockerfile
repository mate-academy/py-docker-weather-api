FROM python:3.10.0-slim

LABEL maintainer="bku089@gmail.com"

WORKDIR /app

COPY requirements.txt .

COPY app/ .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
