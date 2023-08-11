FROM python:3.11.3-slim
LABEL maintainer="vbabiyenko"

ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
