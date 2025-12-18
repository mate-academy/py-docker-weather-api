FROM python:3.12-slim-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /App

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
