from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
import logging

# --- 1. Funciones auxiliares para PythonOperator ---

def extract_raw_data_func():
    """Simula la lógica de extracción de datos brutos."""
    logging.info("Iniciando la extracción de datos brutos...")
    # En un escenario real, aquí iría la lógica para conectarse a una fuente externa 
    # (API, S3, etc.) y guardar el archivo temporalmente.
    logging.info("Datos brutos extraídos (Simulación).")

def cleanup_func():
    """Simula la limpieza de archivos temporales al finalizar."""
    logging.info("Limpiando archivos temporales...")
    # Lógica para eliminar archivos temporales o registros de la ejecución
    logging.info("Limpieza completada.")

# --- 2. Argumentos por defecto y Definición del DAG ---

# Argumentos por defecto
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 0,
    # Configuración del email, si fuera necesario: 'email_on_failure': False,
}

# Definición del DAG
dag = DAG(
    'extract_raw_data_pipeline',
    default_args=default_args,
    description='Pipeline principal de DataDriven.',
    # Ejecución a las 7:00 AM todos los días: "* 7 * * *"
    schedule_interval="0 7 * * *", 
    start_date=datetime(2024, 9, 22),
    catchup=False,
    tags=['datadriven', 'raw', 'dbt'],
)

# --- 3. Definición de Tareas y Consultas SQL ---

# 3.0. Definición de la consulta SQL para crear la tabla
create_raw_table_sql = """
CREATE TABLE IF NOT EXISTS raw.mi_tabla_raw (
    columna1 VARCHAR(50),
    columna2 INT,
    timestamp_carga TIMESTAMP DEFAULT NOW()
);
"""

# 3.0. Definición de la consulta SQL para cargar datos (simulación)
load_raw_data_sql = """
INSERT INTO raw.mi_tabla_raw (columna1, columna2) VALUES ('ejemplo', 100);
"""


with dag:
    # 3.1. Tarea de Extracción de Datos (PythonOperator)
    extract_raw_data_task = PythonOperator(
        task_id='extract_raw_data_task',
        python_callable=extract_raw_data_func,
    )

    # 3.2. Tarea de Creación del Esquema 'raw' (SQLExecuteQueryOperator)
    create_raw_schema_task = SQLExecuteQueryOperator(
        task_id="create_raw_schema_task",
        conn_id='postgres_conn', # ID de conexión correcto según tu UI
        sql="CREATE SCHEMA IF NOT EXISTS raw;"
    )

    # 3.3. Tarea de Creación de la Tabla 'raw' (SQLExecuteQueryOperator)
    create_raw_table_task = SQLExecuteQueryOperator(
        task_id="create_raw_table_task",
        conn_id='postgres_conn',
        # ✅ Usamos la variable SQL definida arriba
        sql=create_raw_table_sql 
    )
    

    # 3.4. Tarea de Carga de Datos (SQLExecuteQueryOperator)
    load_raw_data_task = SQLExecuteQueryOperator(
        task_id='load_raw_data_task',
        sql=load_raw_data_sql,
        conn_id='postgres_conn',
    )

    # 3.5. Tarea de Ejecución de dbt Staging (BashOperator)
    run_dbt_staging_task = BashOperator(
        task_id='run_dbt_staging_task',
        # 💡 CORRECCIÓN: Se añade --profiles-dir para solucionar el error de "Path does not exist".
        # Asume que profiles.yml está en la carpeta del proyecto dbt.
        bash_command='cd /opt/airflow/dags/dbt/ && dbt run --models staging.* --profiles-dir /opt/airflow/dags/dbt/', 
    )

    # 3.6. Tarea de Ejecución de dbt Trusted (BashOperator)
    run_dbt_trusted_task = BashOperator(
        task_id='run_dbt_trusted_task',
        # 💡 CORRECCIÓN: Se aplica la misma corrección aquí.
        bash_command='cd /opt/airflow/dags/dbt/ && dbt run --models trusted.* --profiles-dir /opt/airflow/dags/dbt/',
    )
    
    # 3.7. Tarea de Limpieza (PythonOperator)
    cleanup_task = PythonOperator(
        task_id='cleanup_task',
        python_callable=cleanup_func,
        trigger_rule='all_done', # Se ejecuta si las tareas anteriores fallan o tienen éxito
    )


# --- 4. Definición de Dependencias ---

# Las tareas de extracción y creación de esquema pueden correr en paralelo antes de crear la tabla
[extract_raw_data_task, create_raw_schema_task] >> create_raw_table_task

# La creación de la tabla debe terminar antes de cargar los datos, y la carga antes de dbt staging.
create_raw_table_task >> load_raw_data_task >> run_dbt_staging_task

# dbt staging debe terminar antes de dbt trusted.
run_dbt_staging_task >> run_dbt_trusted_task

# La limpieza se ejecuta al final.
run_dbt_trusted_task >> cleanup_task