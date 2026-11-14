FROM python:3.13-slim
LABEL org.opencontainers.image.authors="creedbroth@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "app/main.py"]
