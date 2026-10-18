FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY app/requirements requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY app/main.py /app

CMD ["python", "main.py"]
