from airflow.models import DagBag

def test_dag_import():
    dagbag = DagBag(dag_folder="airflow/dags")
    assert dagbag.dags is not None
    assert 'scrape_fcnr_interest_rates' in dagbag.dags
    dag = dagbag.dags['scrape_fcnr_interest_rates']
    assert len(dag.tasks) == 2
