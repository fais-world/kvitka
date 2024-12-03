# Use the official Python slim image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the Flask app's port
EXPOSE 5000

# Use Gunicorn as the production WSGI server
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "src.app:app"]
