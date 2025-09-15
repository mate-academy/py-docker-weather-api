FROM python:3.12.3-slim

WORKDIR /app

COPY requirements.txt requirements.txt

LABEL authors="mechanicus"

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]