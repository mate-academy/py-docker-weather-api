FROM python:3.12.2-alpine3.19
LABEL maintainer="danylo3002@gmail.com"

ENV PYTHONUNNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
