FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    && pip install --no-cache-dir requests \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app


COPY app/ ./app/


CMD ["python", "app/main.py"]
