FROM python:3.11.0-slim
LABEL maintainer="amorallex@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/main

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app/main.py"]