FROM python:3.7.5-slim
LABEL maintainer="maksym71417@gmail.com"

ENV PYTHONBUFFERED 1

WORKDIR weather_app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
