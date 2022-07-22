FROM python:3.10.5
LABEL maintainer = "belochard@gmail.com"

ENV PYTHONUNBUFFERED 1
ENV API_KEY "b45afc4e7b2a4bf9a02151752222107"

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]