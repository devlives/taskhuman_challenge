"""Simple DAG that uses a few python operators."""
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator

import example as e

from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2018, 4, 1),
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# DAG Object
dag = DAG(
    'sample_dag',
    default_args=default_args,
    schedule_interval=timedelta(minutes=5),
    catchup=False,
)

print_hello_world = PythonOperator(
    task_id='hello_world',
    python_callable=e.HelloWorld(),
    dag=dag
)

end = DummyOperator(
    task_id='final_task',
    dag=dag
)

end << print_hello_world
