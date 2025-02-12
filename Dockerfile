FROM python:3.12-alpine3.18
LABEL maintainer="lauman@ukr.net"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "app.py"]



