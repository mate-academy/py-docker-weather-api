FROM python:3.10.4
LABEL maintainer="23.smutok@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "app/main.py"]
