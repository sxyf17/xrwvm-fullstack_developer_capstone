# Use the official slim Python image as a base image
FROM python:3.12.0-slim-bookworm

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONWRITEBYTECODE=1
ENV APP=/app

# Set the working directory inside the container
WORKDIR $APP

# Install system dependencies (optional but common for some Python projects)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt to the working directory
COPY requirements.txt $APP

# Install the Python dependencies from requirements.txt
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

# Copy the entire project code to the working directory
COPY . $APP

# Make sure entrypoint.sh is executable
RUN chmod +x /app/entrypoint.sh

# Expose port 8000 for the application
EXPOSE 8000

# Define the entrypoint for the Docker container
ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]

# Default command to run the application using gunicorn
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangoproj.wsgi"]