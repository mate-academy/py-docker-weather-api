FROM python:3.10.4-alpine

LABEL maintainer="nazar.lavrik9@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY . .
RUN pip install -r requirements.txt

CMD ["python", "app/main.py"]
