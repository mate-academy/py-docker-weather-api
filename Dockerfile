FROM python:3.12.9-slim
LABEL maintainer="chukhno.maksym@gmail.com"

ENV PUTHONNBUFFERED = 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN  pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]