# Use the official Airflow image as a base
FROM apache/airflow:2.7.0

# Set the environment variable to prevent airflow from running in a non-root mode
ENV AIRFLOW_HOME=/opt/airflow

# Set the correct working directory
WORKDIR /opt/airflow

# Switch to root user to install dependencies
USER root

# Install system dependencies if needed (e.g., for pyppeteer)
RUN apt-get update && \
  apt-get install -y wget curl gnupg2 && \
  apt-get install -y vim && \
  apt-get clean

# Copy DAGs and configurations into the Airflow container
COPY dags /opt/airflow/dags
# COPY scraper.py /opt/airflow/scraper.py
# COPY utils.py /opt/airflow/utils.py

# RUN chown airflow:root /opt/airflow/scraper.py
# RUN chown airflow:root /opt/airflow/utils.py

# Switch back to the airflow user if needed
USER airflow

# Install additional Python dependencies (Airflow, etc.)
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Set default entrypoint for Airflow
ENTRYPOINT ["bash", "-c", "airflow scheduler & airflow webserver"]
