from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

default_args = {
    'owner' : 'Mateo',
    'retries' : 5,
    'retry_delay' : timedelta(minutes=5)
}

with DAG(
    dag_id='sql_operator_dag_v5',
    description='DAG with SQL operator',
    schedule_interval='@hourly',
    start_date=datetime(2024,1,1),
    default_args=default_args
) as dag:

    # task1 = SQLExecuteQueryOperator(
    #     task_id='SQL_provider_task',
    #     conn_id= 'sql_operator_practice',
    #     sql="""
    #     create table if not exists dag_runs_v2(
    #         dt date,
    #         dag_id varchar,
    #         primary key (dt,dag_id)
    #     )
    #     """
    # )

    task2 = SQLExecuteQueryOperator(
        task_id='SQL_insert_sql_operator_practice',
        conn_id='sql_operator_practice',
        sql="""
        insert into dag_runs_v2(dt,dag_id) values ('{{ ds }}','{{ dag.dag_id }}');
        """
    )

    # task3 = SQLExecuteQueryOperator(
    #     task_id='SQL_delete_dag_if_exists',
    #     conn_id='sql_operator_practice',
    #     sql="""
    #         delete from dag_runs_v2 where dt='{{ ds }}' and dag_id = '{{ dag.dag_id }}';
    #     """
    # )



