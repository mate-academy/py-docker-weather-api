FROM python:3.11.13-alpine3.22

WORKDIR /app

RUN pip install --no-cache-dir requests

COPY app/main.py .

CMD ["python", "main.py"]
