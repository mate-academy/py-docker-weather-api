FROM python:3.12-slim
LABEL maintainer="chebukin404@gmail.com"

WORKDIR weather_app/

ENV PYTHOUNNBUFFERED 1

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "app/main.py" ]
