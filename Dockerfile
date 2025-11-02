FROM python:3.12.12-alpine3.22
LABEL maintainer="bokovdenys.dev@gmail.com"
ENV PYTHONUNBUFFERED 1

WORKDIR get-weather-app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "app/main.py"]
