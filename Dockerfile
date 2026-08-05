FROM python:3.10-slim
LABEL maintainer="mr.denisyakubenko@gmail.com"

ENV PYTHONNBUFFERED 1

WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]