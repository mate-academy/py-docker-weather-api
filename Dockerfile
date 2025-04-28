FROM python:3.13-alpine
LABEL maintainer="volodymyr.vinohradov@gmail.com"

ENV PYTHONUNBUFFERED=1
ENV UV_PROJECT_ENVIRONMENT="/usr/local/"

WORKDIR /app
COPY pyproject.toml uv.lock ./

RUN pip install --no-cache-dir uv \
    && uv sync --no-cache-dir \
    && pip uninstall -y pip setuptools wheel uv \
    && rm -rf /root/.cache /root/.pip

COPY app/ .

CMD ["python", "main.py"]
