FROM python:3.12-alpine
LABEL maintainer="maksym.symonovych@gmail.com"

ENV PYTHOUNNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "-m", "app.main"]
