FROM python:3.10-slim-bullseye

WORKDIR /app

# Copy the application files
COPY . /app

# Update the server, install AWS CLI, and clean up the cache to save space
RUN apt-get update -y && \
    apt-get install awscli -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python requirements without saving the bloated cache files
RUN pip install --no-cache-dir -r requirements.txt

# Start the application
CMD ["python3", "app.py"]