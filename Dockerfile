FROM python:3.10.8-slim
LABEL maintainer="vskesha@gmail.com"

ENV PYTHONUNBUFFERED=1
ENV DONTWRITEBYTECODE=1

WORKDIR /root

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
