FROM python:3.11
LABEL authors="roleksii"

ENV PYTHONNBUFFERED=1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN  pip install -r requirements.txt

COPY . .


CMD ["python", "app/main.py"]