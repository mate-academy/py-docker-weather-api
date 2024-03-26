FROM python:3.10-alpine
LABEL maintainer="p.nakonechnyi@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "-m", "app.main" ]
