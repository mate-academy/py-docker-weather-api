FROM python:3.9.6-slim
LABEL mainteiner="vadim.shkarbul@gmail.com"

ENV PYTHONUNBUFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
