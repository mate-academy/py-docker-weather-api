FROM python:3.9-slim
LABEL maintainer="dolinskiytoha@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./app/ .

CMD ["python", "main.py"]
