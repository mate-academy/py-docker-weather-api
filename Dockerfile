FROM python:3.11.11-slim

RUN apt update

RUN python --version

COPY app /app


RUN pip install -r requirements.txt

CMD ["python", "/app/main.py"]
