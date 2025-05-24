FROM python:3.11-slim
LABEL maintainer="maximuschampion2002@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

CMD ["python", "main.py"]
