FROM python:3.11-slim
LABEL maintainer="n.fabrykator@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app .

CMD ["python", "app/main.py"]