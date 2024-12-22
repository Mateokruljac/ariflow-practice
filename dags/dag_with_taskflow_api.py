from airflow.decorators import dag, task
from datetime import datetime,timedelta

default_args = {
    'owner' : 'mateo',
    'retries' : 5,
    'retry_delay' : timedelta(minutes=5)
}

@dag(
    dag_id = 'dag_with_taskflow_api',
    description= 'First dag with taskflow api',
    start_date=datetime(2024,1,1),
    default_args=default_args,
    schedule_interval='@daily'
)
def hello_world():
    @task
    def get_name() -> str:
        return 'Jerry'

    @task
    def get_age() -> int:
        return 19

    @task()
    def greet(name,age) -> None:
        print(f'My name is {name}. I am {age} years old.')

    name = get_name()
    age = get_age()
    greet(name,age)

greet_dag = hello_world()

