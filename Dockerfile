FROM python:3.12-alpine3.22
LABEL authors="sobkot"

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]