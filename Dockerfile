FROM python:3.12-alpine
LABEL maintainer="pythonzem@gmail.com"

ENV PYTHONUNNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]