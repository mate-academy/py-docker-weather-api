FROM python:3.9-slim
LABEL maintainer="korotenko.qndroid@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR weather_api/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]