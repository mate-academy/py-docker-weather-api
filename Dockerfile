FROM python:3.11-slim-bookworm
LABEL maintainer="deibukdenys@gmail.com"

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "app/main.py" ]
