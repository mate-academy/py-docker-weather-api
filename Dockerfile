FROM python:3.13-slim
LABEL maintainer="shcherbdmytro@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ app/
COPY main.py .

CMD ["python", "app/main.py"]
