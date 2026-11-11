FROM python:3.14-slim

WORKDIR /opt/project

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

CMD ["python", "app/main.py"]
