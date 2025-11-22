FROM python:3.11.6-alpine3.18
LABEL maintainer="antonina.ivanets@ukr.net"

ENV PYTHONUNBUFFERED=1

WORKDIR app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

CMD ["python", "main.py"]
