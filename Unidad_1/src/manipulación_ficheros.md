
***

# Manipulación de ficheros en Python.
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![CSV](https://img.shields.io/badge/CSV-File-FFDD00?logo=filetype&logoColor=black)](https://en.wikipedia.org/wiki/Comma-separated_values)
[![TSV](https://img.shields.io/badge/TSV-File-FFB155?logo=filetype&logoColor=black)](https://en.wikipedia.org/wiki/Tab-separated_values)
[![pandas](https://img.shields.io/badge/Pandas-Dataframe-150458?logo=pandas)](https://pandas.pydata.org/)
[![xlrd](https://img.shields.io/badge/xlrd-Excel%20Read-3a8fff?logo=excel)](https://pypi.org/project/xlrd/)
[![xlwt](https://img.shields.io/badge/xlwt-Excel%20Write-00b050?logo=excel)](https://pypi.org/project/xlwt/)
[![JSON](https://img.shields.io/badge/JSON-Supported-2a2a2a?logo=json&logoColor=white)](https://www.json.org/json-es.html)
[![XML](https://img.shields.io/badge/XML-Data-ff6600?logo=xml&logoColor=white)](https://es.wikipedia.org/wiki/Extensible_Markup_Language)
## CSV

### Datos Importantes

- Los archivos CSV usan comas como separador y una cabecera sigue el mismo orden de atributos.
- Recomendable tratar valores entre comillas y usar encoding='latin1' si hay tildes o caracteres españoles
- El acceso puede ser por índices (reader) o por claves (DictReader).


### Práctica 1: Sumar importes por asociación

#### Paso 1: Crear/usar el archivo `subvenciones.csv` con cabecera y datos.

Ejemplo:

```
"Asociación","Actividad Subvencionada","Importe"
"AMPA ANTONIO MACHADO","TALLER FIESTA DE CARNAVAL","94.56"
"AMPA ANTONIO MACHADO","TALLER DIA DEL PADRE","39.04"
```


#### Paso 2: Leer y sumar importes en Python

```python
import csv

with open('subvenciones.csv', encoding='latin1') as fichero_csv:
    dict_lector = csv.DictReader(fichero_csv)
    asocs = {}
    for linea in dict_lector:
        centro = linea['Asociación']
        subvencion = float(linea['Importe'])
        asocs[centro] = asocs.get(centro, 0) + subvencion
    print(asocs)
```

*Comprobar que la suma se realizó bien y que los nombres de columnas son exactos*.

### Práctica 2: Modificar y añadir columnas

#### Paso 1: Añadir dos columnas (Justificación requerida/recibida)

```python
with open('subvenciones.csv', encoding='latin1') as fich_lect, \
     open('subvenciones_esc.csv', 'w', encoding='latin1') as fich_escr:
    dict_lector = csv.DictReader(fich_lect)
    campos = dict_lector.fieldnames + ['Justificación requerida', 'Justificación recibida']
    escritor = csv.DictWriter(fich_escr, fieldnames=campos)
    escritor.writeheader()
    for linea in dict_lector:
        linea['Justificación requerida'] = "Sí" if float(linea['Importe']) > 300 else "No"
        linea['Justificación recibida'] = "No"
        escritor.writerow(linea)
```

*Verifica la creación del nuevo archivo y que las columnas estén agregadas*.

***

## TSV

### Datos Importantes

- Igual a CSV, pero las columnas se separan por tabuladores (`\t`).
- Usa el parámetro `delimiter='\t'` en DictReader y DictWriter.


### Práctica 3: Convertir CSV en TSV

#### Paso 1: Leer un archivo CSV y escribir uno TSV

```python
import csv

with open('subvenciones.csv', encoding='latin1') as fich_lect, \
     open('subvenciones.tsv', 'w', encoding='latin1') as fich_escr:
    dict_lector = csv.DictReader(fich_lect)
    escritor = csv.DictWriter(fich_escr, delimiter='\t', fieldnames=dict_lector.fieldnames)
    escritor.writeheader()
    for linea in dict_lector:
        escritor.writerow(linea)
```


#### Paso 2: Leer TSV y sumar importes

```python
with open('subvenciones.tsv', encoding='latin1') as fich:
    dict_lector = csv.DictReader(fich, delimiter='\t')
    asocs = {}
    for linea in dict_lector:
        centro = linea['Asociación']
        subvencion = float(linea['Importe'])
        asocs[centro] = asocs.get(centro, 0) + subvencion
    print(asocs)
```

*Recuerda revisar separadores y cabeceras exactas*.

***

## Excel

### Datos Importantes

- Los archivos Excel son libros con hojas y celdas con índices desde cero en Python.
- Usar `xlrd` para leer y `xlwt` para escribir; `pandas` permite manipulación avanzada.


### Práctica 4: Leer Excel y sumar importes

#### Paso 1: Leer con xlrd

```python
import xlrd

with xlrd.open_workbook('subvenciones.xls') as libro:
    asocs = {}
    for hoja in libro.sheets():
        for i in range(1, hoja.nrows):
            fila = hoja.row(i)
            asoc = fila.value
            subvencion = fila.value
            asocs[asoc] = asocs.get(asoc, 0) + subvencion
    print(asocs)
```


### Práctica 5: Crear hoja resumen y fórmulas con xlwt

#### Paso 1: Crear hoja nueva con totales

```python
import xlwt

libro_escr = xlwt.Workbook()
hoja_escr = libro_escr.add_sheet('Totales')

hoja_escr.write(0, 0, "Asociación")
hoja_escr.write(0, 1, "Importe total")
hoja_escr.write(0, 2, "Importe justificado")
hoja_escr.write(0, 3, "Restante")

for i, (asoc, total) in enumerate(asocs.items()):
    fila = i + 1
    hoja_escr.write(fila, 0, asoc)
    hoja_escr.write(fila, 1, total)
    hoja_escr.write(fila, 2, 0)
    formula = f"C{fila+1}-B{fila+1}"
    hoja_escr.write(fila, 3, xlwt.Formula(formula))

libro_escr.save('resumen.xls')
```

*Abre el archivo con Excel para ver fórmulas funcionando.*

### Práctica 6: Copiar hojas con pandas

```python
import pandas

with pandas.ExcelFile('subvenciones.xls') as xl:
    escritor = pandas.ExcelWriter('subvenciones_copia.xls')
    for nombre in xl.sheet_names:
        df = xl.parse(nombre)
        df.to_excel(escritor, nombre)
    escritor.save()
```

*Perfecto para grandes volúmenes y análisis avanzado.*

***

## JSON

### Datos Importantes

- Estructura flexible con objetos (clave:valor) y listas; puede haber jerarquía.
- Lee con `json.load`, escribe con `json.dump`; ojo al convertir cadenas en números.


### Práctica 7: Reorganizar estructura y sumar por asociación

#### Paso 1: Transformar estructura simple en jerárquica

```python
import json

with open('subvenciones.json', encoding='utf-8') as fich_lect, \
     open('subvenciones_reformateado.json', 'w', encoding='utf-8') as fich_escr:
    datos = json.load(fich_lect)
    asoc_str = "Asociación"
    act_str = "Actividad Subvencionada"
    imp_str = "Importe en euros"
    lista, list_act = [], []
    asoc_actual, dicc = "", {}
    for elem in datos:
        asoc = elem[asoc_str]
        act = elem[act_str]
        imp = elem[imp_str]
        if asoc_actual != asoc:
            if asoc_actual != "":
                dicc["Actividades"] = list_act
                lista.append(dicc)
            list_act = []
            dicc = {"Asociación": asoc}
        list_act.append({act_str: act, imp_str: imp})
        asoc_actual = asoc
    if dicc and list_act:
        dicc["Actividades"] = list_act
        lista.append(dicc)
    json.dump(lista, fich_escr, ensure_ascii=False, indent=4)
```

*Abre el archivo resultante para comprobar la organización por asociación y actividades.*

***

## XML

### Datos Importantes

- XML es jerárquico, etiquetas/nodos anidados; manipula fácil con `ElementTree`.
- El acceso a hijos por índice y nombre es común.


### Práctica 8: Leer XML y organizar por asociación

#### Paso 1: Suma de importes por asociación

```python
import xml.etree.ElementTree as ET

arbol = ET.parse('subvenciones.xml')
raiz = arbol.getroot()
asocs = {}
for fila in raiz.findall('Row'):
    centro = fila.find('Asociaci_n').text
    subvencion = float(fila.find('Importe').text)
    asocs[centro] = asocs.get(centro, 0) + subvencion
print(asocs)
```


### Práctica 9: Crear árbol nuevo de asociaciones y actividades

#### Paso 1: Crear XML con estructura avanzada

```python
nuevo = ET.ElementTree()
raiz_nueva = ET.Element("Raiz")
nuevo._setroot(raiz_nueva)

for centro, total in asocs.items():
    elem_actual = ET.SubElement(raiz_nueva, "Asociacion")
    elem_actual.set('nombre', centro)
    actividades = ET.SubElement(elem_actual, "Actividades")
    # Por simplicidad, asociar aquí las actividades si se dispone del listado original
    gas_total = ET.SubElement(elem_actual, "Total")
    gas_total.text = str(total)

nuevo.write('subvenciones_reorganizado.xml')
```

*Abre el nuevo XML para verificar el árbol y las sumas por asociación.*

***

## Recomendaciones Generales

- Usa nombres de columnas/campos identicos en código y archivos.
- Revisa la codificación (`latin1` para español, `utf-8` para internacional).
- Antes de pasar a cada siguiente práctica, valida los resultados de salida de los archivos generados.
- Utiliza Python 3 y las versiones recomendadas de las librerías para compatibilidad completa.

***
<p align="right">
  <a href="/Unidad_2/src/Scrapping.md">
    <img src="/Assets/arrow.png" width="75" height="75" alt="Índice">
  </a>
</p>
