FROM python:3.11.0-slim

LABEL maintainer="terrya@ukr.net"

ENV PYTHONUNBUFFERED 1
ENV API_KEY "9b4c04f7fe1b4ec0b6b94922230703"

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]