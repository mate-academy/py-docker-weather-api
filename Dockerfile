FROM python:3.12-alpine3.24

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHON_UNBUFFERED=1

WORKDIR /app/

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]


