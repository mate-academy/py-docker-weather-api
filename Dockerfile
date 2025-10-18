FROM python:3.11-slim
LABEL maintainer=freepgvlad@gmail.com

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-u", "app/main.py"]
