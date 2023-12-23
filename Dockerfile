FROM python:3.11-slim
LABEL maintainer="dzhurarostislav@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
ENV TZ=Europe/Kiev

CMD ["python", "app/main.py"]
