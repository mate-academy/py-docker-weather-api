FROM python:3.11-alpine
LABEL maintainer="imileckiy@gmail.com"

ENV PYTHONUNBUFFERED  1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./app /app

CMD ["python", "app/main.py"]
