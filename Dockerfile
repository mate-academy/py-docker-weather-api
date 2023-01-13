FROM python:3.10.6-slim

LABEL maintainer="kvmltkv@gmail.com"

ENV PYTHONUNBUFFERD=1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py", "runserver", "0.0.0.0:8000"]
