
***

# **Unidad 3
** Procesamiento por lotes - *Pipeline local*

## Escenario

Para el 3er. sprint, debes crear un pipeline orquestado que permita que todas las etapas se ejecuten de manera gestionada. El pipeline debe ejecutarse diariamente y poner los datos disponibles a las 08:00 AM. Debe extraer datos en la capa bronze (zona cruda) llamada *driven_raw*, aplicar las transformaciones necesarias en la capa silver (zona de staging) llamada *driven_staging*, y cargar los datos en la capa golden (zona confiable) llamada *driven_trusted* para su consumo en el proceso analítico. Se requiere que la capa golden contenga cuatro tablas: una tabla financiera para cálculos de pagos, una tabla técnica para el análisis de incidencias técnicas, una tabla sin PII para usuarios con acceso limitado en toda la organización, y una tabla PII para usuarios con altos niveles de acceso.

## Asignación

Para este Sprint de la unidad tus tareas incluyen:

1. **Lee** los siguientes temas en la sección de [Teoría](#teoría):\

a. Docker:
* i. Docker.
* ii. Docker compose.
* iii. Docker Desktop.
* iv. Docker Hub.

b. Airflow:
* i. Airflow.
* ii. DAGs de Airflow.
* iii. Operadores de Airflow.

c. dbt.

2. **Implementa** los pasos de la sección de [Práctica](#práctica) para la empresa *BookstoneDriven*:\

a. Configura el contenedor Docker:
* i. Ejecuta Docker Desktop.
* ii. Obtén el archivo Docker Compose.
* iii. Actualiza el archivo Docker Compose.
* iv. Añade requisitos.
* v. Crea Dockerfile.

b. Crea dbt:
* i. Crea el proyecto.
* ii. Crea perfiles.
* iii. Crea fuentes.
* iv. Crea modelos.

c. Crea Airflow:
* i. Ejecuta los contenedores.
* ii. Inicia sesión.
* iii. Configura la conexión.
* iv. Crea el DAG.
* v. Ejecuta el DAG.

d. Configura la base de datos pgAdmin 4:
* i. Conéctate a la base de datos.
* ii. Revisa los datos en la base de datos.

3. **Completa** las tareas para la empresa *BookstoneData*:

* Revisa la sección de *Escenario*, completa las etapas de la *Asignación* y documenta tu trabajo en `work/scenario_1.md`. Guarda toda la evidencia de tu trabajo en el directorio `work`.

## Teoría

Los conceptos teóricos principales de la unidad junto con recursos para autoaprendizaje.

### Docker

#### Descripción

Docker es una plataforma de software que te permite construir, probar y desplegar aplicaciones rápidamente. Docker empaqueta el software en unidades estandarizadas llamadas contenedores que incluyen todo lo necesario para que la aplicación funcione: bibliotecas, herramientas del sistema, el código y el entorno de ejecución. Con Docker puedes desplegar y escalar aplicaciones en cualquier entorno y asegúrate de que tu código se ejecutará correctamente.

#### Referencias

- [Docker Curriculum - Tutorial de Docker para principiantes](https://docker-curriculum.com/)
- [IBM - ¿Qué es Docker?](https://www.ibm.com/topics/docker)
- [AWS - ¿Qué es Docker?](https://aws.amazon.com/docker/)


### Docker compose

#### Descripción

Docker Compose es una herramienta para ejecutar aplicaciones con múltiples contenedores en Docker usando el formato de archivo Compose. Un archivo Compose sirve para definir cómo se configuran uno o varios contenedores que forman tu aplicación. Una vez que tienes el archivo Compose, puedes crear e iniciar tu aplicación con un solo comando: `docker compose up`.

#### Referencias

- [Docker docs - Descripción general de Docker Compose](https://docs.docker.com/compose/)
- [GitHub - Docker compose](https://github.com/docker/compose)
- [TutorialsPoint - Docker - Compose](https://www.tutorialspoint.com/docker/docker_compose.htm)


### Docker Desktop

#### Descripción

Docker Desktop es una aplicación de instalación con un solo clic para Mac, Linux o Windows que te permite construir, compartir y ejecutar aplicaciones y microservicios en contenedores. Proporciona una interfaz gráfica sencilla para gestionar tus contenedores, aplicaciones e imágenes desde tu equipo. Docker Desktop simplifica la configuración, gestiona los mapeos de puertos, el sistema de archivos y otros parámetros predeterminados, y se actualiza regularmente con correcciones y parches de seguridad.

#### Referencias

- [Docker docs - Descripción general de Docker Desktop](https://docs.docker.com/desktop/)
- [Docker docs - Instalar Docker Desktop](https://docs.docker.com/desktop/install/windows-install/)


### Docker Hub

#### Descripción

Docker Hub es un registro de contenedores para que desarrolladores y colaboradores open source encuentren, usen y compartan imágenes de contenedores. Con Hub, los desarrolladores pueden alojar repositorios públicos gratuitos o repositorios privados para equipos y empresas.

#### Referencias

- [Docker docs - Descripción general de Docker Hub](https://docs.docker.com/docker-hub/)
- [Docker Hub](https://hub.docker.com/)


### Airflow

#### Descripción

Apache Airflow (o simplemente Airflow) es una plataforma para crear, programar y monitorear flujos de trabajo de forma programática. Al definir los flujos como código, se vuelven más mantenibles, testeables y colaborativos. Airflow permite crear flujos como grafos acíclicos dirigidos (DAGs) de tareas. El planificador de Airflow ejecuta tus tareas siguiendo las dependencias especificadas y dispone de utilidades avanzadas de línea de comandos y una interfaz gráfica para supervisar y depurar.

#### Referencias

- [Apache Airflow](https://airflow.apache.org/)
- [GitHub - Apache Airflow](https://github.com/apache/airflow)
- [Run AI - Apache Airflow Casos de uso, arquitectura y buenas prácticas](https://www.run.ai/guides/machine-learning-operations/apache-airflow#:~:text=Apache%20Airflow%20is%20an%20open,be%20easily%20scheduled%20and%20monitored.)


### DAG de Airflow

#### Descripción

En Airflow, un DAG (grafo acíclico dirigido) es la colección de todas las tareas que quieres ejecutar, organizadas de un modo que refleja sus relaciones y dependencias. Un DAG se define en un script de Python que representa la estructura de las tareas y sus dependencias como código.

#### Referencias

- [Apache Airflow - DAGs](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html)
- [Medium - Crear un DAG en Apache Airflow para principiantes: Guía completa](https://medium.com/apache-airflow/creating-a-dag-in-apache-airflow-for-beginners-a-comprehensive-guide-30a61cf61bea)
- [Medium - Evitando errores en código de DAG de nivel superior](https://medium.com/apache-airflow/avoiding-the-pitfalls-of-top-level-dag-code-fa480d9e75c6)


### Operadores de Airflow

#### Descripción

Los operadores son los bloques fundamentales de los DAGs de Airflow y contienen la lógica de cómo se procesan los datos en el pipeline. Cada tarea de un DAG se define instanciando un operador. Hay muchos tipos de operadores en Airflow, desde funciones de Python que ejecutan código arbitrario hasta operadores específicos para transferir datos entre sistemas.

#### Referencias

- [Apache Airflow - Operadores](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/operators.html)
- [Astronomer - Operadores de Airflow](https://www.astronomer.io/docs/learn/what-is-an-operator)


### dbt

#### Descripción

dbt (data build tool) permite que actividades de ingeniería de datos sean accesibles para personas con habilidades de analista de datos, transformando los datos en el almacén mediante sencillas sentencias SELECT, permitiendo crear el proceso completo de transformaciones utilizando código.

#### Referencias

- [dbt](https://www.getdbt.com/)
- [Analytics8 - dbt (Descripción general y aplicaciones)](https://www.analytics8.com/blog/dbt-overview-what-is-dbt-and-what-can-it-do-for-my-data-pipeline/#:~:text=dbt%20(data%20build%20tool)%20makes,entire%20transformation%20process%20with%20code.)
- [Medium - El poder de dbt](https://medium.com/@nydas/the-power-of-data-build-tool-dbt-6b26dfab5bac)


## Práctica

Implementación para la parte práctica de la unidad.

### Configura el contenedor Docker

El ETL se desarrolló en la máquina local llamada *entorno de pruebas*. Tras prototipar localmente el ETL, valida con los involucrados que los resultados coincidan con lo esperado. Los procesos del entorno de pruebas se trasladarán al *entorno de desarrollo*, también en local, usando herramientas de automatización, orquestación y gestión para operar todos los procesos como una sola unidad: el **pipeline**.

Primero, asegúrate de tener instaladas todas las herramientas necesarias desde la unidad_2 en tu máquina local.

#### Ejecuta Docker Desktop

Ejecuta Docker Desktop.
En Docker Desktop deberías poder ver las opciones de Contenedores, Imágenes y Volúmenes. Todas deberían estar vacías ya que no se ha ejecutado nada aún.
![Image 3.1](/Assets/image_3.1.PNG)

Como se necesitan varios contenedores para toda la infraestructura, instala [Docker Compose](https://docs.docker.com/compose/install/).
Abre la terminal y navega al directorio del proyecto sustituyendo `<tu_ruta>` por tu ubicación y ábrelo en VS Code.

```
cd C:\<tu_ruta>\M_SC_BIGDATA\Unidad_3\work
code .
```


#### Obtén el archivo Docker Compose

Obtén el archivo `docker-compose.yml` o [cópialo](https://airflow.apache.org/docs/apache-airflow/2.10.2/docker-compose.yaml) en un fichero con el mismo nombre.

```
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.10.2/docker-compose.yaml'
```

Ahora puedes ejecutar Apache Airflow básico en tu máquina local.
**Nota:** Si la versión actual no es compatible, consulta las [Notas de la release de Airflow](https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html) para la versión más reciente.

#### Actualiza el archivo Docker Compose

Para este trabajo, necesitas actualizar `docker-compose.yml` y crear una imagen personalizada usando el archivo modificado como plantilla.

La imagen existente está comentada (línea 52) pues no se usará la imagen por defecto. Se irá generando la imagen personalizada (línea 53).
Para obtener un entorno Airflow vacío, cambia `AIRFLOW__CORE__LOAD_EXAMPLES` a `false` (línea 62).
Agrega el directorio `dbt` para el proyecto dbt (línea 80) y el directorio `data` (línea 81) para los datos generados dentro del contenedor.
![Image 3.2](/Assets/image_3.2.PNG)

>Se puede crear otra base de datos distinta a la usada por Airflow, pero se empleará la misma base de datos, pero diferentes esquemas.
Agrega el puerto `5433:5432` para exponer la base de datos (líneas 97-98). Haz visible el directorio `data` para la base de datos (línea 101).
![Image 3.3](/Assets/image_3.3.PNG)

Agrega los directorios `dbt` y `data` para que se creen y puedan leerse en el contenedor (líneas 242-243).
![Image 3.4](/Assets/image_3.4.PNG)

Ya tienes tu archivo `docker-compose.yml` personalizado según las necesidades del proyecto.

#### Añade requisitos

Crea un archivo `requirements.txt` y copia lo siguiente:

``` bash
dbt-core==1.8.0
dbt-postgres==1.8.2
faker==18.4.0
polars==1.8.1
```


#### Crea Dockerfile

Como necesitas una imagen personalizada, crea un `Dockerfile` y pega el contenido siguiente.
Usa la imagen oficial de Airflow como base y la personaliza. Usando el usuario `airflow`, copia el archivo de requerimientos y ejecuta la instalación de dependencias. Copia el contenido del directorio `dbt` al contenedor.

```bash
# Usa la imagen oficial de Airflow como plantilla.
FROM apache/airflow:2.10.2

# Cambia a usuario airflow para instalar paquetes.
USER airflow

# Copia el archivo de requerimientos al contenedor.
COPY requirements.txt .

# Instala todas las dependencias del archivo.
RUN pip install -r requirements.txt

# Copia el directorio dbt al contenedor.
COPY dbt /opt/airflow/dbt
```


### Crea dbt

Las consultas SQL creadas para el *entorno de pruebas* pueden usarse en *desarrollo*, pero conforme el proyecto crezca, será difícil gestionar todos los procesos únicamente en la base de datos. Para una infraestructura escalable de modelado de datos se usará **dbt**.
Crea un directorio `dbt` y dentro otro llamado `models`.

```bash
mkdir dbt
cd dbt
mkdir models
cd ../
```


#### Crea proyecto

En `dbt`, crea el archivo `dbt_project.yml` y agrega:

```bash
name: 'dbt_driven_data'
version: '1.0'
profile: 'default'
model-paths: ["models"]
```


#### Crea perfiles

En `dbt`, crea el archivo `profiles.yml` y pega:

```bash
default:
  target: dev
  outputs:
    dev:
      type: postgres
      host: postgres
      user: airflow
      password: airflow
      dbname: airflow
      schema: driven
      port: 5432
```


#### Crea fuentes

En `dbt/models` crea el archivo `source.yml` con:

```bash
version: 2

sources:
  - name: raw_source
    database: airflow
    schema: driven_raw
    tables:
      - name: raw_batch_data

  - name: staging_source
    database: airflow
    schema: driven_staging
    tables:
      - name: dim_address
      - name: dim_date
      - name: dim_finance
      - name: dim_person
      - name: fact_network_usage

  - name: trusted_source
    database: airflow
    schema: driven_trusted
    tables:
      - name: payment_data
      - name: technical_data
      - name: non_pii_data
      - name: pii_data
```


#### Crea modelos

Crea los modelos SQL (`staging_dim_address.sql`, `staging_dim_date.sql`, etc.) y usa el contenido traducido conforme necesites en tu proyecto. Conserva las directivas dbt (`{{ config(...) }}`) y ajusta solo los comentarios según la traducción.

>(Nota: No se traduce el SQL porque los nombres de columnas y scripts deben mantenerse igual para ejecución técnica, pero los comentarios y explicaciones sí).

### Crea Airflow

Cuando todo lo anterior esté listo, el proyecto estará igual que el *entorno de pruebas*, donde cada parte puede ejecutarse manualmente. Para pasarlo al *entorno de desarrollo*, usa Apache Airflow para orquestar y administrar el pipeline. En Airflow el pipeline se define como un DAG, que ejecuta tareas dependientes entre sí mostrando el éxito solo si todas las tareas se completan correctamente.

#### Ejecuta los contenedores

Con Docker Desktop en ejecución y en la carpeta correcta (`Unidad_3/work`):

```bash
cd work
docker-compose up --build
```
![Image 3.5](/Assets/image_3.5.PNG)
Debes ver la ejecución de todos los pasos y al final el mensaje *booting worker with pid*.
![Image 3.6](/Assets/image_3.6.PNG)
Ahora en Docker Desktop debes ver siete contenedores bajo el nombre `Unidad_3`, siete imágenes y el volumen adjunto a la base de datos.
![Image 3.7](/Assets/image_3.7.PNG)
![Image 3.8](/Assets/image_3.8.PNG)
![Image 3.9](/Assets/image_3.9.PNG)
>**Nota:** Para reconstruir la infraestructura, puedes borrar solo los contenedores y dejar el volumen con los datos guardados, o borrar contenedores y volumen.

- Para borrar contenedores:

```bash
docker-compose down
```

- Para borrar también volúmenes:

```bash
docker-compose down -v
```

![Image 3.10](/Assets/image_3.10.PNG)
#### Inicia sesión

Accede a Airflow local en tu navegador: `localhost:8080`.
Usuario: `airflow`   Contraseña: `airflow`.
![Image 3.11](/Assets/image_3.11.PNG)
Después verás la interfaz de Airflow con los DAGs y el menú `Admin` > `Connections`.
![Image 3.12](/Assets/image_3.12.PNG)

#### Configura la conexión

Ve a `Admin` > `Connection` y crea una nueva conexión rellenando los campos según lo necesites.
![Image 3.13](/Assets/image_3.13.PNG)

#### Crea el DAG

Crea el archivo `driven_data_pipeline.py` en `work_3/dags` y define los argumentos y el DAG:

```python
# Argumentos por defecto
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 0,
}

# Definición del DAG
dag = DAG(
    'extract_raw_data_pipeline',
    default_args=default_args,
    description='Pipeline principal de DataDriven.',
    schedule_interval="* 7 * * *",
    start_date=datetime(2024, 9, 22),
    catchup=False,
)
```

Configura las tareas usando PythonOperator, SQLExecuteQueryOperator y BashOperator.

Define dependencias entre tareas:

```python
[extract_raw_data_task, create_raw_schema_task] >> create_raw_table_task
create_raw_table_task >> load_raw_data_task >> run_dbt_staging_task
run_dbt_staging_task >> run_dbt_trusted_task
```
![Image 3.14](/Assets/image_3.14.PNG)
Una vez guardado y desplegado el archivo, el DAG aparecerá en el entorno de Airflow, y podrás ver el grafo y los logs de ejecución.
![Image 3.15](/Assets/image_3.15.PNG)
#### Ejecuta el DAG

Ejecuta el DAG manualmente o espera la hora programada (07:00 AM). Puedes consultar los logs y la ejecución de los modelos dbt por tags, además de ver el tiempo de ejecución de cada tarea.
![Image 3.16](/Assets/image_3.16.PNG)
![Image 3.17](/Assets/image_3.17.PNG)
![Image 3.18](/Assets/image_3.18.PNG)
![Image 3.19](/Assets/image_3.19.PNG)
### Configura base de datos pgAdmin 4

Con el pipeline funcionando diariamente, los datos están disponibles para su consumo.

Conecta a la base de datos `airflow` en pgAdmin 4.
Crea un servidor y una base de datos con el nombre y parámetros mostrados.
![Image 3.20](/Assets/image_3.20.PNG)

#### Revisa los datos en la base de datos

En la base de datos navega a `Schemas`, verás los esquemas creados: `driven_raw`, `driven_staging`, y `driven_trusted`, y sus tablas correspondientes.
![Image 3.21](/Assets/image_3.21.PNG)

Utiliza las consultas del Unidad_2 modificando solo el nombre del esquema para explotar los datos en la empresa.
![Image 3.22](/Assets/image_3.22.PNG)

Como el pipeline Airflow corre diariamente a las 07:00 AM según la programación, los datos frescos están disponibles antes de las 08:00 AM todos los días.

***
<p align="right">
  <a href="/Unidad_4/work/1_asignacion.md">
    <img src="/assets/arrow.png" width="75" height="75" alt="Índice">
  </a>
</p>
