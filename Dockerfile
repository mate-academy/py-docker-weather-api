FROM python:3.13.0-alpine3.19
LABEL maintainer="bashyrov"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

CMD ["python", "main.py"]