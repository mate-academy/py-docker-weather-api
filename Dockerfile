FROM python:3.11-alpine:3.18

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]