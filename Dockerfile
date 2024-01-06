FROM python:3.11.7-slim
LABEL maintainer="anastasia.su.po@gmail.com"
ENV PYTHONUNBUFFERED 1

WORKDIR app/
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y ca-certificates

COPY app/main.py main.py
COPY .env .env
CMD ["python", "main.py"]
