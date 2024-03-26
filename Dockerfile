FROM python:3.12.2-alpine3.19
LABEL maintainer="tulyulyuk91@gmail.com"

ENV pythonbuffered=1

WORKDIR docker_app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
