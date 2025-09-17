FROM python:3.12.6-slim
LABEL maintainer="borunov65@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app/ .

CMD ["python", "main.py"]
