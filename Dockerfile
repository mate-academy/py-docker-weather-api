FROM python:3.13.7-slim
LABEL maintainer="maksbusl@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR ./

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install requests python-dotenv

COPY . .

CMD ["python", "app/main.py"]
