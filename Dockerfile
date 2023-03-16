FROM python:3.10.4-slim

LABEL maintaner="maggielit"

ENV PYTHONBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python","app/main.py","get_weather"]
