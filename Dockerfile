FROM python:3.10.16-alpine3.20
LABEL maintainer="bogdangavriluk12345@gmail.com"

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]