FROM python:3.14-slim

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app/main.py"]