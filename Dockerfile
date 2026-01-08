FROM python:3.10-slim
LABEL maintainer="oleg.sk2002@gmail.com"

ENV PYTHONNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]