from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="sales_data_pipeline",
    start_date=datetime(2024,1,1),
    schedule_interval="@daily"
) as dag:

    ingest = BashOperator(
        task_id="ingest_api_data",
        bash_command="python ingestion/api_ingestion.py"
    )

    transform = BashOperator(
        task_id="run_dbt_models",
        bash_command="dbt run"
    )

    ingest >> transform
