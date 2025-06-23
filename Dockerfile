FROM python:3.14.0b3-alpine3.21
LABEL maintainer="antonbliznuk71@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python3","main.py"]