FROM python:3.11-alpine

WORKDIR /usr/src/project

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

CMD ["python", "app/main.py"]