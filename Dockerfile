FROM python:3.14.0-slim
LABEL authors="fedir1357@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY app/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app/main.py main.py

CMD ["python", "main.py"]
