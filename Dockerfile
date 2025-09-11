FROM python:3.13-slim
LABEL maintainer="yor_docker_username"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app

CMD ["python", "app/main.py"]
