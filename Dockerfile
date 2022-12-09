FROM python:3.11-slim
LABEL maintainer="dastex1411@gmail.com"

ENV PYTHONUNBAFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "app/main.py"]
