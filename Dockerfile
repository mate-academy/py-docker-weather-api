FROM python:3.11.4-slim
LABEL maintainer="8773927@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR weather_app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]