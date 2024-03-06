FROM python:3.12.2-slim
LABEL maintainer="super.shepard2@gmail.com"

ENV PYTHONBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "./app/main.py"]
