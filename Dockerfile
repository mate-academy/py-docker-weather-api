FROM python:3.10-slim
LABEL maintainer="khomenkotaras1305@gmail.com"

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
