# Instructions for Running the Stack

## Clone the Repo and Navigate to the Project Directory:

```bash
git clone <your-repo-url>
cd <project-directory>
````

## Build and Start the Docker Containers:

Ensure that Docker and Docker Compose are installed, and then run the following command:
```bash
docker-compose up --build
````

### Access Services:

-    Airflow Web UI: http://localhost:8080
-    Scraper API UI: http://localhost:8000/docs
-    Prometheus: http://localhost:9090
-    Grafana: http://localhost:3000
-    Default credentials: ```admin / admin```
-    Alertmanager: http://localhost:9093 (to view alerts)

### Configure Prometheus Targets:

Prometheus will scrape metrics from Airflow, the scraper, and itself based on the prometheus.yml configuration.

Alerts will be handled by Alertmanager, and you can configure them to notify you via Slack, email, or other channels.
