FROM python:3.11.2-slim
LABEL maintainer="rybenchukv@gmail.com"

ENV PYTHONUNBUFFERED 1


WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]