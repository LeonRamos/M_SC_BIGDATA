import csv
import os

# Ruta al archivo CSV
ruta_csv = '/Users/fermin/Desktop/M_SC_BIGDATA/Unidad_1/src/data/subvenciones.csv'

# Verificar que el archivo existe
if not os.path.exists(ruta_csv):
    print(f"Error: El archivo {ruta_csv} no existe")
else:
    # Leer y sumar importes
    with open(ruta_csv, encoding='latin1') as fichero_csv:
        dict_lector = csv.DictReader(fichero_csv)
        asocs = {}
        
        # Mostrar las columnas disponibles para verificar los nombres
        print("Columnas disponibles:", dict_lector.fieldnames)
        
        for linea in dict_lector:
            # Verificar que las claves existen
            centro = linea.get('Asociación', linea.get('Asociacion', ''))
            importe_str = linea.get('Importe', '0')
            
            # Limpiar y convertir el importe
            try:
                subvencion = float(importe_str.replace(',', '.'))
            except ValueError:
                print(f"Error convirtiendo importe: {importe_str}")
                subvencion = 0
                
            if centro:
                asocs[centro] = asocs.get(centro, 0) + subvencion
        
        print("\nSuma de importes por asociación:")
        for asociacion, total in asocs.items():
            print(f"{asociacion}: {total:.2f}€")
