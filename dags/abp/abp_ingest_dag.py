from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def start_ingest():
    print("ABP ingest pipeline started")

with DAG(
    dag_id="abp_ingest_dag",
    start_date=datetime(2026, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    start_task = PythonOperator(
        task_id="start_ingest",
        python_callable=start_ingest,
    )
