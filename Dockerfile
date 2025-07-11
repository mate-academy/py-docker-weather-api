FROM python:3.12
LABEL maintainer="kol230305@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY .env .
COPY app/main.py .

CMD ["python", "main.py"]