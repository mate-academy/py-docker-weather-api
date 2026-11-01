from python:3.10.8-slim
LABEL maintainer="imvovo4kaa@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app/.

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
