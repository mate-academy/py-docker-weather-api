FROM python:3.10-slim

LABEL maintainer="Jakub Paluch"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/ app/

CMD ["python", "app/main.py"]