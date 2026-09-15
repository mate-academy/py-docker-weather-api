FROM python:3.10.8-slim

WORKDIR /app

COPY requirements.txt .
COPY .flake8 .

RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

CMD ["python", "app/main.py"]