FROM python:3.10-alpine
LABEL maintainer="ilias@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app/main.py app/main.py

CMD ["python", "app/main.py"]