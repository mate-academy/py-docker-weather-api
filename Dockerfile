FROM python:3.11-slim
LABEL maintainer="danylkiv.pavlo@gmail.com"

WORKDIR /app

ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]