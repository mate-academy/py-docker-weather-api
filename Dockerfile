FROM python:3.10.11-slim
LABEL maintainer="anton_komarov_qa@ukr.net"

ENV PYTHONBUFFERED 1

WORKDIR app/app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]