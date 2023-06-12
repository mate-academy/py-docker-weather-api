FROM python:3.11.1
LABEL maintainer="acheros4@gmail.com"

ENV PYTHONBUFFERED 1

WORKDIR root/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "./app/main.py"]
