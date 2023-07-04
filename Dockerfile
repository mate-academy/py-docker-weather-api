FROM python:3.11.0-alpine
LABEL maintainer="ivan.korshunov.1997@gmail.com"
# Who is responsible for this project.

ENV PYTHONUNBUFFERED 1
# Set this in order to see logs.

WORKDIR app/
# Path inside of the container --> directory app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
# Copy py-docker-weather-api2 directory to
# app/ directory in container

CMD ["python3", "app/main.py"]
