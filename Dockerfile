FROM python:3.11-slim
LABEL maintainer="den.prislipskyi@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "/main.py"]