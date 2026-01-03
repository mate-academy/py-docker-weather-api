FROM python:3.11.14-alpine3.23

LABEL maintainer="arseniykushnir2007@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR weather-api/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN apk add --no-cache bash

COPY . .

CMD ["python", "./app/main.py"]
