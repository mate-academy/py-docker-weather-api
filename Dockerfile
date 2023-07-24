FROM python:3.8-slim

WORKDIR /app

COPY app/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app/main.py .

CMD ["python", "main.py"]
