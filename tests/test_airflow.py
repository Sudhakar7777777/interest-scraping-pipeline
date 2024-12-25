from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.dummy_operator import DummyOperator

def test_airflow_dag():
    dag = DAG('test_dag', start_date=days_ago(1))
    task = DummyOperator(task_id='dummy_task', dag=dag)
    assert task.dag == dag, "DAG association is incorrect"
