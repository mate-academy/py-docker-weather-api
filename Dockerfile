FROM python:3.9-slim
LABEL maintainer="anettaabl@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py", "0.0.0.0:8000"]