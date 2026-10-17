FROM python:3.10.8-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHON_UNBUFFERED=1

WORKDIR /app/

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]


