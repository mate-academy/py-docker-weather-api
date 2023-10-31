FROM python:3.9.2
LABEL maintainer="yaroslavmazurkevych@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR weather/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
