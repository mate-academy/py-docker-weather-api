FROM python:3.11.12-slim
LABEL maintainer="wenhun1@gmail.com"

ENV PYTHONNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
