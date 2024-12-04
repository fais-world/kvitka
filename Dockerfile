FROM python:3.13-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ /app/src
WORKDIR /app/src

# Expose the app on port 8080
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
