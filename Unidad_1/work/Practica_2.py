import csv

ruta_original = '/Users/fermin/Desktop/M_SC_BIGDATA/Unidad_1/src/data/subvenciones.csv'
ruta_nuevo = '/Users/fermin/Desktop/M_SC_BIGDATA/Unidad_1/src/data/subvenciones_esc.csv'

with open(ruta_original, encoding='latin1') as fich_lect, \
     open(ruta_nuevo, 'w', encoding='latin1', newline='') as fich_escr:
    
    dict_lector = csv.DictReader(fich_lect)
    
    # Verificar nombres de columnas
    print("Columnas originales:", dict_lector.fieldnames)
    
    campos = dict_lector.fieldnames + ['Justificación requerida', 'Justificación recibida']
    escritor = csv.DictWriter(fich_escr, fieldnames=campos)
    escritor.writeheader()
    
    for linea in dict_lector:
        importe_str = linea.get('Importe', '0')
        try:
            importe = float(importe_str.replace(',', '.'))
        except ValueError:
            importe = 0
            
        linea['Justificación requerida'] = "Sí" if importe > 300 else "No"
        linea['Justificación recibida'] = "No"
        escritor.writerow(linea)

print(f"Archivo modificado creado: {ruta_nuevo}")
