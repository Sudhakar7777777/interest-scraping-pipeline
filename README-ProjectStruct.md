# FCNR Interest Rate Scraping Pipeline

This project contains the pipeline for scraping FCNR interest rate data.

## Folder Structure
```
fcnr_interest_rate_scraping_pipeline/
├── airflow/
│   ├── dags/
│   │   └── fcnr_interest_rate_scraping.py      # Airflow DAG to scrape FCNR interest rates
│   ├── requirements.txt                       # Airflow and dependencies (including prometheus-flask-exporter)
│   ├── Dockerfile                             # Dockerfile for the Airflow service
│   └── .env                                   # Airflow environment variables (optional)
├── db/
│   └── db.sqlite3                             # SQLite DB to store scraped data (mounted volume)
├── scraper/
│   ├── Dockerfile                             # Dockerfile for scraper service
│   ├── scraper.py                             # Scraping logic (with Prometheus metrics exposure)
│   ├── requirements.txt                       # Scraper dependencies, including prometheus_client
│   ├── logs/                                  # Logs directory (optional, for scraper logs)
│   └── .env                                   # Scraper environment variables (optional)
├── prometheus/
│   ├── prometheus.yml                         # Prometheus configuration file (scraping targets, rules)
│   ├── alertmanager.yml                       # Alertmanager configuration file (alert routing)
│   ├── alert.rules.yml                        # Prometheus alerting rules
├── config/
│   ├── airflow_config.py                      # Configuration settings for Airflow (e.g., credentials, paths)
│   ├── scraper_config.py                      # Configuration for the scraper service (e.g., URLs, timeouts)
│   └── prometheus_config.yml                  # Configuration related to Prometheus (e.g., alerting rules, scrape intervals)
├── tests/
│   ├── test_scraper.py                        # Unit tests for scraper functionality
│   ├── test_airflow.py                        # Unit tests for Airflow-related logic
│   ├── test_metrics.py                        # Unit tests for Prometheus metrics exposure
│   └── test_config.py                         # Tests for configuration files
├── docker-compose.yml                        # Docker Compose orchestration file
├── .gitignore                                 # Git ignore file
├── .dockerignore                              # Docker ignore file
├── requirements.txt                           # Global requirements for project dependencies
├── README.md                                  # Project description and instructions
└── logs/                                      # General logs folder (optional)
```

## Description of Folders and Files

- **`airflow/`**: Contains the Airflow DAGs and configuration for orchestrating the scraping pipeline.
  - **`dags/`**: Contains the Airflow DAG scripts.
  - **`Dockerfile`**: Docker configuration for running the Airflow environment.
  - **`requirements.txt`**: Python dependencies for the Airflow environment.
  - **`.env`**: Environment variables for Airflow.

- **`scraper/`**: Contains the actual web scraping logic.
  - **`scraper.py`**: Main script for scraping FCNR data.
  - **`utils.py`**: Utility functions used by the scraper.
  - **`Dockerfile`**: Docker configuration for running the scraper.
  - **`requirements.txt`**: Python dependencies for the scraper.

- **`db/`**: Contains the SQLite database where scraped data is stored.
  - **`db.sqlite3`**: SQLite database file.

- **`tests/`**: Contains unit and integration tests for the project.
  - **`test_scraper.py`**: Tests for the scraper module.
  - **`test_database.py`**: Tests for database interactions.
  - **`test_dag.py`**: Tests for the Airflow DAG.

- **`config/`**: Configuration files for different environments.
  - **`dev_config.py`**: Development environment configuration.
  - **`qa_config.py`**: QA environment configuration.
  - **`prod_config.py`**: Production environment configuration.

- **`docker-compose.yml`**: Docker Compose file for setting up the development environment.

- **`.gitignore`**: Git ignore file to exclude unnecessary files from version control.

- **`requirements.txt`**: Global project dependencies.

- **`.env`**: Environment variables for the project.

- **`README.md`**: Documentation for the project.
