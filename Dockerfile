FROM python:3.10.10-slim-buster
LABEL maintainer="vborovets0@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py", "0.0.0.0:8000"]