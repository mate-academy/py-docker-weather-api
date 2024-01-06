FROM python:3.11.1-slim
LABEL maintainer = callogan217@gmail.com

ENV PYTHONBUFFERED 1

WORKDIR weather_app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
