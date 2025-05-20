FROM python:3.11-alpine3.21
LABEL maintaner="andriishtaher@gmail.com"

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

CMD ["python", "app/main.py"]