FROM python:3.10.4-slim
LABEL maintainer ="nazar.psheiuk@gmail.com"

ENV PYTHONUNBUFFERED 1
ENV API_KEY my_api_key

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]