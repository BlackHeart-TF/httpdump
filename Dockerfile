# Use the Python 3.13 image
FROM python:3.13-slim

# User modifiable port
ENV PORT=80

# Set environment variable to ensure logs are unbuffered
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy the Python script into the container
COPY httpdump.py requirements.* /app/

# Install the required dependencies if exists
RUN if [ -f /app/requirements.txt ]; then pip install -r /app/requirements.txt; fi

EXPOSE $PORT

# Run the script when the container starts
CMD ["python", "-u", "httpdump.py"]
