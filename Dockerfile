FROM python:3.10.8-slim
LABEL maintainer="bogdantheone"

ENV PYTHONUNBUFFERED 1

WORKDIR weather_app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
