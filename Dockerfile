FROM python:3.10.4
LABEL maintainer="gladiolus0707@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN docker pull ivangls/docker-weather


COPY . .

CMD ["python", "app/main.py"]
