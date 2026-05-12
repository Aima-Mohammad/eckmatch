# Base image — Python 3.12 slim to reduce image size
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependencies first
# Optimization: Docker caches this layer if requirements don't change
COPY requirements/base.txt requirements/base.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements/base.txt

# Copy application code
COPY app/ app/

# Expose the port FastAPI listens on
EXPOSE 8000

# Start the server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]