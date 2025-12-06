import csv

# Convertir CSV a TSV
ruta_csv = '/Users/fermin/Desktop/M_SC_BIGDATA/Unidad_1/src/data/subvenciones.csv'
ruta_tsv = '/Users/fermin/Desktop/M_SC_BIGDATA/Unidad_1/src/data/subvenciones.tsv'

with open(ruta_csv, encoding='latin1') as fich_lect, \
     open(ruta_tsv, 'w', encoding='latin1', newline='') as fich_escr:
    
    dict_lector = csv.DictReader(fich_lect)
    escritor = csv.DictWriter(fich_escr, delimiter='\t', fieldnames=dict_lector.fieldnames)
    escritor.writeheader()
    
    for linea in dict_lector:
        escritor.writerow(linea)

print(f"Archivo TSV creado: {ruta_tsv}")

# Leer TSV y sumar importes
with open(ruta_tsv, encoding='latin1') as fich:
    dict_lector = csv.DictReader(fich, delimiter='\t')
    asocs = {}
    
    for linea in dict_lector:
        centro = linea.get('Asociación', linea.get('Asociacion', ''))
        importe_str = linea.get('Importe', '0')
        
        try:
            subvencion = float(importe_str.replace(',', '.'))
        except ValueError:
            subvencion = 0
            
        if centro:
            asocs[centro] = asocs.get(centro, 0) + subvencion
    
    print("\nSuma desde TSV:")
    for asociacion, total in asocs.items():
        print(f"{asociacion}: {total:.2f}€")
