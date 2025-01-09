# Use the official Python image from the Docker Hub as the base image
FROM python:3.9-slim

# Set environment variables to prevent Python from writing .pyc files
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install necessary system dependencies for Playwright and Chromium
RUN apt-get update && apt-get install -y \
  wget \
  ca-certificates \
  curl \
  fonts-liberation \
  gnupg2 \
  libappindicator3-1 \
  libasound2 \
  libatk-bridge2.0-0 \
  libatk1.0-0 \
  libcups2 \
  libdbus-1-3 \
  libgdk-pixbuf2.0-0 \
  libnspr4 \
  libnss3 \
  libx11-xcb1 \
  libxcomposite1 \
  libxdamage1 \
  libxrandr2 \
  lsb-release \
  xdg-utils \
  libjpeg-dev \
  libpng-dev \
  libwebp-dev \
  --no-install-recommends \
  && rm -rf /var/lib/apt/lists/*

# Install Playwright dependencies
RUN apt-get update && apt-get install -y \
  libx11-xcb1 \
  libnss3 \
  libatk-bridge2.0-0 \
  libgtk-3-0 \
  libxcomposite1 \
  libxrandr2 \
  libgbm1 \
  libasound2 \
  libappindicator3-1 \
  libgdk-pixbuf2.0-0 \
  xdg-utils \
  --no-install-recommends \
  && rm -rf /var/lib/apt/lists/*

# Install Python dependencies from requirements.txt
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright
RUN pip install playwright
RUN python -m playwright install --with-deps

# Install the browsers (Chromium by default)
RUN playwright install chromium-headless-shell

# Copy the entire project into the container
COPY . /app/

# Expose the FastAPI app port
EXPOSE 8000

# Command to run the FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
