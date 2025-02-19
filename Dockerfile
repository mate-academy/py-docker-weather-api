FROM python:3.13.2-alpine3.21
LABEL maintainer="julia4406@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /weather

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./app .

CMD ["python", "main.py"]
