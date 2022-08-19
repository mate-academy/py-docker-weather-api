FROM python:3.10.4-alpine
LABEL maintainer=www.shpachyk98@gmail.com

ENV PYTHONBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]