FROM python:3.10.8-slim
LABEL maintainer="diashiroks@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR weather_api/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
