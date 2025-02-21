FROM python:3.11-slim
LABEL maintainer="vasyabarilyuk1427@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY app/main.py ./main.py
COPY requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
