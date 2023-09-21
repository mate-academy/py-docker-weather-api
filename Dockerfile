FROM python:3.10.4-alpine
LABEL maintainer="o.denysenko@hotmail.com"

ENV PYTHONUNBUFFERED=1 \
    API_KEY=""

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
