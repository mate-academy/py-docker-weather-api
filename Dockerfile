FROM python:3.12.11-alpine3.22
LABEL authors="akostenikov@gmail.com"

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR app/

RUN pip install --no-cache-dir requests

COPY app/main.py .

CMD ["python", "main.py"]