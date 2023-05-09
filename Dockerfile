FROM python:3.10.7
LABEL maintainer="yura.vataschuk@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]


#FROM python:3.11-alpine
#RUN mkdir /app
#ADD . /app
#WORKDIR /app
#RUN pip install -r requirements.txt
#EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]