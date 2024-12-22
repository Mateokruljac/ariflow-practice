from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

default_args = {
    'owner' : 'mateo',
    'retries' : 5,
    'retry_delay': timedelta(minutes=5)
}

def greet(ti) -> str: # ti -> Task instance
    # name = ti.xcom_pull(task_ids='get_name') # In this way we share data between tasks
    first_name = ti.xcom_pull(task_ids='get_name',key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name',key='last_name')
    age = ti.xcom_pull(task_ids='get_age',key='age')
    return f'Hello {first_name} {last_name}. You are {age} years old. :) '

def get_name(ti) -> None:
    ti.xcom_push(key='first_name',value='Mateo')
    ti.xcom_push(key='last_name',value='Kruljac')

def get_age(ti) -> None:
    ti.xcom_push(key='age',value=21)

with DAG(
    dag_id='python_operator_dag_v11',
    description='First dag using python operator',
    default_args=default_args,
    start_date=datetime(2021,10,6),
    schedule='@daily',
    schedule_interval=None # Only manual trigger -> check why it's started more than once
    # catchup - no more instances
) as dag:

    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        # op_kwargs= {'name':'Josip'}
    )

    task2 = PythonOperator(
        task_id = 'get_name',
        python_callable=get_name
    )

    task3 = PythonOperator(
        task_id = 'get_age',
        python_callable=get_age
    )

    [task2,task3] >> task1