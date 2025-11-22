FROM python:3.12-alpine3.21
LABEL maintainer="kononovb777@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app/ .

CMD ["python", "main.py", "runserver", "0.0.0.0:8000"]
