FROM python:3.11.15-alpine3.22

LABEL maintainer="yukhnenko.o@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "app/main.py"]
