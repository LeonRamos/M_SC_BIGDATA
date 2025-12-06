# Usa la imagen oficial de Airflow como plantilla.
FROM apache/airflow:2.10.2 
#-python3.12

# Cambia a usuario airflow para instalar paquetes.
USER airflow

# Copia el archivo de requerimientos al contenedor.
COPY requirements.txt .

# Instala todas las dependencias del archivo.
RUN pip install -r requirements.txt
# Instala el provider de Postgres usando la instrucción RUN

# Copia el directorio dbt al contenedor.
COPY dbt /opt/airflow/dbt