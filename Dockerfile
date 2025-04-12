FROM python:3.10.8-slim
LABEL maintainer="kovalukilla271@gmail.com"

ENV PYTHONUNBUFFERED=1
WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
