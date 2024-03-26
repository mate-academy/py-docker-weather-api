FROM python:3.12.1-slim
LABEL maintainer="example@example.com"

ENV PYTHOUNNBUFFERED 1

WORKDIR weather-api/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
