FROM python:3.10.12-slim

WORKDIR /app

COPY app/main.py /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]