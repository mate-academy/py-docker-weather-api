FROM python:3.11-alpine3.18
LABEL maintainer="juliakamynskaya@gmail.com"

ENV PYTHONBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
