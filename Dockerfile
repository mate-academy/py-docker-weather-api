FROM python:3.12-alpine
LABEL maintainer="dmitriykuzmin@ymail.com"

ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir

COPY app ./app

CMD ["python", "app/main.py"]
