# Use an official Python runtime as a parent image
FROM python:3.12-slim-buster

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app/health

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Expose port
EXPOSE 8000

# Run Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "project.wsgi:application"]
