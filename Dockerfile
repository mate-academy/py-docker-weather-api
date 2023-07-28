FROM python:3.11-alpine
LABEL maintainer="dashazaika@gmail.com"

ENV PYTHONBUFFERED 1


WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py", "0.0.0.0:8000"]
