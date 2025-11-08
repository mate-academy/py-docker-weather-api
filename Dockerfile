FROM python:3.9.25-alpine3.22
LABEL maintainer="v.nykonenko@gmail.com"
ENV PYTHOUNNBUFFERED 1
WORKDIR app/
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app/main.py", "runserver", "0.0.0.0:8000"]