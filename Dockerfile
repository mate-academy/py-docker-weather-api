FROM python:alpine3.24
LABEL maintainer="skiv08098@gmail.com"


ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]