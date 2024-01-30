FROM python:3.11-slim
LABEL maintainer="moleksii10@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]