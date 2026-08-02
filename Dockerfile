FROM python:3.12-alpine
LABEL org.opencontainers.image.authors="Denys <denytop3@gmail.com>"

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
