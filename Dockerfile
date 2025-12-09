FROM python:3.10-slim

ENV PYTHONBUFFERED=1
# Set working directory
WORKDIR /app

# Copy dependency list and install
COPY requirements.txt .
RUN pip  install -r requirements.txt

# Copy the app files
COPY . .

# Run the FastAPI server
CMD ["python", "app/main.py"]