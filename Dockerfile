FROM python:3.11.6-alpine3.18

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN adduser \
    --disabled-password \
    --no-create-home \
    user
USER user

COPY . .

EXPOSE 8000

CMD ["python3", "app/main.py"]
