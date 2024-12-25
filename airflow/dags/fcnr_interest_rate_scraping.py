import logging
from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from scraper.scraper import scrape_interest_rates_optimized
from scraper.utils import store_data_in_sqlite
from airflow.exceptions import AirflowException
import os

# Set logging configuration
logging.basicConfig(level=logging.DEBUG)

def scrape_interest_rates_task(**kwargs):
    """Task to scrape the interest rates"""
    try:
        logging.debug("Starting the scrape task")
        data = scrape_interest_rates_optimized()
        logging.debug(f"Scraped data: {data}")
        return data
    except Exception as e:
        logging.error(f"Error scraping interest rates: {e}")
        raise AirflowException(f"Scrape failed: {str(e)}")

def store_data_task(**kwargs):
    """Task to store scraped data in SQLite"""
    try:
        data = kwargs['ti'].xcom_pull(task_ids='scrape_interest_rates')
        store_data_in_sqlite(data)
        logging.debug("Data stored successfully in SQLite")
    except Exception as e:
        logging.error(f"Error storing data in SQLite: {e}")
        raise AirflowException(f"Store data failed: {str(e)}")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'scrape_fcnr_interest_rates',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    max_active_runs=1,
)

scrape_task = PythonOperator(
    task_id='scrape_interest_rates',
    python_callable=scrape_interest_rates_task,
    provide_context=True,
    dag=dag,
)

store_task = PythonOperator(
    task_id='store_data_in_sqlite',
    python_callable=store_data_task,
    provide_context=True,
    dag=dag,
)

scrape_task >> store_task
