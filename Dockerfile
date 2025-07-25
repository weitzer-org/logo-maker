FROM --platform=linux/amd64 python:3.9-slim

WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Cloud Run will set PORT environment variable
EXPOSE ${PORT}

# Start the app
CMD exec gunicorn --bind :${PORT} --workers 1 --threads 8 --timeout 0 'app:app'