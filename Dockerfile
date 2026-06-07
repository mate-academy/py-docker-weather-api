FROM python:3.12-slim

WORKDIR /app

COPY requirements.app.txt .
RUN pip install --no-cache-dir -r requirements.app.txt

COPY app/main.py .

CMD ["python", "main.py"]
