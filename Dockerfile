FROM python:3.11.0-slim
LABEL maintainer="ygudzovski@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR weather_app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
