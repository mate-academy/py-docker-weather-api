FROM python:3.9-alpine
LABEL maintainer="yaroslavbiziuk@gmail.com"

ENV PYTHONUNBUFFERED 1
ENV API_KEY 45aa589d47f145f3874211504242703

WORKDIR app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
