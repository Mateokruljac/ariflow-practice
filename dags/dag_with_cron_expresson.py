from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner' : 'mateo',
    'retries' : 5,
    'retry_delay' : timedelta(minutes=5)
}

with DAG(
    dag_id='cron_expression_airflow',
    schedule_interval='0 0 * * *', # daily == '0 0 * * *'
    start_date=datetime(2023,1,1,),
    default_args=default_args,
    description='First dag with cron expression'
) as dag:

    task1 = BashOperator(
        task_id='bash_cron_expression_task_1',
        bash_command="echo dag with cron expression task 1"
    )

