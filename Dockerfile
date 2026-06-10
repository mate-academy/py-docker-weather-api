FROM python:3.10.8-slim

WORKDIR /app

COPY app/ /app/

RUN pip install --no-cache-dir requests python-dotenv

CMD ["python", "main.py"]
