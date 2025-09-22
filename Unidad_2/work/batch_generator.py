import os
import random
import csv
import logging
import uuid
import polars as pl
from pathlib import Path

from faker import Faker
from datetime import date, datetime, timedelta

# Configura logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[logging.StreamHandler()]
)

def create_directories_if_not_exist(file_path: str) -> None:
    """
    Crea los directorios necesarios si no existen.
    Args:
        file_path (str): Ruta del archivo donde se crearán los directorios padres.
    """
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
        logging.info(f"Created directory: {directory}")

def create_data(locale: str) -> Faker:
    """
    Crea una instancia de Faker para generar datos falsos localizados.
    Args:
        locale (str): Código de la región/idioma de los datos falsos.
    Returns:
        Faker: Instancia de Faker configurada con dicho locale.
    """
    # Loguea la acción.
    logging.info(f"Created synthetic data for {locale.split('_')[-1]} country code.")
    return Faker(locale)

def generate_record(fake: Faker) -> list:
    """
    Genera un único registro de usuario falso.
    Args:
        fake (Faker): Instancia de Faker para datos aleatorios.
    Returns:
        list: Lista con diversos detalles simulados del usuario.
    """
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

def write_to_csv(file_path: str, rows: int) -> None:
    """
    Genera múltiples registros falsos y los escribe en un CSV.
    Args:
        file_path (str): Ruta donde se guardará el CSV.
        rows (int): Total de registros sintéticos a generar.
    """
    # Crear directorios si no existen
    create_directories_if_not_exist(file_path)
    
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

def add_id(file_name: str) -> None:
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

def update_datetime(file_name: str, run: str) -> None:
    """
    Actualiza la columna 'accessed_at' en el CSV con el timestamp correspondiente.
    Args:
        file_name (str): Ruta al archivo CSV a actualizar.
        run (str): Indica el tipo de timestamp a usar.
    """
    if run == "next":
        current_time = datetime.now().replace(microsecond=0)
        yesterday_time = current_time - timedelta(days=1)
        df = pl.read_csv(file_name)
        df = df.with_columns(pl.lit(yesterday_time).alias("accessed_at"))
        df.write_csv(file_name)
        logging.info("Updated accessed timestamp.")
    else:
        logging.info("No timestamp update needed for first run.")

if __name__ == "__main__":
    logging.info(f"Started batch processing for {date.today()}.")
    
    output_file = f"data/batch_{date.today()}.csv"
    
    # Crear directorios si no existen
    create_directories_if_not_exist(output_file)
    
    if str(date.today()) == "2025-09-22":
        records = random.randint(300_372, 300_372)
        run_type = "first"
    else:
        records = random.randint(0, 1_101)
        run_type = "next"
    
    write_to_csv(output_file, records)
    
    add_id(output_file)
    
    update_datetime(output_file, run_type)
    
    logging.info(f"Finished batch processing {date.today()}.")
