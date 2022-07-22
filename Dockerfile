FROM python:3.10.4-alpine
LABEL maintainer="darten360"

ENV PYTHONUNBUFERED 1 API_KEY

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
