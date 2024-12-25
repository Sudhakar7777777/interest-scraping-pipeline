# Use the official Airflow image as a base
FROM apache/airflow:2.7.0

# Set the environment variable to prevent airflow from running in a non-root mode
ENV AIRFLOW_HOME=/usr/local/airflow

# Install system dependencies if needed (e.g., for pyppeteer)
RUN apt-get update && \
  apt-get install -y wget curl gnupg2 && \
  apt-get clean

# Install additional Python dependencies (Airflow, etc.)
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Copy DAGs and configurations into the Airflow container
COPY dags /usr/local/airflow/dags

# Set the correct working directory
WORKDIR /usr/local/airflow

# Set default entrypoint for Airflow
ENTRYPOINT ["bash", "-c", "airflow scheduler & airflow webserver"]
