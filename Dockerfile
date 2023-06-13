FROM python:3.10.8-slim
LABEL maintainer="yuraua5@gmail.com"

ENV PYTHONUNBUFFERED 1
ENV API_KEY NONE

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
