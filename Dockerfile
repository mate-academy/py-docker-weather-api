FROM python:3.10.8-slim

LABEL maintainer="petropavliuk12.05@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

CMD ["python", "-u", "main.py"]
