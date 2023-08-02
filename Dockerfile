FROM python:3.10.7-slim

LABEL maintainer = "roman.harmatiuk@gmail.com"

ENV PYHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .


CMD ["python", "app/main.py", "0.0.0.0.8000"]



