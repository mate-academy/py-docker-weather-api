FROM python:3.11-slim
LABEL maintainer="markus9869@gmail.com"

WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY app/ .

CMD ["python", "main.py"]

