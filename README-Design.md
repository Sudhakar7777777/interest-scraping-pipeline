# Interest Rates Scraping Pipeline with SQLite Storage

## Overview

This solution provides an optimized pipeline for scraping Interest Rates from a website, storing the data in **SQLite**, and orchestrating the pipeline using **Apache Airflow**. The pipeline also integrates **ELK** (Elasticsearch, Logstash, Kibana) for logging, **Prometheus** for monitoring, and is containerized with **Docker Compose**. 

The following components are included:
- **Apache Airflow** for scheduling and orchestrating tasks.
- **SQLite** for persistent data storage.
- **ELK Stack** for logging and visualizing logs.
- **Prometheus** for monitoring and alerting.
- **Docker Compose** for easy deployment and orchestration of the pipeline.

---

## Architecture

### 1. **Airflow Pipeline Setup**
Airflow will orchestrate the entire process of scraping, data cleaning, and storing in the SQLite database.

- **Scraping Task**: Scrape the Interest Rates data from the website.
- **Data Cleaning Task**: Process the raw data (format tenure, clean interest rates).
- **Store Data Task**: Store the cleaned data into an SQLite database.
  
Airflow will be used to schedule the tasks, manage retries, handle failure alerts, and track job statuses.

### 2. **SQLite for Data Storage**
SQLite will be used to persist the scraped interest rates data. The data schema will have two main fields:
- **Tenure** (e.g., "Years >= 1 < 2")
- **USD Interest Rate** (e.g., "5.75")

SQLite is file-based, so the database will be stored in the container and persisted using Docker volumes.

### 3. **Logging with ELK Stack**
Logs will be aggregated and visualized using **ELK**:
- **Elasticsearch** will store logs.
- **Logstash** will collect and ship logs.
- **Kibana** will be used for querying and visualizing the logs.

### 4. **Monitoring with Prometheus**
Prometheus will collect metrics from Airflow and other system components (e.g., CPU, memory usage). Metrics will be visualized using **Grafana**. Alerts will be set up in Prometheus for job failures, task retries, and other critical events.

---

## SQLite Schema Design

We will create a SQLite table to store the scraped data. The schema will look like this:

```sql
CREATE TABLE IF NOT EXISTS interest_rates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tenure TEXT NOT NULL,
    usd_interest_rate TEXT NOT NULL,
    date_scraped TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Conclusion
This solution provides an end-to-end pipeline that:

- Scrapes Interest Rates from a website.
- Processes and stores the data into an SQLite database.
- Orchestrates the entire process using Apache Airflow.
- Monitors the pipeline using Prometheus and Grafana.
- Logs the pipeline’s execution using the ELK Stack.
With Docker Compose, all services can be easily managed, making it simple to set up and deploy the pipeline in any environment.
