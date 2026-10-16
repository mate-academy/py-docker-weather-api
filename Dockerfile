FROM python:3.13-alpine
LABEL authors="kateriina.cherepanova@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY app/requirements.txt requirements.txt
RUN pip install --no-cache-dir --no-compile -r requirements.txt

COPY app/main.py main.py

CMD ["python", "main.py"]
