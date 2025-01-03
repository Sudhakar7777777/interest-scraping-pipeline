import os

AIRFLOW_HOME = os.getenv('AIRFLOW_HOME', '/usr/local/airflow')
AIRFLOW_DAGS_FOLDER = os.getenv('AIRFLOW_DAGS_FOLDER', '/usr/local/airflow/dags')

# You can add other configurations specific to Airflow, such as database URLs, DAG retries, etc.
# Example: Database connection string if using external DB instead of SQLite
DATABASE_URL = 'sqlite:///db.sqlite3'