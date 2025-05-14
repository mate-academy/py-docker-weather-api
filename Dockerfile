FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY app/main.py .
COPY .env .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
