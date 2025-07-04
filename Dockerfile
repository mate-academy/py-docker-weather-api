FROM python:3.13-slim
LABEL maintainer="s.merlenko@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app/main.py .

CMD ["python", "main.py"]