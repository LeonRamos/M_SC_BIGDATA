

# **Unidad 2** 
**Procesamiento por lotes - *Desarrollo Local***

## Escenario
Para esta unidad / 2do sprint, necesitas investigar la fuente de datos de *BookstoneData*, comprender la cantidad de datos del año anterior e identificar los campos disponibles y sus tipos de datos. Prepara un pipeline ETL local para extraer los datos hacia la capa bronce (zona raw), aplicar las transformaciones necesarias hacia la capa plata (zona staging) y cargar los datos en la capa oro (zona confiable) para su consumo en el proceso analítico. Se requiere que la capa oro contenga cuatro tablas: una tabla financiera para los cálculos de pagos, una tabla técnica para analizar problemas técnicos, una tabla sin PII (non-PII) para acceso de todos los usuarios con acceso restringido en la organización, y una tabla con PII para usuarios con altos niveles de acceso.

## Actividad
Para este  2do Sprint, tus tareas incluyen:
1. **Leer** los siguientes temas en la sección [Teoría](#teoría):  
    a. Extraer Transformar Cargar (ETL).  
    b. Procesamiento por lotes.  
    c. Extracción de datos.  
    d. Normalización de datos.  
    e. Python.  
    f. SQL.  
    g. Framework.

2. **Implementar** los pasos de la sección [Práctica](#práctica) para la empresa *BookstoneDriven*:  
    a. Investigar la fuente de datos.  
    b. Extraer datos:
    * i. Generador de datos.
    * ii. Extracción de datos.

    c. Transformar datos:
    * i. Capa bronce.
    * ii. Capa plata.

    d. Cargar datos:
    * i. Datos financieros.
    * ii. Datos de soporte.
    * iii. Datos sin PII.
    * iv. Datos PII.

    f. Scrapping 
    * i. Abre el portal catastral de España.
    * ii. Selecciona la pestaña "Coordenadas".
    * iii. Introduce una latitud y longitud.
    * iv. Extrae los datos.

3. **Completar** tareas para la empresa *BookstoneData*:
    * Revisa la sección *Escenario*, completa las etapas de la *Actividad* y documenta tu trabajo en `work/scenario_2.md`. Guarda toda la evidencia en el directorio `work`.

## Teoría
Principales conceptos teóricos para la unidad junto con recursos de aprendizaje autodidacta.

### ETL
#### Descripción
ETL significa extraer, transformar y cargar. Es un proceso de integración de datos que combina, limpia y organiza datos de múltiples fuentes en un único conjunto de datos consistente para almacenarlos en un data warehouse, data lake u otro sistema de destino.
#### Referencias
[IBM - ¿Qué es ETL?](https://www.ibm.com/topics/etl)  
[GeeksforGeeks - ETL Process in Data Warehouse](https://www.geeksforgeeks.org/etl-process-in-data-warehouse/)  
[AWS - ¿Qué es ETL?](https://aws.amazon.com/what-is/etl/)

### Procesamiento por lotes
#### Descripción
El procesamiento por lotes es una técnica computacional en la que un conjunto de datos se acumula y luego se procesa en una sola operación, a menudo sin necesidad de interacción en tiempo real. Este enfoque es especialmente efectivo para manejar grandes volúmenes de datos, donde las tareas pueden ejecutarse como grupo en horas de baja demanda para optimizar recursos y rendimiento del sistema.
#### Referencias
[Splunk - An Introduction to Batch Processing](https://www.splunk.com/en_us/blog/learn/batch-processing.html)  
[AWS - ¿Qué es Batch Processing?](https://aws.amazon.com/what-is/batch-processing/)  
[Influxdata - Explicación Procesamiento por Lotes](https://www.influxdata.com/glossary/batch-processing-explained/)

### Extracción de datos
#### Descripción
La extracción de datos es el proceso de obtener datos crudos de una fuente y replicar dichos datos en otro lugar. Los datos crudos pueden provenir de varias fuentes, como bases de datos, hojas de Excel, plataformas SaaS, web scraping u otros. Pueden replicarse en un data warehouse, diseñado para soportar procesamiento analítico en línea (OLAP). Esto puede incluir datos no estructurados, datos de distintos tipos o datos mal organizados. Una vez consolidados, procesados y refinados, pueden almacenarse en un lugar central, ya sea local, en la nube o híbrido, para esperar su transformación o procesamiento futuro.
#### Referencias
[Airbyte - ¿Qué es la extracción de datos? Herramientas y técnicas](https://airbyte.com/data-engineering-resources/data-extraction)  
[Stitch - ¿Qué es la extracción de datos? Herramientas y técnicas](https://www.stitchdata.com/resources/what-is-data-extraction/)  
[Zapier - ¿Qué es la extracción de datos? Y cómo automatizarla](https://zapier.com/blog/data-extraction/?msockid=19299d3c1eef6bd012a689b41f156a45)

### Normalización de datos
#### Descripción
La normalización de datos es el proceso de estructurar la información en una base de datos para reducir la redundancia y hacerla más eficiente. Se trata de garantizar que cada campo y tabla esté lógica y eficazmente organizado para evitar anomalías al insertar, actualizar o eliminar registros. Este proceso se realiza según reglas específicas que dictan cómo deben organizarse las tablas.
#### Referencias
[Splunk - Explicación normalización de datos](https://www.splunk.com/en_us/blog/learn/data-normalization.html)  
[Database Star - Guía paso a paso de normalización](https://www.databasestar.com/database-normalization/)  
[Metabase - Normalización de datos](https://www.metabase.com/learn/grow-your-data-skills/data-fundamentals/normalization)

### Python
#### Descripción
Python es un lenguaje de programación de alto nivel y propósito general. Su filosofía de diseño enfatiza la legibilidad del código usando indentación significativa. Python es tipado dinámicamente y cuenta con recolección de basura. Soporta múltiples paradigmas de programación, incluyendo estructurado (especialmente procedural), orientado a objetos y funcional. Con frecuencia se le describe como un lenguaje "baterías incluidas" por su extensa biblioteca estándar.
#### Referencias
[Documentación de Python](https://docs.python.org/3/)  
[W3School - Tutorial Python](https://www.w3schools.com/python/)  
[Real Python Tutorials](https://realpython.com/)

### SQL
#### Descripción
SQL es un lenguaje estándar de bases de datos utilizado para acceder y manipular datos en base de datos. SQL significa Structured Query Language. Fue desarrollado por IBM en los años 70. Al ejecutar queries, SQL puede crear, actualizar, borrar y recuperar datos en bases como MySQL, Oracle, PostgreSQL, etc.
#### Referencias
[SQL Tutorial](https://www.sqltutorial.org/)  
[W3School - Introducción a SQL](https://www.w3schools.com/sql/sql_intro.asp)  
[GeeksforGeeks - SQL Tutorial](https://www.geeksforgeeks.org/sql-tutorial/)

### Framework
#### Descripción
Cuando usas un lenguaje de programación, puedes encontrar diferentes frameworks basados en ese lenguaje. Al desarrollar software, puedes utilizar algún framework para mejorar la calidad de tu aplicación. Los frameworks ofrecen muchas ventajas y reducen el tiempo y esfuerzo requeridos en el proceso de desarrollo, permitiendo escribir un código limpio y fácilmente entendible por otros.
#### Referencias
[Medium - ¿Cómo dominar un nuevo framework de data engineering?](https://medium.com/@sounder.rahul/how-you-can-master-a-new-data-engineering-framework-e3a7c31458e5)  
[Medium - Top 6 frameworks de data engineering para aprender](https://blog.insightdatascience.com/top-6-data-engineering-frameworks-to-learn-b124f9b71ba5)  
[GeeksforGeeks - ¿Qué es un Framework?](https://www.geeksforgeeks.org/what-is-a-framework/)

## Práctica
La implementación de la parte práctica de la unidad.

### Investigar la fuente de datos
Investiga los datos generados por cada inicio de sesión de usuarios en la plataforma de internet de la empresa *bookstoneDriven*, comprende la cantidad de datos existente y los nombres y tipos de columnas.  
Después de investigar, prepárate para crear el ETL local para el pipeline.  
Los datos contienen 16 columnas: person_name, user_name, email, personal_number, birth_date, address, phone, mac_address, ip_address, iban, accessed_at,
session_duration, download_speed, upload_speed, consumed_traffic, unique_id.  
El número de registros actualmente es: 300,372 registros, y se espera una tasa diaria de hasta 3,000 registros.  
En esta etapa, la empresa desea ingerir todos los datos históricos y la ingesta diaria de datos del día anterior para procesos analíticos.

### Extraer datos
Los datos pueden obtenerse mediante diferentes opciones: API, [Scrapping](/Unidad_2/src/Scrapping.md), Crawling, Generador, Manual, etc.  
Para *BookstoneDriven* se usará un generador sintético de datos que imitará una API.  
Como los datos del año anterior no ocupan mucho (~30 MB), no se requiere una aplicación intensiva en procesamiento; la API será reemplazada por un generador sintético de datos. Se usará Python, la librería [Faker](https://faker.readthedocs.io/en/master/) para generación de datos y [Polars](https://docs.pola.rs/) para manejo de datos.

#### Generador de datos
Para ingerir datos históricos necesitas crear un Framework (por ahora, sólo como script; luego crecerá en complejidad).

Crea un archivo en el directorio `work` y nómbralo `batch_generator.py`, crea un subdirectorio llamado `data`. Sustituye `<path_to_user>` con la ruta local de tu proyecto.
```cmd

cd <path_to_user>\Unidad_2\work
type nul > batch_generator.py

```

En el archivo `batch_generator.py` importa todos los paquetes y módulos necesarios. Además, define el nivel de logging y los mensajes que se almacenarán.
```python

import random
import csv
import logging
import uuid
import polars as pl

from faker import Faker
from datetime import date, datetime, timedelta

# Configura logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[logging.StreamHandler()]
)
```

Crea la función `create_data` que instancia el generador de datos con el engine de idioma provisto. Para *BookstoneDriven* se utiliza el engine para México; todos los datos sintéticos serán MXN.
```python

def create_data(locale: str) -> Faker:
```
Crea una instancia de Faker para generar datos falsos localizados.
Args:
locale (str): Código de la región/idioma de los datos falsos.
Returns:
Faker: Instancia de Faker configurada con dicho locale.

``` python
# Loguea la acción.
logging.info(f"Created synthetic data for {locale.split('_')[-1]} country code.")
return Faker(locale)
```

Crea la función `generate_record` y proporciona las funciones sintéticas para obtener todos los campos necesarios. Esta función generará un registro por llamada, conteniendo todos los campos definidos.

```python
def generate_record(fake: Faker) -> list:
```
Genera un único registro de usuario falso.
Args:
fake (Faker): Instancia de Faker para datos aleatorios.
Returns:
list: Lista con diversos detalles simulados del usuario.

```python
# Generar datos personales aleatorios.
person_name = fake.name()
user_name = person_name.replace(" ", "").lower()
email = f"{user_name}@{fake.free_email_domain()}"
personal_number = fake.ssn()
birth_date = fake.date_of_birth()
address = fake.address().replace("\n", ", ")
phone_number = fake.phone_number()
mac_address = fake.mac_address()
ip_address = fake.ipv4()
iban = fake.iban()
accessed_at = fake.date_time_between("-1y")
session_duration = random.randint(0, 36000)
download_speed = random.randint(0, 1000)
upload_speed = random.randint(0, 800)
consumed_traffic = random.randint(0, 2000000)

return [
    person_name, user_name, email, personal_number, birth_date,
    address, phone_number, mac_address, ip_address, iban, accessed_at,
    session_duration, download_speed, upload_speed, consumed_traffic
]
```

Dado el volumen de datos y columnas, los datos generados se escribirán en un archivo CSV. Para esto, crea la función `write_to_csv`. Aquí indicarás cuántos registros generar.

```python
def write_to_csv(file_path: str, rows: int) -> None:
```
Genera múltiples registros falsos y los escribe en un CSV.
Args:
file_path (str): Ruta donde se guardará el CSV.
rows (int): Total de registros sintéticos a generar.

```python
# Faker con datos para México.
fake = create_data("es_MX")
headers = [
    "person_name", "user_name", "email", "personal_number", "birth_date", "address",
    "phone", "mac_address", "ip_address", "iban", "accessed_at",
    "session_duration", "download_speed", "upload_speed", "consumed_traffic"
]
with open(file_path, mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    for _ in range(rows):
        writer.writerow(generate_record(fake))
logging.info(f"Written {rows} records to the CSV file.")
```

Cada registro debe estar identificado de forma única; para eso añade una columna `unique_id` con valores [UUID](https://medium.com/@gaspm/understanding-uuid-purpose-and-benefits-of-a-universal-unique-identifier-59110154d897). Se usará Polars para esta actividad.

```python
def add_id(file_name) -> None:
    """
    Añade un UUID único a cada fila de un archivo CSV.
    Args:
        file_name (str): Ruta al archivo CSV a procesar.
    """
    df = pl.read_csv(file_name)
    uuid_list = [str(uuid.uuid4()) for _ in range(df.height)]
    df = df.with_columns(pl.Series("unique_id", uuid_list))
    df.write_csv(file_name)
    logging.info("Added UUID to the dataset.")
```

Para el dato histórico la columna `accessed_at` debe ser datetime del año previo. Para la siguiente carga, debe tener un datetime del día previo. Para esto, crea la función `update_datetime`.

```python
def update_datetime(file_name: str, run: str) -> None:
```

Actualiza la columna 'accessed_at' en el CSV con el timestamp correspondiente.
Args:
file_name (str): Ruta al archivo CSV a actualizar.
run (str): Indica el tipo de timestamp a usar.

```python 
if run == "next":
current_time = datetime.now().replace(microsecond=0)
yesterday_time = str(current_time - timedelta(days=1))
df = pl.read_csv(file_name)
df = df.with_columns(pl.lit(yesterday_time).alias("accessed_at"))
df.write_csv(file_name)
logging.info("Updated accessed timestamp.")
```

#### Extracción de datos
En este paso, los datos fuente se extraen a la capa bronce (zona raw) tal cual están; los datos pasan a ser datos crudos.

Como `batch_generator.py` formará parte del Framework, por ahora será solo un script, pero en el futuro formará parte de un módulo. Por tanto, ejecútalo encapsulando la lógica bajo `if __name__ == "__main__":`.
Inicia el logging, define la ruta del CSV generado, la fecha para la carga inicial y siguientes. Para la carga define el número de registros (del escenario - inicial = 300,372 y siguientes = máximo 3,000), también define la hora de carga según fecha. Extrae los datos, añade el identificador único y actualiza el datetime si es necesario. Finaliza y loguea.

```python 

if __name__ == "__main__":

    logging.info(f"Started batch processing for {date.today()}.")
    
    output_file = f"Unidad_2/work/data/batch_{date.today()}.csv"
    
    if str(date.today()) == "2024-09-14":
        records = random.randint(300_372, 300_372)
        run_type = "first"
    else:
        records = random.randint(0, 1_101)
        run_type = "next"
    
    write_to_csv(f"{output_file}", records)
    
    add_id(output_file)
    
    update_datetime(output_file, run_type)
    
    logging.info(f"Finished batch processing {date.today()}.")
```

Ejemplo de logs tras la primera ejecución:
![Imagen 2.1](/Assets/image_2.1.PNG)

Ejemplo de logs de ejecuciones siguientes:
![Imagen 2.2](/Assets/image_2.2.PNG)

Tras la generación, debe existir en el directorio `data` un archivo CSV `batch_20024-09-14.csv` con las 16 columnas y 300,372 filas. Este archivo contiene la fuente de datos ingerida (como si viniera por API). Esta es la capa bronce (raw zone) y los datos están crudos.

### Transformar datos
Una vez los datos crudos están en la capa bronce, serán transformados y movidos a la capa plata.

#### Capa bronce
Abre pgAdmin 4 y crea un nuevo servidor. Click derecho sobre el ícono del servidor y elige `Register` -> `Server`.
![Imagen 2.3](/Assets/image_2.3.PNG)

En el cuadro de diálogo, en la sección *General*, introduce *BookstoneDriven* como nombre del servidor.
![Imagen 2.4](/Assets/image_2.4.PNG)

En la sección *Connection*, introduce *localhost* como *Host name*, *postgres* como *Username* y una *contraseña* para tu servidor y pulsa `Save`.
![Imagen 2.5](/Assets/image_2.5.PNG)

En el nuevo servidor, crea una base de datos: click derecho sobre el servidor *BookstoneDriven*, elige `Create` -> `Database`.
![Imagen 2.6](/Assets/image_2.6.PNG)

En el cuadro de diálogo en *General*, introduce *bookstonedriven_db* como base de datos y pulsa `Save`.
![Imagen 2.7](/Assets/image_2.7.PNG)

Ahora la base tiene un esquema *public* y sin tablas.
![Imagen 2.8](/Assets/image_2.8.PNG)

Click derecho en *Tables* y elije `Create` -> `Table`.  
En el cuadro de diálogo introduce *batch_first_load* como nombre.
![Imagen 2.9](/Assets/image_2.9.PNG)

En la sección *Columns* agrega cada columna y define el tipo de dato.
![Imagen 2.10](/Assets/image_2.10.PNG)

A continuación, los nombres de columnas y tipos de datos para pgAdmin 4.
```sql

person_name character varying (100)
user_name character varying (100)
email character varying (100)
personal_number numeric
birth_date character varying (100)
address character varying (100)
phone character varying (100)
mac_address character varying (100)
ip_address character varying (100)
iban character varying (100)
accessed_at time without time zone
session_duration integer
download_speed integer
upload_speed integer
consumed_traffic integer
unique_id character varying (100)

```
![Imagen 2.12](/Assets/image_2.12.PNG)

Ahora la tabla *batch_first_load* está creada pero vacía.
![Imagen 2.13](/Assets/image_2.13.PNG)

Para cargar los datos fuente haz click derecho y elige `Import/Export data`, selecciona el archivo CSV e indica opción `Header: On`.
![Imagen 2.14](/Assets/image_2.14.PNG)

En la sección *Columns* deben aparecer todas las columnas. Si no es así, asegúrate de haber definido bien las columnas. Al terminar pulsa `OK`.
![Imagen 2.15](/Assets/image_2.15.PNG)

Si todo está bien, aparecerá *Process completed*. Si marca *Process failed*, revisa los mensajes y corrige.
![Imagen 2.16](/Assets/image_2.16.PNG)

Abre el *Query tool* de la tabla y usa la consulta del archivo `select_all_raw_data.sql`:
```sql

SELECT
*
FROM
batch_first_load
LIMIT
10

```
![Imagen 2.17](/Assets/image_2.17.PNG)

Crea los esquemas: click derecho en *Schemas* y elige `Create` -> `Schema`, nombra como *bronze_layer*, repite para *silver_layer* y *golden_layer*. 
Crea la tabla y carga los datos fuente en cada uno para tener los datos en cada esquema correspondiente.
![Imagen 2.18](/Assets/image_2.18.PNG)

#### Capa plata
La transformación principal consiste en modelar los datos: normalizarlos, ajustar tipos de datos si es necesario y manejar nulos o duplicados.

**Valores faltantes**  
Para detectar valores nulos usa esta consulta SQL:

```sql
SELECT
    COUNT(*) AS null_values
FROM
    bronze_layer.batch_first_load
WHERE
    person_name IS NULL
    OR user_name IS NULL
    OR email IS NULL
    OR personal_number IS NULL
    OR birth_date IS NULL
    OR address IS NULL
    OR phone IS NULL
    OR mac_address IS NULL
    OR ip_address IS NULL
    OR iban IS NULL
    OR accessed_at IS NULL
    OR session_duration IS NULL
    OR download_speed IS NULL
    OR upload_speed IS NULL
    OR consumed_traffic IS NULL
    OR unique_id IS NULL
```

**Valores duplicados**  
Para detectar duplicados utiliza:
```sql
SELECT
    *,
    COUNT(*) AS duplicated_values
FROM
    bronze_layer.batch_first_load
GROUP BY (
    person_name, user_name, email, personal_number,
    birth_date, address, phone, mac_address, ip_address,
    iban, accessed_at, session_duration, download_speed,
    upload_speed, consumed_traffic, unique_id
)
HAVING COUNT(*) > 1
```

Para la normalización se usará un *Star Schema* que divide la tabla inicial en una tabla de hechos y cuatro dimensionales.  
Abre [Draw.io](https://app.diagrams.net/) y sube el archivo `star_schema.drawio` del directorio `docs` para visualizar o actualizar el diagrama.  
![Imagen 2.19](/Assets/image_2.19.PNG)

Para crear las tablas usa consultas como las siguientes en pgAdmin 4:

Para *dim_address*:
```sql
CREATE TABLE silver_layer.dim_address AS
SELECT
    unique_id,
    address,
    mac_address,
    ip_address
FROM
    bronze_layer.batch_first_load

```
Para *dim_date*:
```sql
CREATE TABLE silver_layer.dim_date AS
SELECT
    unique_id,
    accessed_at
FROM
    bronze_layer.batch_first_load
```
Para *dim_finance*:
```sql
CREATE TABLE silver_layer.dim_finance AS
SELECT
    unique_id,
    iban
FROM
    bronze_layer.batch_first_load
```
Para *dim_person*:
```sql
CREATE TABLE silver_layer.dim_person AS
SELECT
    unique_id,
    person_name,
    user_name,
    email,
    phone,
    birth_date,
    personal_number
FROM
    bronze_layer.batch_first_load


```
Para *fact_network_usage*:
```sql
CREATE TABLE silver_layer.fact_network_usage AS
SELECT
    unique_id,
    session_duration,
    download_speed,
    upload_speed,
    consumed_traffic
FROM
    bronze_layer.batch_first_load

```

### Cargar datos
Una vez los datos están en capa plata, se cargan a la capa oro. Aquí, se incluye lógica adicional: una tabla para facturación diaria, otra para soporte técnico y dos tablas denormalizadas con y sin PII para diferentes casos de uso.

#### Datos Financieros
La tabla de uso financiero tendrá todos los campos involucrados y una columna *payment_amount* calculada con la fórmula correspondiente.
![Imagen 2.20](/Assets/image_2.20.PNG)
Para crearla:
```sql
CREATE TABLE golden_layer.payment_data AS
SELECT
    fnu.unique_id,
    df.iban,
    fnu.download_speed,
    fnu.upload_speed,
    fnu.session_duration,
    fnu.consumed_traffic,
    ((fnu.download_speed + fnu.upload_speed + 1) / 2) + (fnu.consumed_traffic / (fnu.session_duration + 1)) AS payment_amount
FROM
    silver_layer.fact_network_usage fnu
JOIN
    silver_layer.dim_finance df
ON
    fnu.unique_id = df.unique_id
```
Para consultar la tabla:
```sql
SELECT
    *
FROM
    golden_layer.payment_data
LIMIT
    10
```
![Imagen 2.21](/Assets/image_2.21.PNG)

#### Datos de Soporte
La tabla para soporte tendrá unique_id, dirección, mac_address, ip_address, velocidades, duración y una columna *technical_issue* (bool). Es *true* si download_speed < 50 MB, upload_speed < 60 MB o duración < 3 min.
```sql

CREATE TABLE golden_layer.technical_data AS
SELECT
    fnu.unique_id,
    da.address,
    da.mac_address,
    da.ip_address,
    fnu.download_speed,
    fnu.upload_speed,
    ROUND(fnu.session_duration / 60.0, 1) AS min_session_duration,
    CASE
        WHEN fnu.download_speed < 50 
             OR fnu.upload_speed < 60 
             OR fnu.session_duration / 60.0 < 3 THEN true
        ELSE false
    END AS technical_issue
FROM
    silver_layer.fact_network_usage fnu
JOIN
    silver_layer.dim_address da
ON
    fnu.unique_id = da.unique_id;

```
Para consultar la tabla:
```sql
SELECT
    *
FROM
    golden_layer.technical_data
LIMIT
    10
```
![Imagen 2.22](/Assets/image_2.22.PNG)

#### Datos sin PII
La tabla para datos sin PII (denormalizada y con campos sensibles enmascarados).
```sql
CREATE TABLE golden_layer.non_pii_data AS
SELECT
    '***MASKED***' AS person_name,
    SUBSTRING(dp.user_name, 1, 5) || '*****' AS user_name,
    SUBSTRING(dp.email, 1, 5) || '*****' AS email,
    '***MASKED***' AS personal_number,
    '***MASKED***' AS birth_date,
    '***MASKED***' AS address,
    '***MASKED***' AS phone,
    SUBSTRING(da.mac_address, 1, 5) || '*****' AS mac_address,
    SUBSTRING(da.ip_address, 1, 5) || '*****' AS ip_address,
    SUBSTRING(df.iban, 1, 5) || '*****' AS iban,
    dd.accessed_at,
    fnu.session_duration,
    fnu.download_speed,
    fnu.upload_speed,
    fnu.consumed_traffic,
    fnu.unique_id
FROM
    silver_layer.fact_network_usage fnu
INNER JOIN
    silver_layer.dim_address da ON fnu.unique_id = da.unique_id
INNER JOIN
    silver_layer.dim_date dd ON da.unique_id = dd.unique_id
INNER JOIN
    silver_layer.dim_finance df ON dd.unique_id = df.unique_id
INNER JOIN
    silver_layer.dim_person dp ON df.unique_id = dp.unique_id
```
Consulta ejemplo:
```sql
SELECT
    *
FROM
    golden_layer.non_pii_data
LIMIT
    10
```
![Imagen 2.23](/Assets/image_2.23.PNG)

#### Datos con PII
La tabla PII se construye denormalizando todas las dimensiones y hecho.
```sql
CREATE TABLE golden_layer.pii_data AS
SELECT
    dp.person_name,
    dp.user_name,
    dp.email,
    dp.personal_number,
    dp.birth_date,
    da.address,
    dp.phone,
    da.mac_address,
    da.ip_address,
    df.iban,
    dd.accessed_at,
    fnu.session_duration,
    fnu.download_speed,
    fnu.upload_speed,
    fnu.consumed_traffic,
    fnu.unique_id
FROM
    silver_layer.fact_network_usage fnu
INNER JOIN
    silver_layer.dim_address da ON fnu.unique_id = da.unique_id
INNER JOIN
    silver_layer.dim_date dd ON da.unique_id = dd.unique_id
INNER JOIN
    silver_layer.dim_finance df ON dd.unique_id = df.unique_id
INNER JOIN
    silver_layer.dim_person dp ON df.unique_id = dp.unique_id
```
Consulta ejemplo:
```sql
SELECT
    *
FROM
    golden_layer.pii_data
LIMIT
    10
```
![Imagen 2.24](/Assets/image_2.24.PNG)
<p align="right">
  <a href="/Unidad_3/work/1_asignacion.md">
    <img src="/assets/arrow.png" width="75" height="75" alt="Índice">
  </a>
</p>
