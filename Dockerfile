FROM python:3.12.0-slim
LABEL develop_by="sergmarten21@gmail.com"

ENV PYTHONUNNBUFFERED=1


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV API_KEY=$API_KEY

COPY . .

CMD ["python", "-m", "app.main"]
