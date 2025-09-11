FROM python:3.10-slim
LABEL maintainer="pashock1337@gmail.com"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]