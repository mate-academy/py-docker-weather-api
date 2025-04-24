FROM python:3.13-alpine AS init-stage
WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.13-alpine AS entry-stage
WORKDIR /app
COPY --from=init-stage /install /usr/local
COPY ./app .

ENV PYTHONUNBUFFERED=1 API_KEY=""

ENTRYPOINT ["python", "main.py"]
