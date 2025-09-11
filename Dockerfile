FROM python:3.12-slim
LABEL authors="Otstoy"

ENV PYTHONBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app/ .

CMD ["python", "main.py"]
