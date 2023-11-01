FROM python:3.11.5-slim
LABEL maintainer="edlrian814@gmail.com"

ENV PYTHONUNBUFFERED 1

RUN pip install requests

COPY . .

WORKDIR app/

CMD ["python", "main.py"]