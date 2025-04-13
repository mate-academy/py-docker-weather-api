FROM python:3.12.8-slim

WORKDIR /app

COPY app /app
RUN pip install --no-cache-dir requests

CMD ["python", "main.py"]
