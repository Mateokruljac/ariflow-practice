from airflow import DAG
from datetime import datetime,timedelta

from airflow.operators.bash import BashOperator
default_args = {
    'owner' : 'mateo',
    'retries' : 5,
    'retry_delay' : timedelta(minutes=2)
}

with DAG(dag_id='our_first_catch_backfill_dag_v2',
         default_args=default_args,
         description='Tour_first_catch_backfill_dag',
         start_date=datetime(2021,7,29,2),
         schedule='@daily',
         # catchup=True -> pogledati
        catchup=False
         ) as dag:

    task1 = BashOperator(
        task_id= 'first_task_cb',
        bash_command="echo This is a simple bash command"
    )
