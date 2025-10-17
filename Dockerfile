FROM python:3.12-slim
LABEL maintainer="volikitin.vitaliy@icloud.com"

ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --no-cache-dir --disable-pip-version-check -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]