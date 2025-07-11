FROM python:3.10.8-slim

LABEL maintainer="a9p9m@gmail.com"

ENV PYTHONUNBUFFERED=1
ENV API_KEY=""

WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]
