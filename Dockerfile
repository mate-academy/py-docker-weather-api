FROM python:3.11.4
LABEL maintainer="ladyvaleriya13@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY .  .

CMD ["python", "app/main.py"]
