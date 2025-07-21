FROM python:3.13-alpine3.21
LABEL maintainer="videv1410@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app/ .

CMD ["python", "app/main.py"]
