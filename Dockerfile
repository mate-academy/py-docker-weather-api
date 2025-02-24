FROM python:3.11-slim
LABEL maintainer="zhyganiuk.elizaveta@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /.

RUN pip install -r requirements.txt

COPY ./app .

CMD ["python", "main.py"]
