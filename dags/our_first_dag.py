from airflow import DAG
from datetime import datetime,timedelta

from airflow.operators.bash import BashOperator

default_args = {
    'owner' : 'mateo',
    'retries' : 5,
    'retry_delay' : timedelta(minutes=2)
}

with DAG(
        dag_id='our_first_dag_v10',
         default_args=default_args,
         description='This is our first dag that we write',
         start_date=datetime(2021,7,29,2),
         schedule='@daily') as dag:

    task1 = BashOperator(
        task_id= 'first_task',
        bash_command="echo hello world, this is the first task"
    )

    task2 = BashOperator(
        task_id = 'second_task',
        bash_command= "echo I am the second task and i will me executed after first task"
    )

    task3 = BashOperator(
        task_id='third_task',
        bash_command="echo I am the third task and I will be executed at the same time as the second task."
    )


    # Task dependency method 1
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)


    # Task dependency metthod 2 - same like method 1
    # task1 >> task2
    # task1 >> task3

    # Task dependecy method 3 -> same like method 1 and 2
    task1 >> [task2,task3]

with DAG(
        dag_id='our_first_dag_after_update',
         default_args=default_args,
         description='This is our first dag that we write',
         start_date=datetime(2021,7,29,2),
         schedule='@daily') as dag2:  pass
