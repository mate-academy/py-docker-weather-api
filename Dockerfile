from python:3.11-alpine
LABEL maintainer="imvovo4kaa@gmail.com"

ENV PYTHONBUFFERED 1

WORKDIR app/ ./app/

COPY requirements.txt requirements.txt
RUN pip install requests

COPY . .

CMD ["python", "app/main.py"]
