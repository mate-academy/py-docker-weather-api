FROM python:3.13-alpine
LABEL maintainer="vo.melnyk37@gmail.com"

ENV PYTHOUNNBUFFERED=1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py", "0.0.0.0:8000"]
