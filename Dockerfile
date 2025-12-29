FROM python:3.13-slim
LABEL maintainer="totsevich02@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app/main.py"]
