FROM python:3.10.4
LABEL maintainer="gladiolus0707@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN docker images

RUN docker pull ivangls/docker-weather

RUN docker images

RUN docker run -e API_KEY="6f5034b237604c6095f61436230602" ivangls/docker-weather


COPY . .

CMD ["python", "app/main.py"]
