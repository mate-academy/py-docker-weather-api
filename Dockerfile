FROM python:3.12-slim

WORKDIR /app

COPY app/ /app/

RUN pip install requests

CMD ["python", "main.py"]
