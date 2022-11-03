FROM python:3.10.8-slim
LABEL maintainer="olbody12@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

EXPOSE 8001

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
