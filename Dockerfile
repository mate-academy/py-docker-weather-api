FROM python:3.11.0-slim
LABEL maintainer="mr.skyrda@gmail.com"

ENV PYTHONUNBUFFERED 1
ENV API_KEY 6aee2b17b8a842018aa122043242503

WORKDIR docker_app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]