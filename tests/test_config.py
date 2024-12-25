import configparser
from config import airflow_config, scraper_config

def test_airflow_config():
    assert airflow_config.AIRFLOW_HOME is not None, "AIRFLOW_HOME is not set"
    assert airflow_config.AIRFLOW_DAGS_FOLDER is not None, "AIRFLOW_DAGS_FOLDER is not set"

def test_scraper_config():
    assert scraper_config.SCRAPER_URL is not None, "SCRAPER_URL is not set"
    assert scraper_config.REQUEST_TIMEOUT > 0, "REQUEST_TIMEOUT should be greater than 0"
