FROM python:3.13-slim

WORKDIR /app

COPY requirements_docker.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY app app

CMD ["python", "app/main.py"]