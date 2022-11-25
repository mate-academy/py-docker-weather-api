FROM python:3.10-slim
LABEL maintainer="gsstahiv@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
