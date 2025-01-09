# Use official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install system dependencies if needed (e.g., for pyppeteer)
RUN apt-get update && \
  apt-get install -y wget curl gnupg2 && \
  apt-get clean

# Copy requirements and install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the scraper code
COPY . /app

# Expose the necessary port (if the scraper exposes a port)
EXPOSE 8081

# Set the default command to run the scraper
CMD ["python", "-m", "scraper"]
